from django.shortcuts import render

def index(request):
    response = render(request, 'login/index.html')
    return response
