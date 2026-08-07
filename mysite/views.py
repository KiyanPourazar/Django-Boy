from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse('<1>helloooooooo</1>')

def json_test(request):
    return JsonResponse({'king':'boy'})