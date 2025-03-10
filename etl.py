import pandas as pd
import psycopg2
from sqlalchemy import create_engine
# extraction des fichiers plats (extract)
client = pd.read_csv('data/clients.csv',sep=';')
ventes = pd.read_csv('data/ventes.csv',sep=';')
sous_cat = pd.read_csv('data/produits_sous-categorie.csv',sep=';')
# (Transform)
# renommage des colonnes pour correspondre exactement a ce qu'il y aura dans les tables
client.columns = ['client_id', 'sex', 'birth']
ventes.columns = ['product_id', 'date', 'session_id', 'client_id', 'quantity_sold']
sous_cat.columns = ['product_id', 'category', 'sub_category', 'price', 'stock_quantity']
# concordance de la date
ventes['date'] = pd.to_datetime(ventes['date'], format='%d/%m/%Y %H:%M')
# concordance des types
ventes['quantity_sold'] = ventes['quantity_sold'].astype(int)
sous_cat['stock_quantity'] = sous_cat['stock_quantity'].astype(int)
sous_cat['price'] = sous_cat['price'].str.replace(',', '.', regex=False)
sous_cat['price'] = sous_cat['price'].astype(float)
# (load)
# connection a la base de donnée
# Assurez-vous que DATABASE_URL est correct
DATABASE_URL = "postgresql://user:password@my_postgres:5432/mydatabase"
engine = create_engine(DATABASE_URL)
# chargement en base de donnée
client.to_sql('client', engine, index=False, if_exists='replace')
ventes.to_sql('ventes', engine, index=False, if_exists='replace')
sous_cat.to_sql('sous_cat', engine, index=False, if_exists='replace')

print("Les données ont été chargées avec succès dans PostgreSQL.")