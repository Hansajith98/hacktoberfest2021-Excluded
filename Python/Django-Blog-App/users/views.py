from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('blog') 

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not Exists')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog')
        else:
            messages.error(request, 'Username or Password does not match')


    context = {}
    return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request)
    messages.error(request, 'User was logged Out')
    return redirect('login')


def userProfile(request):
    users = Profile.objects.all()
    
    context = {'users': users}
    return render(request, 'users/profile.html', context)
