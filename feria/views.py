from django.shortcuts import render
# from .models import VentLocal, VentExtran

# # Create your views here.

# def index(request):
#     return render(request, 'index.html')

# def login(request):
#     return render(request, 'registration/login.html')

# #Formato del Listar
# def listarVentLocal(request):
#     #Accediendo al objeto que contiene los datos en la base de datos
#     #con el .all() se traen todos los objetos que esten en la tabla
#     ventas = VentLocal.objects.all()
#     # con esta variable 'ventas' se le pasa los datos al template
#     datos = {
#         'ventas': ventas
#     }

#     #ahora hay que retornar todo para que lo envie al template
#     return render(request, 'ventas/listarVentaLocal.html', datos)