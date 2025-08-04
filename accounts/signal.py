from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

        # Send Welcome Email
    send_mail(
        subject ='Welcome to Our Site',
        message = 'Hi ' + instance.username + ', Thank you for registering.',
        from_email = 'noreply@localhost.com',
        recipient_list = [instance.email],
        fail_silently = True,
    )

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()



