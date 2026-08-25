from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')

        return render(request, 'accounts/login.html')
    else:
        return redirect('/')

@login_required(login_url='/accounts/login')
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    return render(request, 'accounts/signup.html')