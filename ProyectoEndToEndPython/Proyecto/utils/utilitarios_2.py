import os
import yaml
from io import StringIO
import pandas as pd
from google.cloud.storage import Client
from azure.storage.blob import ContainerClient
from pymongo import MongoClient

#Loading the credentials from config

CONFIG_DIR="/user/app/ProyectoEndToEndPython/Proyecto/config/config.yml"

with open(CONFIG_DIR,"r") as file:
        config=yaml.safe_load(file)



# Utilitarios para Google Cloud Storage
def get_cliente_cloud_storage():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=config["cloud_storage"]["credentials"]
    client = Client() #json de cuenta de servicio

    return client

# Utilitarios para Azure Blob Storage
def get_cliente_azure_storage(containerName):
    conn_str = config["azure_storage"]["connection_string"]
    container = containerName
    container_client = ContainerClient.from_connection_string(conn_str=conn_str,container_name=container)
    
    return container_client
    

    
#Utilitario mongodb

def get_mongo_client(database_name):
    # Configure la cadena de conexion para Mongo DB Atlas
    connection_string = config["mongo_db"]["connection_string"]
    # Crea el cliente de MongoDB Atlas
    client = MongoClient (connection_string)
    # Selecciona la base de datos
    db = client[database_name]
    return db      
