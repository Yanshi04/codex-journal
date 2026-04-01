from django.test import TestCase
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CustomUserTests(TestCase):
    def test_create_custom_user(self):
        # verifies that custom user
        user = UserModel.objects.create_user(username = 'yennefer', email = 'yen@vengerberg.com', password = 'magic')
        self.assertEqual(user.username, 'yennefer')
        self.assertTrue(user.is_active)