from celery import shared_task

def process_register(form_data):
    name = form_data["name"]
    last_name = form_data["last_name"]
    email = form_data["email"]
    cpf = form_data["cpf"]
    phone_number = form_data["phone_number"]
    age = form_data["age"]
    
@shared_task
def task_process_register(form_data):
    process_register(form_data)
    