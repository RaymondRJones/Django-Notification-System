# Django-Notification-System

Project to practice some system design concepts like message queues and also build a useful tool that people pay like $600/year and up to $5000/year depending on the scale

# TO-DO

1. Deploy the app on Heroku (Likely need to ask for database payment)
I prefer Heroku over AWS for not needing to learn how to use HTTPS on AWS
3. Daily check if a user was created with another user's referal code and send an email if so?
4. Add a way for client to see their loyalty points
  4.1. text their points occasionally to remind them and allow them to unsubscribe
5. Remove hard coding for email templates and allow more customization via database
    Allow admin to use no code to create their email templates and schedule emails
    Or maybe they'll just go to SendGrid directly?
6. Celery for Workers Queue