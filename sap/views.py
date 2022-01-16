
from django.shortcuts import render, redirect
# from .forms import SubscribeForm

from django.core.mail import send_mail
from django.conf import settings
from . models import Users 

def home(request):
    if 'username' in request.session:
        info_details=Users.objects.all()
        return render(request, 'home.html',{'details':info_details})
    return redirect('login')

def signup(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        details=Users(Name=name, Password=password)
        details.save()
        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        dataexist=Users.objects.filter(Name=name, Password=password).exists()
        if dataexist:
            request.session['username']=name
            return redirect('home')
    return render(request, 'login.html')


def logout(request):
    request.session.flush()
    return redirect('login')


def index(request):

    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject, message, settings.EMAIL_HOST_USER,
                  [email], fail_silently=False)
        return render(request, 'success.html', {'email': email})
    return render(request, 'index.html')
    #     form = SubscribeForm(request.POST)
    #     if form.is_valid():
    #         subject = 'Code Band'
    #         message = 'Sending Email through Gmail'
    #         recipient = form.cleaned_data.get('email')
    #         send_mail(subject, 
    #           message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
    #         #messages.SUCCESS(request, 'Profile details updated.')
    #         return redirect('subscribe')
    # return render(request, 'index.html')
    
