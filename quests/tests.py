from django.test import TestCase
from django.urls import reverse

# from django.urls import reverse
from quests.models import Quest
from profiles.models import Profile
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class QuestModelTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username = 'vesemir', password = 'password123')
        self.profile = Profile.objects.get(user = self.user)
        self.profile.first_name = "Vesemir"
        self.profile.save()

    def test_quest_str_method(self):
        # tests quest string
        quest = Quest.objects.create(title = "The Beast of White Orchard", description = "Kill the Griffin", profile = self.profile)
        self.assertEqual(str(quest), "The Beast of White Orchard")

    def test_quest_default_is_completed_is_false(self):
        # tests the boolean value
        quest = Quest.objects.create(title = "Devil by the Well", description = "Noonwraith", profile = self.profile)
        self.assertFalse(quest.is_completed)

class QuestViewTests(TestCase):
    def test_quest_create_redirects_anonymous_user(self):
        url = reverse('quest_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)