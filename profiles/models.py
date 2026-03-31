from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Profile(models.Model):

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')

    first_name = models.CharField(max_length = 70)
    last_name = models.CharField(max_length = 70)
    email = models.EmailField()
    profile_pic = models.URLField(
        null = True,
        blank = True,
        help_text = "If you wish to add a profile pic for your profile, please add a link above."
    )
    bio = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.first_name + " " + self.last_name

