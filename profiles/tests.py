from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class ProfileModelTests(TestCase):
    def test_profile_str_method(self):
        # tests the concatenation in the Profile string method
        user = UserModel.objects.create_user(username = 'ciri', password = 'password123')
        profile = Profile.objects.get(user = user)
        profile.first_name = "Cirilla"
        profile.last_name = "Fiona"
        profile.save()
        self.assertEqual(str(profile), "Cirilla Fiona")