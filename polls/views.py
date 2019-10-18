from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import Posts


def index(request):
    return render(request, "index.html")

def signup(request):

    if  request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                print('Username taken')
            elif User.objects.filter(email=email).exists():
                print ('Email taken')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save();
                print('user created successfully!!!')

        else:
            print('Password not matching!!!')

    else:
         return render(request, "signup.html")

def editProfile(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']

        user = User.objects.filter(id=userId).update(first_name=first_name,last_name=last_name,username=username,email=email)
        user.save();
        print ('user updated successfully!!!')

def deleteUser(request):

    if request.method == 'DELETE':

        userId = request.POST['userId']
        user = User.objects.get(id=userId)
        user.delete()
        print('user deleted successfully!!!')
    else:
        print('Bad Request!!!')

             

def post(request):
    posts  = Posts.objects.all() 
    return render(request, "post.html",{'posts':posts})    