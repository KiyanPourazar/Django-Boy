from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

def index_home(request):
    return render(request, 'website/index.html')

def index_about(request):
    return render(request, 'website/about.html')

def index_contact(request):
    return render(request, 'website/contact.html')

def test_view(request):
    context = {'name':'Kiyan','lastname':'Pourazar'}
    return render(request, 'website/test.html', context)

def elements_view(request):
    return render(request, 'website/elements.html')