from io import StringIO
import os
import sqlalchemy as db
from sqlalchemy import text
import pandas as pd
from pandas import DataFrame
from utils import utilitarios_2 as u
from pymongo import MongoClient
from azure.storage.blob import ContainerClient
from google.cloud.storage import Client


#engine = db.create_engine("mysql://root:root@192.168.1.7:3310/retail_db")
#conn = engine.connect()

#customers_df = pd.read_sql_query(text('SELECT * FROM customers'), con=conn)

class Extract():
    def __init__(self) -> None :
        self.process = "Extractprocess"

    def read_mysql(self,databaseName,tableName):
        
        engine = db.create_engine(f"mysql://root:root@192.168.1.7:3310/{databaseName}")
        conn = engine.connect()
        sql_query = pd.read_sql_query(text(f'SELECT * FROM {tableName}'), con=conn) #sqlalchemy 2.0.2
        #sql_query = pd.read_sql(text(f'SELECT * FROM {tableName}'), conn) #sqlalchemy 1.4.6
        df = pd.DataFrame(sql_query)
        
        return df
    
    def read_cloud_storage(self,bucketName,fileName):

        client = u.get_cliente_cloud_storage()
        bucket = client.get_bucket(bucketName)
        blob = bucket.get_blob(fileName)
        downloaded_file = blob.download_as_text(encoding = "utf-8")
        df = pd.read_csv(StringIO(downloaded_file))

        return df
        
    def read_mongodb(self,databaseName,collectionName):
        dbname = u.get_mongo_client(databaseName)
        collection_name = dbname[collectionName]
        customers = collection_name.find({})
        df = DataFrame(customers)

        return df

    def read_adls(self,containerName,fileName):

        container_client = u.get_cliente_azure_storage(containerName)
        downloaded_blob = container_client.download_blob(fileName)
        df = pd.read_csv(StringIO(downloaded_blob.content_as_text()))

        return df
        
    