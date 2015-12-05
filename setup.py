from setuptools import setup, find_packages

setup(name='flask-project',
      version='0.1',
      description='A command line tool to create a skeleton flask project',
      url='https://github.com/sumanthns/flask-project.git',
      author='Sumanth Nagadavalli Suresh',
      author_email='nsready@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'jinja2',
      ],
      entry_points= {
          'console_scripts': ['flask-project=flask-project:main'],
      },
      zip_safe=False)
