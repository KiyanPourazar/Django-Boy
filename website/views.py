from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

def index_home(request):
    return render(request, 'index.html')

def index_about(request):
    return render(request, 'about.html')

def index_contact(request):
    return render(request, 'contacts.html')
