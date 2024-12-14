# Desenvolvemento-integracion-scripts-en-Python :snake:

## :book: Descripción

Este repositorio contiene dos scripts de `Python` para realizar una tarea de acceso a APIs. El primer script accede a la API periódicamente (5 min.) y lee los datos sobre las estaciones de bicicletas en A Coruña y los guarda en una base de datos MongoDB; el segundo script se conecta a la base de datos, toma los datos, y los convierte en ficheros `.csv` y `.parquet`

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

Las dependencias necesarias para el primer script (export-to-mongo.py) se importarán al ejecutar el `Dockerfile`.

Las dependencias necesarias para ejecutar el segundo script (read-from-mongo.py) vienen definidas en el archivo `requirements.txt`.
~~~
pip install -r requirements.txt
~~~

Crea un contenedor de Docker con una base de datos Mongo.

~~~
docker pull mongo
docker run -p 27017:27017 --name mongobikes
~~~

## :arrow_forward: Ejecución

### 💼 Arrancar los contenedores de Docker

Ejecuta el siguiente comando para arrancar dos contenedores, uno ejecutará el script `export-to-mongo.py` segun lo definido en el `Dockerfile`. El segundo contenedor desplegará la base de datos Mongo.

~~~
docker-compose build -t
~~~

Una vez hayas comprobado que los contenedores están en marcha; desde consola, sitúate dentro de la carpeta `/code` y ejecuta `read-from-mongo.py`

~~~
cd code/
python read-from-mongo.py
~~~

Tras ejecutar este script, deberías ver cómo se crean dos archivos en la carpeta `/data`

