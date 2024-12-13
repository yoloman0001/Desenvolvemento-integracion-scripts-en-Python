import requests
import time
from pymongo import MongoClient
import logging

# Set up logging
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

endpoint = 'https://api.citybik.es/v2/networks/bicicorunha'

# Connection to the database
MONGO_URI = 'mongodb://mongobikes:27017'
client = MongoClient(MONGO_URI) 
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
            logger.info(f'Inserted {len(result.inserted_ids)} documents with IDs: {result.inserted_ids}')
        else :
            logger.info('Error when trying to access the  API, check if the endpoint is correct.')
    except KeyboardInterrupt :
        logger.info('Interrupted by user')
    except Exception as e:
        logger.info(f'Unexpected error: {e}')

# Reconnect to the API every 5 minutes
while True:
    accessAPI(endpoint)
    time.sleep(300)