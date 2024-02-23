from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError


def say_hello(request):
    try:
        mail_admins('subject', 'message', html_message='message')
        send_mail('subject', 'message', 'info@thesarfo.com', ['elisahines76@gmail.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Ernest'})
