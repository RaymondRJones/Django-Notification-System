from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    group = models.CharField(max_length=50)  # Assuming group as a char field, could be a ForeignKey if it's another model.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_sent = models.BooleanField(default=False)
    send_after = models.DateTimeField()
    TYPE_CHOICES = (
        ('TYPE1', 'Type 1'),
        ('TYPE2', 'Type 2'),
        # Add other types as needed
    )
    type = models.CharField(max_length=5, choices=TYPE_CHOICES)
