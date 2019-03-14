# DEV CORNERSHOP TEST

Esta aplicación intenta cumplir con los requerimientos del test para desarrollador python en cornershop. 

https://github.com/cornershop/backend-test

##TODO

Falta testing

## Installation
Python 3.7

## Installation

pip install -r requirements.txt


## Usage

Desde Windows seguir los siguientes pasos:

cd Dev

Scripts\Activate

cd src

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

## Creating nora user

Browse the following url to create "nora" user in database

http://localhost:8000/createuser/

This will create user nora with 1234 as the password.

## Images

Ejemplo de envio del reminder al usuario

![image](https://github.com/miguelaav/dev/blob/master/reminder.png)

Ejemplo de visualizacion de opciones del menu y opcion de envio de slack

![image](https://github.com/miguelaav/dev/blob/master/demo_vistaslack.png)

Ejemplo de respuesta cuando ya se ha respondido el menu

![image](https://github.com/miguelaav/dev/blob/master/demo_peticion.png)

Creacion de usuario sin usar admin

![image](https://github.com/miguelaav/dev/blob/master/createuser.png)






## License
[MIT](https://choosealicense.com/licenses/mit/)