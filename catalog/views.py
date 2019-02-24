from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
        context={},
    )

def signIn(request):
    user = User.objects.create_user(request.POST['login'], None, request.POST['password'])
    user.save()
    userSignIn = authenticate(username=request.POST['login'], password=request.POST['password'])
    login(request, userSignIn)
    return render(
        request,
        'index.html',
        context={},
    )
