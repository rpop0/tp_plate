# Plate Recognition Program

This repository consists the plate recognition program written in Python for the UVT Team Project, Year 2, Semester 2, 2021.

Contributors:
* Rosian Pop (Team Leader)
* Patrick Lenis
* Paul Cvasa

## Setup requirements

In order to start working on this project, you need the following things:

* Python 3.9.2
* pip
* "virtualenv" Python Package
* opencv-python 4.5.1.48 Python Package

### Setting up the project

This section will guide you in setting up the project and the envirnoment. An important thing about this project is that we will be using python virtual envirnoments, and we will be specifically using the "virtualenv" python package. First things first, you need to clone this repository and then you will need to install the **virtualenv** python package, by running the following command:

```
python3 -m pip install virtualenv
```

Then, you will need to create a python virtual envirnoment in your projects folder by running this command:

```
python3 -m virtualenv venv
```

Note, you can replace *venv* with any other name you'd like your envirnoment to have. You will see that after running the command, a new folder will be created named **venv**. In order to activate the virtual envirnoment, depending on your platform you need to run a specific command:

**Mac OS / Linux**
```
source venv/bin/activate.sh
```

**Windows**
```
venv\Scripts\activate
```

Note, you will need to do this *every time* you will be running this the application. If it worked, your command prompt should be prefixed by **(venv)**.

[![image.png](https://i.postimg.cc/j5QR6j55/image.png)](https://postimg.cc/wyMKggD8)

If you look through the files you downloaded through the repository, you should see a **requirements.txt** file. This file can be used by Python's package installer, *pip*, in order to install all of the required packages automatically. After you activate the virtual envirnoment, you can run the following command to download all the packages and install them.

```
python3 -m pip install -r requirements.txt
```

And that is it! You should have all the required packages installed in the envirnoment in order to develop and run this program.