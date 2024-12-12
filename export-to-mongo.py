import requests
import time
from pymongo import MongoClient

endpoint = 'https://api.citybik.es/v2/networks/bicicorunha'

# Connection to the database
client = MongoClient('localhost:27017')
db_name = client['citybik']
collection_name = db_name['bikestations']

# Function that exports the data from the API and inserts it in the mongo database
def accessAPI(endpoint):

    response = requests.get(endpoint)

    try:
        if response.status_code == 200 :
            # We only want the stations, wich are inside of an object 'network'
            station_list = response.json().get('network',{}).get('stations',[])
            result = collection_name.insert_many(station_list)
            print(f'Inserted {len(result.inserted_ids)} documents with IDs: {result.inserted_ids}')
        else :
            print('Error al acceder a la API, compruebe que el endpoint sea correcto.')
    except Exception as e:
        print(f'Error inesperado: {e}')

# Reconnect to the API every 5 minutes
while True:
    accessAPI(endpoint)
    time.sleep(300)