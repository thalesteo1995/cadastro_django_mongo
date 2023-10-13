
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

    def insert(self, document: Dict):
        client = MongoClient("mongodb://%s:%s@127.0.0.1" % ("user", "pass"))
        db = client[self.database]
        collection = db[self.collection]
        collection.insert_one(document)
        print(colored(f"Documento: {document} inserido no BD!", color="blue"))
