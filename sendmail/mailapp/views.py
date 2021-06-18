

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def home(request):

    return render(request, 'home.html')

def sendmail(request):

    send_mail(
        'Alert',
        'This mail is genetated via django frame work',
        'ravitejakompalli01@gmail.com',
        ['Nithya.kl.Official@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse('Mail successfully sent')
