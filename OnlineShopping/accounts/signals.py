import stripe
from django.db import models
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django,contrib.auth import get_user_model
from .models import UserStripe

stripe.api_key = settings.STIPE_SECRET_KEY
User=get_user_model()


def get_or_create_stripe(user):
    new_user_stripe,created=UserStripe.objects.get_or_create(user=user)
    if created:
        customer= stripe.Customer.create(
            email=str(user.email)
        )
        new_user_stripe.stripe_id=customer.id
        new_user_stripe.save()
# user_logged_in.connect(get_or_create_stripe)


def user_saved_signal(sender,instance,created,*args,**kwargs):
    user=instance
    if created:
        get_or_create_stripe(user)


post_save.connect(user_saved_signal,sender=User)
