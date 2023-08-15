from django.db import models

class User(models.Model):
    class Meta:
        app_label = 'notifications_app'
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    referral_code = models.CharField(max_length=5, unique=True, blank=True, null=True)
    loyalty_points = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=50)  # Assuming group as a char field, could be a ForeignKey if it's another model.
    def __str__(self):
        return self.name
class Message(models.Model):
    class Meta:
        app_label = 'notifications_app'
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
    def __str__(self):
        return f"Message for user {self.user.name}"
