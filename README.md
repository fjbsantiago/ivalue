# ivalue

This is a Dango Application that collects stocks financial data from different sources on the web and calculates the fittest for every day.


## Getting Started

These instructions will get a copy of the project up and running on your local machine for development and testing purposes.

### Installation Prerequisites

git

### Installing

These instructions explain how to set up a working local Development Environment

Install PyEnv

```
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
$ exec $SHELL (restart the shell)
```

Install Python 3.5.3 using PyEnv and set that version as active

```
$ pyenv install 3.5.3
$ pyenv local 3.5.3
```
Issues: Refer to https://github.com/pyenv/pyenv/wiki/Common-build-problems

Install Virtualenvwrapper plugin for PyEnv

```
$ git clone https://github.com/yyuu/pyenv-virtualenvwrapper.git ~/.pyenv/plugins/pyenv-virtualenvwrapper
```

Install Virtualenvwrapper scripts

```
$ export WORKON_HOME=$HOME/.virtualenvs
$ export PROJECT_HOME=$HOME/Devel (chose directory in which your projects will live)
$ source ~/.pyenv/shims/virtualenvwrapper.sh
```

Create a virtual environment, clone the project into it and set default folder for that project

```
$ mkproject ivalue
$ workon ivalue (activates virtual environment and switches to project's working dir)
$ git clone https://github.com/fjbsantiago/ivalue.git
```

Install Python dependencies

```
$ pip install -r requirements.txt
```

### Running the app

```
$ cd src/
$ python manage.py runserver
```

Open a browser on http://localhost:8000

## Authors

* **Francisco Santiago**
* **João Pio**
