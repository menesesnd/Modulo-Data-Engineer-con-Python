# Modulo-Data-Engineer-con-Python
Trabajo final de Modulo
El objetivo de estar demostrar el flujo ETL en python usando apache airflow como orquestador.

## Pre requisitos
Tener instalado Docker con los contenedores de jupyter y SQL, se uilizara para al ejcucion de scripts  de python y apache airflow
Tener las tablas en las fuentes de datos correspodientes (Azure Datalake Storage, Cloud Datalake Storage, MySQL Workbench, MongoDB)

# Crear cluster con docker file

    A partir del archivo [docker-compose.yml](https://github.com/menesesnd/Modulo-Data-Engineer-con-Python/blob/8e763a885a9f3e22b9b428e3980f60f75cfc0d2e/ProyectoEndToEndPython/Proyecto/docker-compose.yml) vamos a crear nuestro cluster.

    Abrimos un cmd y nos ubicamos donde se encuentra el archivo .yml, ejecutando este comando:

    ```bash
    docker compose -f docker-compose.yml up -d
    ```
    Esperamos unos minutos hasta que termine de crearse los contenedores de nuestro cluster.

    Abrir el siguiente link para validar la instalacion:

    [localhost:8200](http://localhost:8200/)
    Y en esta parte creamos o colocamos los archivos del respositorio para las ejecuciones de prueba correspondientes.
## Explicación de la ingesta de Datos
En el repositorio de GitHUB se tiene 4 carpetas las cuales se pasara a explicar el contenido de cada uno:
* Config : Contiene las informacion de las credenciales a las conexiones de distinas fuentes de informacion (Azure, GCP, MongoDB)
* Credentials : Contiene archivos que son credenciales en este caso un json con conexion a GCP 
* Process : Contiene archivos python, los cuales son los siguientes:
  * Extract_2:  Contiene la funciones de extraccion de distinas fuentes de información
  * Load_2: Contiene las funciones de carga para distinas fuentes de información
  * Tranform_2: Contiene las funciones de tranformaciones o consultas requeridas por el usuario que posteriormente son cargadas usando Load_2.py para distinas fuentes de información
* Utils : Contiene las funciones de conexiones a distintas fuentes de información como Azure, GCP o MongoDB.

 Para el desarrollo de ETL, se creo un archivo Ingest-2.pynb ejecuta por partes cada codigo de extracion , tranformacion y carga y que este todo bien para orquestación en apache airflow, ya habiendo validado todo lo anterior se migra a un archivo Ingest-2.py

 Luego se ejecutara los scripts o codigos del apache airflow , los cuales se puede utilizar los codigos en el archivo apache airflow.txt con las recomendaciones.
 Y por finalizar se mostrara la evidencia de la ejecucion del script Ingest-2.py con apache airflow, con los detalles de la ejecución.
 
  
