import os
import subprocess
import sys

import pip
from jinja2 import Template


current_path = os.getcwd()
this_file_path = os.path.dirname(os.path.abspath(__file__))
FLASK_PACKAGES = [
    "Flask==0.10.1",
    "Flask-Alembic==1.2.1",
    "Flask-Login==0.3.2",
    "Flask-Mail==0.9.1",
    "Flask-Migrate==1.6.0",
    "Flask-Principal==0.4.0",
    "Flask-SQLAlchemy==2.1",
    "Flask-Script==2.0.5",
    "Flask-Security==1.7.5",
    "Flask-WTF==0.12",
    "Jinja2==2.8",
    "Mako==1.0.3",
    "MarkupSafe==0.23",
    "MySQL-python==1.2.5",
    "SQLAlchemy==1.0.10",
    "WTForms==2.1",
    "Werkzeug==0.11.3",
    "alembic==0.7.7",
    "bcrypt==2.0.0",
    "blinker==1.4",
    "cffi==1.4.2",
    "itsdangerous==0.24",
    "nose==1.3.7",
    "passlib==1.6.5",
    "pycparser==2.14",
    "six==1.10.0",
    "wsgiref==0.1.2",
]


def print_usage():
    print """
    Usage: flask_project <project_name>
    """


def install(package):
    pip.main(['install', package])


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
        self.dir_name = os.path.join(current_path, project_name)
        self.app_dir = os.path.join(self.dir_name, 'app')
        static_dir = os.path.join(self.app_dir, 'static')
        template_dir = os.path.join(self.app_dir, 'templates')
        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)
            os.mkdir(self.app_dir)
            os.mkdir(static_dir)
            os.mkdir(template_dir)
        else:
            msg = "{0} already exists in {1}". \
                format(project_name, current_path)
            raise FlaskProjectCreatorException(msg)

    def _install_flask(self):
        install("virtualenv")
        command = ["cd {0}".format(self.dir_name),
                   "virtualenv venv",
                   "source {0}/bin/activate".format(self.project_name)]
        for package in FLASK_PACKAGES:
            command.append("pip install {0}".format(package))
        subprocess.call(";".join(command), shell=True)

    def _create_files(self):
        self._create_init()
        self._create_file(os.path.join(self.dir_name, "factory.py"))
        self._create_file(os.path.join(self.dir_name, "manage.py"))
        self._create_file(os.path.join(self.dir_name, "settings.py"))
        self._create_file(os.path.join(self.dir_name, "tests.py"))

    def _create_file(self, name):
        template_file_name = name.split("/")[-1]
        template_path = os.path.join(this_file_path, 'templates')
        template_file_path = os.path.join(template_path, template_file_name)

        with open(template_file_path) as t_file, open(name, 'w+') as o_file:
            data = t_file.read()
            t = Template(data)
            o_file.write(t.render(project=self.project_name))

    def _create_init(self):
        template_path = os.path.join(this_file_path, 'templates')
        with open("{0}/__init__.py".format(template_path)) as t_file, \
                open("{0}/__init__.py".format(self.app_dir), 'w+') as o_file:
            data = t_file.read()
            t = Template(data)
            o_file.write(t.render(project=self.project_name))


def main():
    project_name = sys.argv[1]
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