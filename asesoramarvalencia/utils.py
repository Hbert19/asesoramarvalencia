from django.core.mail import send_mail
from . import settings
from threading import Thread
import logging

class SendEmail():

    def __init__(self, request, subject=str, html_message=str, recipient_list=list):
        self.request = request
        self.subject = subject
        self.html_message = html_message
        self.recipient_list = recipient_list
        self.threading = Thread(target=send_email, args=(self.request, self.subject, self.html_message, self.recipient_list))

    def send(self):
        self.threading.start()
        return True

def send_email(request, subject, html_message, recipient_list):
    send_mail(subject=subject, message="", html_message=html_message, from_email= '{} <{}>'.format(subject, settings.EMAIL_HOST_USER), recipient_list= recipient_list, fail_silently=False)
    logging.info('The message {} has sent sucessfully'.format(subject))
