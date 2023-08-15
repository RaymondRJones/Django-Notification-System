from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import User, Message
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import User, Message
import os
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, HtmlContent, TemplateId
from dotenv import load_dotenv
import random


def generate_referral_code():
    code = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    return code

load_dotenv()

def load_email_template(template_name):
    with open(template_name, 'r') as file:
        return file.read()

@csrf_exempt  # Note: This disables CSRF protection for the view. In production, a more secure method should be used.
def send_notification_to_one_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        username = request.POST.get('name')
        message_type = request.POST.get('type')

        try:
            if user_id:
                user = User.objects.get(pk=user_id)
            elif username:
                user = User.objects.get(name=username)
            else:
                return JsonResponse({'status': 'error', 'message': 'Please provide a user_id or username'})
            print("Gets the name")

            message = Message.objects.filter(type=message_type).first()
            if not message:
                return JsonResponse({'status': 'error', 'message': 'Message not found'})
            
            print("Gets the message")


            msg = "<strong> " + message.content + "</strong>"
            template_path = '/Users/raymondjones/Documents/GitHub/Django-Notification-System/notification_system/notifications_app/email_template_1.html'

            email_content = load_email_template(template_path)

            message_to_send = Mail(
                from_email='ray@raymondjones.dev',
                to_emails=user.email,
                subject='Part 3 - Sending with Twilio SendGrid is Fun',
                html_content=email_content)
            # print(os.environ.get('SENDGRID_API_KEY'))


            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

            # Here
            response = sg.send(message_to_send)
            print("Response", response)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            message.is_sent = True
            message.save()

            return JsonResponse({'status': 'success', 'message': 'Notification sent'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Only POST method is allowed'})

@csrf_exempt
def create_new_user(request):
    if request.method == 'POST':
        # Extract data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        # Validate the data (you can add more validations if needed)
        if not name or not email:
            return JsonResponse({'status': 'error', 'message': 'Name and Email are required fields.'})

        # Create the new user
        try:
            while True:  # Normally really bad code but it's okay for 100 users, like a .01% collision chance
                referral_code = generate_referral_code()
                if not User.objects.filter(referral_code=referral_code).exists():
                    break
            user = User(name=name, email=email, phone_number=phone_number, referral_code= referral_code)
            user.save()
            return JsonResponse({'status': 'success', 'message': 'User created successfully.'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Only POST method is allowed.'})
