# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


from dotenv import load_dotenv

load_dotenv()
data = {
    "from": {
        "email": "ray@raymondjones.dev"
    },
    "personalizations": [
        {
            "to": [
                {
                    "email": "rayjones2170@gmail.com",
                    "name": "Learn in a nutshell"
                }
            ],
            "dynamic_template_data": {
                "name": "Raymond"
            }
        }
    ],
    "template_id": "d-c2c2a6c8a5d2425da166762fbe979d5e"

}
message = Mail(
    from_email='ray@raymondjones.dev',
    to_emails='rayjones2170@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(data)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
