import requests
import time
from pymongo import MongoClient

endpoint = 'https://api.citybik.es/v2/networks/bicicorunha'

client = MongoClient('localhost:27017')
db_name = client['citybik']
collection_name = db_name['bikestations']

def accessAPI(endpoint):

    response = requests.get(endpoint)

    if response.status_code == 200 :
        station_list = response.json().get('network',{}).get('stations',[])
        result = collection_name.insert_many(station_list)
        print(f'Inserted {len(result.inserted_ids)} documents with IDs: {result.inserted_ids}')
    else :
        print('Error al acceder a la API, compruebe que el endpoint sea correcto.')

while True:
    accessAPI(endpoint)
    time.sleep(600) # 600 segundos = 10 minutos