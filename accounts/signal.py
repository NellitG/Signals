from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import pre_delete
from django.db.models.signals import post_delete
from django.db.models.signals import pre_save

@receiver(pre_save, sender=User)
def pre_save_user_profile(sender, instance, **kwargs):
    print(f"Preparing to save user profile for {instance.username}.")
    instance.userprofile.save()


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

@receiver(pre_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    print (f"Good Bye {instance.username}!! We are deleting your account.")
    instance.userprofile.delete()

@receiver(post_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    print(f"Account for {instance.username} has been deleted.")
    
    send_mail(
        subject='Account Deletion Confirmation',
        message=f'Hi {instance.username}, your account has been successfully deleted.',
    ) 

