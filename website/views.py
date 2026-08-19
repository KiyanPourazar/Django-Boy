from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsletterForm

def index_home(request):
    return render(request, 'website/index.html')

def index_about(request):
    return render(request, 'website/about.html')

def index_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent.")
        else:
            messages.error(request, "Your message hasn't been sent.")
    form = ContactForm()

    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your email has been saved.")
        else:
            messages.error(request, "Your email hasn't been saved.")

    return redirect(request.META.get('HTTP_REFERER', '/'))

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
