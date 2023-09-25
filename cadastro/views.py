from django.shortcuts import render
from .models import Register
from .tasks import task_process_register

def cadastro(request):
    register = Register(request.POST)

    form_data = {
        "name": register["name"].value(),
        "last_name": register["last_name"].value(),
        "email": register["email"].value(),
        "cpf": register["cpf"].value(),
        "phone_number": register["phone_number"].value(),
        "age": register["age"].value(),
        "gender": register["gender"].value(),
    }
    
    print(form_data)    
    task_process_register.delay(form_data=form_data)
    return render(request, 'cadastro.html',  {'register': register})