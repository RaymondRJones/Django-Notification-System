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
from dotenv import load_dotenv
load_dotenv()
@csrf_exempt  # Note: This disables CSRF protection for the view. In production, a more secure method should be used.
def send_notification(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        username = request.POST.get('username')
        message_type = request.POST.get('type')

        try:
            if user_id:
                user = User.objects.get(pk=user_id)
            elif username:
                user = User.objects.get(name=username)
            else:
                return JsonResponse({'status': 'error', 'message': 'Please provide a user_id or username'})

            message = Message.objects.filter(user=user, type=message_type).first()

            if not message:
                return JsonResponse({'status': 'error', 'message': 'Message not found'})
            message = Mail(
                from_email='ray@raymondjones.dev',
                to_emails='rayjones2170@gmail.com',
                subject='Part 2 - Sending with Twilio SendGrid is Fun',
                html_content='<strong>and easy to do anywhere, even with Python</strong>')
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message, fail_silently=False)
            print("Response", response)
            message.is_sent = True
            message.save()

            return JsonResponse({'status': 'success', 'message': 'Notification sent'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Only POST method is allowed'})




"""
@csrf_exempt  # Note: This disables CSRF protection for the view. In production, a more secure method should be used.
def send_notification_api(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        message_type = request.POST.get('type')

        try:
            if username:
                user = User.objects.get(name=username)
            else:
                return JsonResponse({'status': 'error', 'message': 'Please provide a user_id or username'})

            message = Message.objects.filter(type=message_type).first()

            if not message:
                return JsonResponse({'status': 'error', 'message': 'Message not found'})

            message = Mail(
                    from_email='sender@example.com',
                    to_emails=user.email,
                    subject='Notification',
                    plain_text_content=message.content)
            try:
                sg = SendGridAPIClient('YOUR_SENDGRID_API_KEY')  # Again, consider securely managing this API key.
                response = sg.send(message)
                # Check the response, etc. (not shown here)
                return JsonResponse({'status': 'success', 'message': 'Notification sent'})

            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Only POST method is allowed'})


"""

