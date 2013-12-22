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
- node js

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

### Setting Retrieving Node Libraries###

    npm install

### Using grunt ###

Simply type grunt <commandName> into the console window for the command that you
want to run.  The grunt default will start the watcher that currently watches
less files and compiles them to css.  example:

    grunt less