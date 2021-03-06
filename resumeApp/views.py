from django.core.checks import messages
from django.shortcuts import redirect, render
from resumeApp.models import Contact
from django.contrib import messages
from django.http import HttpResponse

#from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.template import RequestContext
from django.core.mail import send_mail

def index(request):
    
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            Contact.objects.create(
                name = name,
                email = email,
                subject = subject,
                message = message
            ).save()
            #send_mail_after_registration(email)
            messages.success(request, name)
            return redirect('success')
        except:
            return HttpResponse('invalid entry, Try again')
    return render(request, 'resumeApp/index.html')

def success(request):
    
    
    return render(request, 'resumeApp/success.html')

def send_mail_after_registration(email):
    subject = 'Confirmation message'
    message = f'Your message has beesn recieved, thank you. feel free to call me on +234 9052089164'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail(subject, message , email_from ,recipient_list )