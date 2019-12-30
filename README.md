# Nao Garden

![Logo](Doc/image/logo-small.png)

Nao Garden was a Licence 3 project supervised by Jean-Charles MARTY and François Colin.
We were a team of 5 students:

* Swan
* Thomas
* Maël
* Sébastien
* Tristan

The objective was to learn with a robot in our case we use Nao and his goal his to help you gardening.

For more information see [my website](https://swan-blanc.fr/nao-garden/) or the [project doc](http://nao-garden.swan-blanc.fr/)

## Installation.

For this project you will need a python 2.7 version.

First you lust install naoqi python [SDK version 1.14.5](https://community.ald.softbankrobotics.com/en/resources/software/former-nao-versions-python-naoqi-sdk)

To test open python 2.7 console and try to import `naoqi`

You will need the following package:
    
    sudo apt install virtualenv
    sudo apt install python-pip
    sudo apt install python-tk
    sudo apt install cmake
 
Prepare your virtualenv:

    virtualenv -p python3 venv
    . venv/bin/activate
    pip install -r requirements.txt   

If you want to exit your virtualenv:

    deactivate

And you can follow the [doc instruction](http://nao-garden.swan-blanc.fr/Installation.html)

**Note** I dont provide the Nao Creator UI because his not work really well XD

Be indulgent his a old school code XD.
