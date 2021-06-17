# Course Certificate Generator 
Simple Certificate/Award Generator Utility deployed as a Web App

Simple and dynamic course/event certificate generator. Easy to use and customizable. Simply generate customized certificates by selecting template, recipient name, event/Course name and Date of event/Course. 

## Getting Started
Instructions will get you a copy of the project up and running on a local machine and deploy to Cloud.

### Prerequisites
[ **Python (> Python 3.5)**](https://www.python.org/) .

#### Get the project.

```sh
$ git clone 

```
### Install Dependencies
Highly recommend using Python virtual environments (pyenv or virtualenv) 
```sh
$ cd certificate-generator
$ pip install -r requirements.txt 
```

## Configuration
1. Edit Configuration ['**config.ini**'](https://github.com/hm82/award-gen/config.ini) file. A properly configured file should look like :

```
[SETTINGS]
TEMPLATE = templates/example-template.jpg

[NAME]
NAME_FONT = fonts/Cookie-Regular.ttf
NAME_FONT_SIZE = 35
NAME_COLOR = rgb(0,0,0)
NAME_X = 122
NAME_Y = 220
NAME_WIDTH = 404

[EVENT]
EVENT_FONT = fonts/Kanit-Regular.ttf
EVENT_FONT_SIZE =30
EVENT_COLOR = rgb(0,0,0)
EVENT_X = 122
EVENT_Y = 318
EVENT_WIDTH = 404

[DATE]
DATE_FONT = fonts/Kanit-Regular.ttf
DATE_FONT_SIZE = 21
DATE_COLOR = rgb(0,0,0)
DATE_X = 90
DATE_Y = 375
DATE_WIDTH = 126
```
### OPTIONS 
| OPTION | DESCRIPTION |
| ------ | ------ |
| TEMPLATE | **Path of the Template** (IMAGE) of the Certificate |
| *_FONT | **Path of Font File** (.ttf) that will be use for * field in the Certificate |
| *_FONT_SIZE | **Font Size** that will be use for * field in the Certificate  |
| *_COLOR | **Font Color** that will be use for * field in the Certificate |
|*_X | **X Co-ordinate** from where the * field begins in the Certificate |
|*_Y | **Y Co-ordinate** from where the * field begins in the Certificate |
|*_WIDTH | **Width** of the * field in the Certificate |

##### * can be replaced with NAME/DATE/EVENT

## Running Certificate Generator locally
The project comes with 2 samples programs 
2. [test.py](https://github.com/hm82/award-gen/test.py) : It is an example that demonstrates how **Certificate Generator** can be implemented in already existing projects.
```sh
$ python test.py

>>  CERTIFICATE GENERATED AND SAVED AS : certificate_.png  <<
STATUS : SUCCESSFUL
```
2. 1. [certificate_cli.py](https://github.com/hm82/award-gen/certificate_cli.py). A CLI example to use **Certificate Generator** directly from the command line.

```sh
$ python certificate_cli.py -n "Tony Stark" -e "AVENGERS REBOOT 2021" -d "9/9/2021" -o SampleCertificate.png

** DATA TO BE USED **
>> NAME : Tony Stark
>> EVENT : AVENGERS REBOOT 2021
>> DATE : 9/9/2021
>> OUTPUT FILE : SampleCertificate.png

!! Can we proceed? [y/n]:y

>>  CERTIFICATE SAVED AS : SampleCertificate.png <<
```

## Dependencies

- **[PILLOW](https://pillow.readthedocs.io/en/stable/)** : For Image Processing
- **[Configparser](https://docs.python.org/3/library/configparser.html)** : For reading config file.
- **[Flask](https://flask.palletsprojects.com/en/2.0.x/)** : For web application

## Contributing
All contributions/reuse are welcomed