from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.management import call_command
from .models import Submission


@receiver(post_save, sender=Submission)
def run_checker(sender, instance, created, **kwargs):
    if created:
        # Call your script here, passing the necessary parameters
        call_command('run_checker', submission_id=instance.id)
