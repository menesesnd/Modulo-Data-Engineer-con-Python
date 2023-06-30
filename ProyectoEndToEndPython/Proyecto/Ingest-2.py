from process.Extract_2 import Extract 
from process.Transform_2 import Transform
from process.Load_2 import Load 
import pandas as pd


extract = Extract()
transform = Transform()
load = Load()

print("INICIA EXTRACION DE DATOS")

customer_adls = extract.read_adls('source','retail/menesesnd/customers')
orders_adls = extract.read_adls('source','retail/menesesnd/orders')
order_items_adls = extract.read_adls('source','retail/menesesnd/order_items')
products_adls = extract.read_adls('source','retail/menesesnd/products')
categories_adls = extract.read_adls('source','retail/menesesnd/categories')
departments_adls = extract.read_adls('source','retail/menesesnd/departments')

categories_adls.head()

customer_sql = extract.read_mysql('retail_db','customers')
orders_sql = extract.read_mysql('retail_db','orders')
order_items_sql = extract.read_mysql('retail_db','order_items')
products_sql = extract.read_mysql('retail_db','products')
categories_sql = extract.read_mysql('retail_db','categories')
departments_sql = extract.read_mysql('retail_db','departments')

products_sql.head()

customer_cloud = extract.read_cloud_storage('datadep12','retail/customers')
orders_cloud = extract.read_cloud_storage('datadep12','retail/orders')
order_items_cloud = extract.read_cloud_storage('datadep12','retail/order_items')
products_cloud = extract.read_cloud_storage('datadep12','retail/products')
categories_cloud = extract.read_cloud_storage('datadep12','retail/categories')
departments_cloud = extract.read_cloud_storage('datadep12','retail/departments')

customer_cloud.head()

customer_mongoDB = extract.read_mongodb('retail_db',"customers")
orders_mongoDB= extract.read_mongodb('retail_db','orders')
order_items_mongoDB = extract.read_mongodb('retail_db','order_items')
products_mongoDB = extract.read_mongodb('retail_db','products')
categories_mongoDB = extract.read_mongodb('retail_db','categories')
departments_mongoDB = extract.read_mongodb('retail_db','departments')

order_items_mongoDB.head()

print("TERMINA EXTRACION DE DATOS")

print("INICIA CARGA DE DATOS A LANDING")

load.load_to_adls(customer_mongoDB,'source','landing/customers')
load.load_to_adls(orders_cloud,'source','landing/orders')
load.load_to_adls(order_items_sql,'source','landing/order_items')
load.load_to_adls(products_mongoDB,'source','landing/products')
load.load_to_adls(categories_cloud,'source','landing/categories')
load.load_to_adls(departments_sql,'source','landing/departments')

load.load_to_cloud_storage(customer_mongoDB,'datadep12','landing/customers')
load.load_to_cloud_storage(orders_adls,'datadep12','landing/orders')
load.load_to_cloud_storage(order_items_sql,'datadep12','landing/order_items')
load.load_to_cloud_storage(products_mongoDB,'datadep12','landing/products')
load.load_to_cloud_storage(categories_adls,'datadep12','landing/categories')
load.load_to_cloud_storage(departments_sql,'datadep12','landing/departments')

print("TERMINA CARGA DE DATOS A LANDING")

print("INICIA TRANFORMACION DE DATOS A GOLD")
customer_trans_adls = extract.read_adls('source','landing/customers')
orders_trans_adls = extract.read_adls('source','landing/orders')
order_items_trans_adls = extract.read_adls('source','landing/order_items')
products_trans_adls = extract.read_adls('source','landing/products')
categories_trans_adls = extract.read_adls('source','landing/categories')
departments_trans_adls = extract.read_adls('source','landing/departments')



df_enunciado1=transform.enunciado1(customer_trans_adls,orders_trans_adls,order_items_trans_adls)
df_enunciado2=transform.enunciado2(order_items_trans_adls,products_trans_adls,categories_trans_adls,)
df_enunciado3=transform.enunciado3(customer_trans_adls,orders_trans_adls,order_items_trans_adls,products_trans_adls,categories_trans_adls)
df_enunciado4=transform.enunciado4(customer_trans_adls,orders_trans_adls,order_items_trans_adls,products_trans_adls,categories_trans_adls)

df_enunciado3.head()
print("INICIA CARGA DE DATOS A GOLD")

load.load_to_adls(df_enunciado1,"source","gold/df_enunciado1")
load.load_to_adls(df_enunciado2,"source","gold/df_enunciado2")
load.load_to_adls(df_enunciado3,"source","gold/df_enunciado3")
load.load_to_adls(df_enunciado4,"source","gold/df_enunciado4")

print("TERMINA CARGA DE DATOS A GOLD")