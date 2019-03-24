from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from .models import Comment, userScore

# Create your views here.

def index(request):
    if request.method == 'POST':
        userSignUp = authenticate(username=request.POST['login'], password=request.POST['password'])
        if userSignUp is not None:
            login(request, userSignUp)
            return redirect("/", { 'wrongLogin':'' })
        else:
            return render(request, 'index.html', context={'wrongLogin':'Login or password is incorrect.'},)
    if request.method == 'GET' and request.session.get('busyLogin', False) == True:
        request.session['busyLogin'] = False
        return render(request, 'index.html', context={'wrongLogin':'This username is busy.'},)
    if request.method == 'GET':
        return render(request, 'index.html', context={'wrongLogin':''},)

def signIn(request):
    if User.objects.filter(username=request.POST['login']).exists():
        request.session['busyLogin'] = True
        return redirect("/")
    user = User.objects.create_user(request.POST['login'], None, request.POST['password'])
    user.save()
    newUserScore = userScore(userName = request.POST['login'], score = '')
    newUserScore.save()
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
    if "updateComments" in request.GET:
        all_comments = Comment.objects.all()
        to_page = ""
        for i in all_comments[::-1]:
            to_page += "<div class='comment'><b>" + i.userName + ":</b> " + i.textOfComment + "</div>"
        return HttpResponse(to_page)
    if "updatePlayers" in request.GET:
        all_players = userScore.objects.all()
        best_players = []
        to_page = ""
        for i in all_players:
            temp = i.score.split()
            for j, item in enumerate(temp):
                temp[j] = int(item)
            temp = sum(temp)
            best_players.append([i.userName, temp])
        sorted(best_players, key=lambda x: x[1])
        best_players[0:9]
        for n in best_players:
            to_page += "<li>" + n[0] +" - " + str(n[1]) + "</li>"
        to_page = "<ol>" + to_page + "</ol>"
        return HttpResponse(to_page)
    if "score" in request.GET:
        if request.user.is_authenticated == True:
            newUser = userScore.objects.get(userName = request.user.username)
            newUserScore = newUser.score.split()
            newUserScore.insert(0, request.GET['score'])
            newUser.score = " ".join(newUserScore)
            newUser.save()
        return HttpResponse()

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
