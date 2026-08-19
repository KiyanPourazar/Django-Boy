from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from website.models import Contact
from website.forms import NameForm, ContactForm

def index_home(request):
    return render(request, 'website/index.html')

def index_about(request):
    return render(request, 'website/about.html')

def index_contact(request):
    return render(request, 'website/contact.html')

def test_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # subject = form.cleaned_data['subject']
            # message = form.cleaned_data['message']
            #
            # print(name, subject, message, email)
            # contact = Contact(name=name, subject=subject, message=message, email=email)
            # contact.save()
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')

    form = ContactForm()

    return render(request, 'website/test.html', {'form': form})

def elements_view(request):
    return render(request, 'website/elements.html')