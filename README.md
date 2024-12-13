# Desenvolvemento-integracion-scripts-en-Python :snake:

## :book: Descripción

Este repositorio contiene las herramientas necesarias para acceder a una API periodicamente, guardar sus datos en una base de datos MongoDB y acceder a esos datos.

## :open_file_folder: Estructura
- `/code` - Carpeta que contiene los scripts para leer la API y para acceder a Mongo.
- `/data` - Carpeta donde se van a guardar los documentos generados con los datos de la base de datos.

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

Crea un environment con conda (opcional).

~~~
conda create --name nombre-environment python=3.12
~~~

Las dependencias necesarias para el primer script (export-to-mongo.py) vienen definidas en el `Dockerfile`.

Las dependencias necesarias para ejecutar el segundo script (read-from-mongo.py) vienen definidas en el archivo `requirements.txt`.
~~~
pip install -r requirements.txt
~~~

### :leaves: Crear una base de datos Mongo

Crea un contenedor de Docker con una base de datos Mongo.

~~~
docker pull mongo
docker run -p 27017:27017 --name mongobikes
~~~

## :arrow_forward: Ejecución

Para ejecutar el script `export-to-mongo.py` crea un contenedor usando `Dockerfile`, el script se va a estar ejecutando hasta que se cancele la ejecución.

~~~
docker built -t nombre_imagen .
docker run nombre_imagen
~~~

Desde consola ejecuta `read-from-mongo.py`

~~~
cd code/
python read-from-mongo.py
~~~