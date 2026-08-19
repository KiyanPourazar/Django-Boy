from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from website.models import Contact
from website.forms import NameForm

def index_home(request):
    return render(request, 'website/index.html')

def index_about(request):
    return render(request, 'website/about.html')

def index_contact(request):
    return render(request, 'website/contact.html')

def test_view(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Name']
            subject = form.cleaned_data['Subject']
            message = form.cleaned_data['Message']
            email = form.cleaned_data['Email']
            print(name)
            print(subject)
            print(message)
            print(email)
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')

    form = NameForm()

    return render(request, 'website/test.html', {'form': form})

def elements_view(request):
    return render(request, 'website/elements.html')