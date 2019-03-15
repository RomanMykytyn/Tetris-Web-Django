from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from .models import Comment

# Create your views here.

def index(request):
    if request.method == 'POST':
        userSignUp = authenticate(username=request.POST['login'], password=request.POST['password'])
        if userSignUp is not None:
            login(request, userSignUp)
            return redirect("/", { 'wrongLogin':'' })
        else:
            return render(request, 'index.html', context={'wrongLogin':'Login or password is incorrect.'},)
    if request.method == 'GET':
        return render(request, 'index.html', context={'wrongLogin':''},)

def signIn(request):
    user = User.objects.create_user(request.POST['login'], None, request.POST['password'])
    user.save()
    userSignIn = authenticate(username=request.POST['login'], password=request.POST['password'])
    login(request, userSignIn)
    return redirect('/')


def exitAcc(request):
    logout(request)
    return HttpResponse()

def ajaxView(request):
    if "text" in request.GET:
        newComment = Comment(userName = request.user.username, textOfComment = request.GET['text'])
        newComment.save()
        return HttpResponse()
    if "update" in request.GET:
        all_comments = Comment.objects.all()
        #all_comments.order_by('-userName', '-textOfComment')
        to_page = ""
        for i in all_comments:
            to_page += "<div class='comment'><b>" + i.userName + ":</b> " + i.textOfComment + "</div>"
        return HttpResponse(to_page)

'''def signUp(request):
    userSignUp = authenticate(username=request.POST['login'], password=request.POST['password'])
    if userSignUp is not None:
        login(request, userSignUp)
        return redirect('/')
    else:
        messages.add_message(request, messages.INFO, 'Hello world.')
        return render(
            request,
            'index.html',
            context={},
        )'''
