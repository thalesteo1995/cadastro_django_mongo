from celery import shared_task
from src.mongo import Mongo

def process_register(form_data):
    name = form_data["name"]
    last_name = form_data["last_name"]
    email = form_data["email"]
    cpf = form_data["cpf"]
    phone_number = form_data["phone_number"]
    age = form_data["age"]
    
    form_data = {
        "name": name, 
        "last_name": last_name, 
        "email": email,
        "cpf": cpf,
        "phone_number": phone_number,
        "age": age
                 }
    return form_data
    
@shared_task
def task_process_register(form_data):
    form_data = process_register(form_data)
    db = Mongo(database="my_database", collection="my_collection")
    db.insert(form_data)
    