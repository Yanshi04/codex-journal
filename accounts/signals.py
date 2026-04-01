from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def assign_master_witcher_group(sender, instance, created, **kwargs):
    # Automatically assigns every new user to the 'Master Witcher' group so they have full CRUD permissions immediately.
    if created:
        try:
            master_group = Group.objects.get(name='Master Witcher')
            instance.groups.add(master_group)
        except Group.DoesNotExist:
            pass