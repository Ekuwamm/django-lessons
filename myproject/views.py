from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html' )

def contact(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        full_message = f'Message from {username} <{email}>:\n\n{message}'

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            ['mosekuwam@gmail.com','mosekuwam@yahoo.com'],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been successfully send')
    return render(request,'contact.html' )