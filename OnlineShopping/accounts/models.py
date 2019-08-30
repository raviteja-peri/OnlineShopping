import stripe
from django.db import models
from django.contrib.auth.signals import user_logged_in
from django.conf import settings

# Create your models here.
stripe.api_key = settings.STIPE_SECRET_KEY


class UserStripe(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    stripe_id=models.CharField(max_length=120)

    def __str__(self):
        return self.stripe_id
