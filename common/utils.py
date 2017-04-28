from django.core.mail import send_mail

from emerald.constants import ADMIN_EMAIL

def mail_to_admin(subject, message):
    send_mail(
        subject,
        message,
        'mailer@emeraldgov.com',
        [ADMIN_EMAIL],
        fail_silently=False
    )
