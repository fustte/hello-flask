# hello-flask
Conocemos el framework para web: Flask

## A tener en cuenta

Flask necesita un servidor web para funcionar.
El servidor web es el encargado de recibiri las peticiones
HTTP del navegador y enviarlas al programa que
hacemos en Flask. Flas le da el resultado al servidor
web y este se lo envia al navegador.

Para simplificar el escenadrio, por el momento solamente
vamos a uilizar el **SERVIDOR WEB DE DESARROLLO** que nos
proporciona FLask. Este servidor no sirve para poner una
aplicacion pública en internet en modo produccion. solamente
sirve en el escenario en el que estamos desarrollamndo
localmente nuestra aplicacion.

## Variables de entorno

- Linux / Mac
  export FLASK_APP=hola
  export FLASK_DEBUG=True

- Windows
  set FLASK_APP=hola
  set FLASK_DEBUG=True