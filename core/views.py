from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.conf import settings
from templated_mail.mail import BaseEmailMessage
# Create your views here.


def send_something(request):
    try:
        # message = EmailMessage('subject','something new message', settings.DEFAULT_FROM_EMAIL , ['recepient@gmail.com'])
        # message.attach_file('core/static/images/')
        message = BaseEmailMessage( template_name='email.html', context={'name' : 'davola'} )
        message.send(['james@gmail.com'])
    except BadHeaderError:
        pass
    return render(request, 'index.html', {})