# flask-project
A command line tool to create a skeleton flask project

Installation

1. Clone the project on your box
    git clone git@github.com:sumanthns/flask-project.git

2. Cd into the project folder
    cd flask-project

3. Install (Create a virtual env if required)
    python setup.py install

Usage:

flask-project <project-name>

Explanation

1. This will create a skeleton project structure in this format:

    project_name/  
        --  app/  
            ----  static/  
            ----  templates/  
            ----  __init__.py  
        --  run.sh
        --  run_tests.py
        --  manage.py
        --  factory.py
        --  settings.py

2. This will also create a virtual env called <project name> and install the below modules -

    flask-login  
    flask-mail  
    flask-sqlalchemy  
    sqlalchemy-migrate  
    flask-whooshalchemy  
    flask-wtf  
    flask-babel  
    guess-language  
    flipflop  
    coverage  
