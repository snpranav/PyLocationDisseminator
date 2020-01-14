#!/usr/bin/env python
"""PyLocationDisseminator is a script that uses an IP Location API to disseminate location details of your device.
"""

__author__ = "Pranav Shikarpur"
__credits__ = "Pranav Shikarpur"
__version__ = "1.0.1"

from requests import get
import datetime, pymongo
from os import environ

def writetodb(loc):
    # Creating connection with DB
    client = pymongo.MongoClient("mongodb://" + environ.get('IP_ADDRESS') + ":" + environ.get('PORT'))
    dbName = client[environ.get('DB_NAME')]
    collectionName = dbName[environ.get('COLLECTION_NAME')]

    collectionName.insert_one(loc)

def get_location_from_ip():
    location = get(environ.get('API_URL')+environ.get('API_KEY'))
    location_dict = location.json()
    location_dict['datetime'] = datetime.datetime.now()
    return location_dict

def main():
    # Pinging IP Location api for location details
    locationDetails = get_location_from_ip()
    # Using location details to write into the mongo db
    writetodb(locationDetails)


if __name__ == "__main__":
    main()