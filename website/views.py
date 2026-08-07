from django.http import HttpResponse,JsonResponse

def index_home(request):
    return HttpResponse('<h1>main</h1>')

def index_about(request):
    return HttpResponse('<h1>about</h1>')

def index_contact(request):
    return HttpResponse('<h1>cantact</h1>')
