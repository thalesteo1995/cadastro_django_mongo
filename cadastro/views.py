from django.shortcuts import render
from .models import Register
from .tasks import process_register

def cadastro(request):
    register = Register(request.POST)

    form_data = {
        "name": register["name"].value(),
        "last_name": register["last_name"].value(),
        "email": register["email"].value(),
        "cpf": register["cpf"].value(),
        "phone_number": register["phone_number"].value(),
        "age": register["age"].value(),
    }
    valores_vazios = all(not valor for valor in form_data.values())
    if valores_vazios:
        return render(request, 'cadastro.html',  {'register': register})
    process_register(form_data=form_data)
    return render(request, 'cadastro.html',  {'register': register})