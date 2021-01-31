from django.shortcuts import render,redirect

# Create your views here.
from  . models import *



def home(request):
    yo = request.session.get("user","f")
    if yo=="f":
        flag=0
    else:
        flag=1
    return render(request,'home.html',{'flag':flag})



def about(request):
    return render(request,'about.html')

def logout_admin(request):
    del request.session['club']
    return redirect('home')

def logout(request):
    del request.session['user']
    return redirect('home')

def hackathons(request):

    
    if request.session.get("user","f")=="f":
        flag=0
    else:
        flag=1

    context={
    'hackathons':general.objects.all().filter(title_type="hackathon"),
    'flag':flag
    }
    return render(request,'hackathon.html',context)


def college(request):
    if request.session.get("user","f")=="f":
        flag=0
    else:
        flag=1
    context={
    'fests':general.objects.all().filter(title_type="fest"),
    'flag':flag
    }
    return render(request,'college.html',context)

def competition(request):

    if request.session.get("user","f")=="f":
        flag=0
    else:
        flag=1
    context={
    'competitions':general.objects.all().filter(title_type="competition") ,
    'flag':flag
    }
    return render(request,'competition.html',context)

def news(request):
    return render(request,'news.html')

def quizzes(request):

    if request.session.get("user","f")=="f":
        flag=0
    else:
        flag=1
    context={
    'quizes':general.objects.all().filter(title_type="quiz") ,
    'flag':flag
    }
    return render(request,'quizzes.html',context)

def workshops(request):

    if request.session.get("user","f")=="f":
        flag=0
    else:
        flag=1
    context={
    'workshops':general.objects.all().filter(title_type="workshop"),
    'flag':flag
    }
    return render(request,'workshop.html',context)


def blog_detail(request):
    return render(request,'blog-single.html')