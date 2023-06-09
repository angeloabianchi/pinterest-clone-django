from django.shortcuts import render
from datetime import datetime

def index(request):
    response = render(request, 'home/index.html')
    return response
