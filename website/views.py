from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from website.models import Contact

def index_home(request):
    return render(request, 'website/index.html')

def index_about(request):
    return render(request, 'website/about.html')

def index_contact(request):
    return render(request, 'website/contact.html')

def test_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()



    return render(request, 'website/test.html', {})

def elements_view(request):
    return render(request, 'website/elements.html')