import inspect
import os
import sys
from jinja2 import Template

current_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
this_file_path = os.path.dirname(os.path.abspath(__file__))

def print_usage():
    print """
    Usage: flask-project <project_name>
    """


class FlaskProjectCreatorException(Exception):
    def __init__(self, msg):
        super(FlaskProjectCreatorException, self).__init__(msg)


class FlaskProjectCreator(object):
    def __init__(self, project_name):
        self.project_name = project_name

    def create(self):
        self._create_directory(self.project_name)
        self._install_flask()
        self._create_files()

    def _create_directory(self, project_name):
        self.dir_name = os.path.dirname(os.path.join(current_path, project_name))
        self.app_dir = os.path.dirname(os.path.join(self.dir_name, 'app'))
        db_dir = os.path.dirname(os.path.join(self.dir_name, 'db_repository'))
        static_dir = os.path.dirname(os.path.join(self.app_dir, 'static'))
        template_dir = os.path.dirname(os.path.join(self.app_dir, 'templates'))
        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)
            os.mkdir(self.app_dir)
            os.mkdir(db_dir)
            os.mkdir(static_dir)
            os.mkdir(template_dir)
        else:
            msg = "Project: {0} already exists in path: {1}".\
                format(project_name, current_path)
            raise FlaskProjectCreatorException(msg)

    def _install_flask(self):
        os.popen("pip install virtualenv")
        os.popen("cd {0}; virtualenv {1}".format(self.dir_name, self.project_name))
        os.popen("cd {0}; source {1}/bin/activate".format(self.dir_name, self.project_name))
        os.popen("cd {0}; pip install flask".format(self.dir_name))
        os.popen("cd {0}; pip install flask-login".format(self.dir_name))
        os.popen("cd {0}; pip install flask-mail".format(self.dir_name))
        os.popen("cd {0}; pip install flask-sqlalchemy".format(self.dir_name))
        os.popen("cd {0}; pip install sqlalchemy-migrate".format(self.dir_name))
        os.popen("cd {0}; pip install flask-whooshalchemy".format(self.dir_name))
        os.popen("cd {0}; pip install flask-wtf".format(self.dir_name))
        os.popen("cd {0}; pip install flask-babel".format(self.dir_name))
        os.popen("cd {0}; pip install guess_language".format(self.dir_name))
        os.popen("cd {0}; pip install flipflop".format(self.dir_name))
        os.popen("cd {0}; pip install coverage".format(self.dir_name))

    def _create_files(self):
        self._create_init()
        self._create_file(os.path.dirname(os.path.join(self.app_dir, "forms.py")))
        self._create_file(os.path.dirname(os.path.join(self.app_dir, "models.py")))
        self._create_file(os.path.dirname(os.path.join(self.app_dir, "views.py")))
        self._create_file(os.path.dirname(os.path.join(self.dir_name, "config.py")))
        self._create_file(os.path.dirname(os.path.join(self.dir_name, "db_create.py")))
        self._create_file(os.path.dirname(os.path.join(self.dir_name, "db_migrate.py")))
        self._create_file(os.path.dirname(os.path.join(self.dir_name, "db_downgrade.py")))
        self._create_file(os.path.dirname(os.path.join(self.dir_name, "fb_upgrade.py")))
        self._create_file(os.path.dirname(os.path.join(self.dir_name, "run.py")))
        self._create_file(os.path.dirname(os.path.join(self.dir_name, "tests.py")))

    def _create_file(self, name):
        template_file_name = name.split("/")[-1]
        template_path = os.path.dirname(os.path.join(this_file_path, 'templates'))
        template_file_path = os.path.dirname(os.path.join(template_path, template_file_name))

        with open(template_file_path) as t_file, open(name, 'w+') as o_file:
            data = t_file.read()
            t = Template(data)
            o_file.write(t.render(project=self.project_name))

    def _create_init(self):
        with open("%s/../templates/__init__.py" % this_file_path) as t_file,\
                open("%s/__init__.py" % self.app_dir, 'w+') as o_file:
            data = t_file.read()
            t = Template(data)
            o_file.write(t.render(project=self.project_name))





def main():
    project_name = sys.argv[0]
    if not project_name:
        print_usage()
        exit(1)
    else:
        try:
            print "Creating %s" % project_name
            FlaskProjectCreator(project_name).create()
            print "Finished"

        except Exception as e:
            print "Error:", e
            exit(1)




if __name__ == "__main__":
    main()