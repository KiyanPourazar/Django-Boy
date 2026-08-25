from django.shortcuts import render

# Create your views here.
def login(request):
    # if request.user.is_authenticated:
    #     msg = f"user is authenticated as {request.user.username}"
    # else:
    #     msg = f"user is NOT authenticated"

    return render(request, 'accounts/login.html', )

def logout(request):
    return render(request, 'accounts/logout.html')

def signup(request):
    return render(request, 'accounts/signup.html')