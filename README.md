# Glowing Barnacle

A basic project to improve quality of images with face

# Environement requirements

The devolopement environement was using: 
* python 3.8
* pip 19.2.3

# Tools used

This project use Django on the web server, and BasicSR as image processing tool.

# Installing the project


This process can take a while, as some dependencies are quite big.

```
$ git clone https://github.com/Krozark/glowing-barnacle.git
$ cd glowing-barnacle
$ pip install -e .
```

This will create several commands that all starts with `gb-`.

As some required dependencies don't respect the pip standard, a extra step is needed, and a helper was made to 
download and install them all at once. THis step will also setup all the environment (such as the database). 
This step can also take a while. 
```
$ gb-setup
```
In case of failure (internet connection lost, missing software ...), please fix it first, and then 
you will need to remove the following directory `glowing_barnacle/data/repo/` and re-run the previous command.


Note: 
During the installation process, the commands `gb-manage` and `gb-runserver` were created.
The first one is a direct link to the usual django manage.py file (`python manage.py`) and the second one
will start the development web server.


# Run the project

```
$ gb-runserver
```

And the go to `http://127.0.0.1:8000` to test the project


# Architecture

The project is composed of 2 mains directories

## glowing_barnacle

This is the directory tha contain all the images processing

## gb_backend

This is the django website project and all the standard filename are used


## data

This directory will be created at runtime and will contain all the files created
during the life cycle of the project (database, dependencies, file uploaded ...)
