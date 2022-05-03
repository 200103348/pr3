from typing import OrderedDict
from xmlrpc.client import MAXINT
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.decorators.csrf import *
from .forms import *


from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from django.core.mail import EmailMessage
from django.conf import settings


from django.contrib.auth.forms import UserCreationForm

# Create your views here.


    


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm']
        form = Logreg(request.POST)
        email_subject = 'Activate your account'
        email_body = render_to_string('activate.html')
        emaill=EmailMessage(subject=email_subject, body=email_body, from_email='200103348@stu.sdu.edu.kz', to=[email])
        if password1 == password2:
            if regis.objects.filter(username = username).exists():
                print('Username are already used')
                return redirect('/register/')
            elif regis.objects.filter(email = email).exists():
                print('Email invalid')
                return redirect('/register/')
            else:
                form.save()
                print('user created')
                emaill.send()        
        else:
            print('password not matching...')
            return redirect('/register/')
        return redirect('/register/')
    else:
        return render(request, 'register.html')


def reg(request):
    return render(request, 'register.html')

def user(request):
    s = regis.objects.last()
    return render(request, 'user.html', {'s':s})


def send_message(request):
    '''send_mail(
        'Hello',
        'Body goes here',
        '200103348@stu.sdu.edu.kz',
        ['200103348@stu.sdu.edu.kz'],
        fail_silently = False, html_message = "tur zhata bermei"
    )
    return render(request, 'successfull.html')'''

    email = EmailMessage(
        'Hello',
        'Body goes here',
        '200103348@stu.sdu.edu.kz',
        ['200103348@stu.sdu.edu.kz'],
        headers={'Message-ID':'foo'},
    )
    email.attach_file('C:/Users/Hp/Pictures/11.png')
    email.send(fail_silently=False)
    return render(request, 'successfull.html')


def loginPage(request):
    context = {}
    return render(request, 'login.html', context)

def regPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        
    context = {'form': form}
    return render(request, 'reg.html', context)