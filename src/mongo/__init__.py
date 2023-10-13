
from typing import Dict
from pymongo import MongoClient
from termcolor import colored


class Mongo(object):
    def __init__(
        self,
        database: str,
        collection: str,
    ):
        self.database = database
        self.collection = collection

    def insert_doc(self, document: Dict):
        client = MongoClient('localhost', 27017)
        db = client[self.database]
        collection = db[self.collection]
        collection.insert_one(document)
        