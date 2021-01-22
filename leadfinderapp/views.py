from django.shortcuts import render
from .scrapper import EmailCrawler
from django.http import HttpResponse
from celery import shared_task
from multiprocessing import Process
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from asgiref.sync import sync_to_async
from django.shortcuts import redirect
from .forms import CreateUserForm
from rest_framework.decorators import APIView
from rest_framework.response import Response
from leadfinderapp import serializers
from django.contrib import messages
import asyncio
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *

@login_required(login_url='login')
def index(request):
    profileimage = User.objects.all()
    context = {'profileimage':profileimage}
    return render(request, 'leadfinderapp/dashboard.html', context)

@login_required(login_url='login')
def emailsearcher(request):
    return render(request, 'leadfinderapp/emailsearcher.html')

def example(request):
    return render(request, 'leadfinderapp/example.html')

@login_required(login_url='login')
def scrap(request):
    url = request.GET.get('Email')
    crawl = EmailCrawler(url)
    target = crawl.crawl()
    email_list = crawl.emails # or whatever class-level variable you use
    return render(request, 'leadfinderapp/emailsearcher.html', {"email_list": email_list})

def userlogin(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
    return render(request, 'leadfinderapp/login.html', context)

def register(request):

    if request.user.is_authenticated:
        return redirect('login')
    else:

        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was created succesfully')
                return redirect('login')

    context = {'form':form}

    return render(request, 'leadfinderapp/register.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def lostPassword(request):
    context = {}
    return render(request, 'leadfinderapp/forgot-password.html', context)


def imageprofile(request):
    userimage = UserProfile.objects.all()
    context = {'userimage': userimage}

    return render(request, 'leadfinderapp/dashboard.html', context)




class apiOverview(APIView):
    serializer_class = serializers.EmailsSerializer


    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            url = serializer.validated_data.get('url')
            message = f'The url is {url}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})
