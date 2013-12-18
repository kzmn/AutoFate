AutoFate
========

A set of web based tools for the Fate Core RPG system built on top of Angular.js and Django.

The web service is hosted at api/.

In order to get started:
------------------------

### Requirements ###
- Python 3.3
- pip
- virtualenv

### Setting up the virtual environment ###
On Windows run in cmd:

	cd <project root directory>
	virtualenv env
	env\Scripts\activate
	pip install requirements.txt

On Linux:

	cd <project root directory>
	virtualenv env
	source env/bin/activate
	pip install requirements.txt

### Setting up the database ###

	manage.py syncdb

### Running the development server ###

	manage.py runserver

### Exiting the virtual environment ###

	deactivate