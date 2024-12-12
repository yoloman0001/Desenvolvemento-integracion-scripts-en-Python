# Desenvolvemento-integracion-scripts-en-Python :snake:

## :book: Descripción

Este repositorio contiene las herramientas necesarias para acceder a una API periodicamente y guardar sus datos en una base de datos MongoDB.

## :open_file_folder: Estructura
- 

## :wrench: Requisitos previos

### :arrow_down: Clonar repositorio en local

Clona este repositorio en tu máquina local usando la URL o usando una clave SSH.

Con URL

~~~
git clone https://github.com/yoloman0001/Desenvolvemento-integracion-scripts-en-Python.git
~~~

Con SSH key

~~~
git clone git@github.com:yoloman0001/Desenvolvemento-integracion-scripts-en-Python.git
~~~

### :link: Instalar dependencias

Crea un environment con conda (opcional)

~~~
conda create --name nombre-environment python=3.12
~~~

Las dependencias necesarias vienen definidas en un archivo `requirements.txt`
~~~
pip install -r requirements.txt
~~~

### :leaves: Crear una base de datos Mongo

Crea un contenedor de Docker con una base de datos Mongo

~~~
docker pull mongo
docker run -p 27017:27017 --name mongobikes
~~~

## :arrow_forward: Ejecución

Ejecuta primero el script `export-to-mongo.py`, y luego desde otra consola (el primer script se va a estar ejecutando hasta que se cancele la ejecución) ejecuta `read-from-mongo.py`

Comandos para ejecutar desde consola
~~~
python export-to-mongo.py
python read-from-mongo.py
~~~