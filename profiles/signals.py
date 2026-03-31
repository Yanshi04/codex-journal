from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def auto_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user = instance,
            first_name = instance.first_name or instance.username,
            # this here is just a placeholder, since the og Geralt is 'of rivia'
            last_name = instance.last_name or "of Rivia",
            email = instance.email
        )

