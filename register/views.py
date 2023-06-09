from django.shortcuts import render

def index(request):
    response = render(request, 'register/index.html')
    return response
