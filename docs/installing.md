# Installing

## Requirements
Kitsu.py requires Python 3.8+. You can download the latest version of Python [here](https://www.python.org/downloads/)
* [aiohttp](https://pypi.org/project/aiohttp/)
* [python-dateutil](https://pypi.org/project/python-dateutil)

```{note}
You don't have to install the packages manually as they will be installed automatically with pip.
Just ensure you have python setup and pip added to path.
```

## Installing Stable Version

Kitsu.py is distributed on [PyPI](https://pypi.org/project/kitsu.py/), You can use pip to install it.
To install the library, run the following command:
````{tab} Windows
```console
$ py -3 -m pip install -U kitsu.py
```
````


````{tab} MacOS/Linux
```console
$ python3 -m pip install -U kitsu.py
```
````

## Installing Developement Version

```{admonition} Caution
:class: caution

Make sure you have Installed & Setup git before proceeding.
```
```{admonition} Warning
:class: attention

Installing the developement version is not recommended as the it might have bugs.
```

To install the developement version run the following command:

````{tab} Windows
```console
$ py -3 -m pip install -U git+https://github.com/MrArkon/Kitsu.py.git
```
````


````{tab} MacOS/Linux
```console
$ python3 -m pip install -U git+https://github.com/MrArkon/Kitsu.py.git
```
````