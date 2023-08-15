from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User  # or wherever your User model is located
import os
from sendgrid import SendGridAPIClient

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    print("Checking if user was created...")
    if created:  # checks if the instance was just created
        print("User was created! Sending email...")
        send_email(instance)

def send_email(user):
    data = {
        "from": {
            "email": os.environ.get('SENDGRID_EMAIL')
        },
        "personalizations": [
            {
                "to": [
                    {
                        "email": user.email,
                        "name": user.name
                    }
                ],
                "dynamic_template_data": {
                    "name": user.name,
                    "referral": user.referral_code
                }
            }
        ],
        "template_id": "d-c2c2a6c8a5d2425da166762fbe979d5e"
    }

    try:
        print("Sending template data")
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(data)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
