import os
import sys
import json
import certifi #for secure HTTP connection using trusted certified certificates to signify valid request.
import pandas as pd
import numpy as np
import pymongo
from dotenv import load_dotenv
from network_security.exception.exception import CyberSecurityException
from network_security.logging.logger import logging

load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

ca=certifi.where()#path to the bundle of certified certificates for SSL and TSL connections.

class CyberSecurityDataExtract():
    def __init__(self):
        try:
            self.database = ''
            self.collection= ''
        except Exception as e:
            raise CyberSecurityException(e, sys)

    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = data.to_dict('records')
            
            return records
        except Exception as e:
            raise CyberSecurityException(e, sys)
        
    def insert_data_to_mongodb(self, records, database, collection):
        try:
            self.database = database  
            self.collection = collection  
            self.records = records  
        
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)  # Added tlsCAFile parameter
        
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise CyberSecurityException(e, sys)
    
if __name__ == '__main__':
    FILE_PATH="network_data/phisingData.csv"
    DB="DANISHMONGO"
    Collection="PhishingData"
    networkobj=CyberSecurityDataExtract()
    records=networkobj.csv_to_json_converter(file_path=FILE_PATH)
    print(f'type or record variable:{type(records)}')
    no_of_records=networkobj.insert_data_to_mongodb(records,DB,Collection)
    print(no_of_records)

