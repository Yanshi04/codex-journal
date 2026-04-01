from django.test import TestCase
from armory.models import Weapon
from profiles.models import Profile
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class ArmoryModelTests(TestCase):
    # signal creates the profile automatically
    def setUp(self):
        self.user = UserModel.objects.create_user(username = 'geralt', password = 'password123')
        self.profile = Profile.objects.get(user = self.user)
        self.profile.first_name = "Geralt"
        self.profile.last_name = "of Rivia"
        self.profile.save()

    def test_weapon_str_method(self):
        # tests weapon string
        weapon = Weapon.objects.create(name = "Aerondight", damage = 100, owner = self.profile)
        self.assertEqual(str(weapon), "Aerondight")

    def test_weapon_default_description_is_blank(self):
        # tests if the description defaults to blank correctly
        weapon = Weapon.objects.create(name = "Steel Sword", damage = 50, owner = self.profile)
        self.assertEqual(weapon.description, "")