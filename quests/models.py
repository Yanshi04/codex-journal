from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Quest(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    is_completed = models.BooleanField(default = False)

    profile = models.ForeignKey(UserModel, on_delete = models.CASCADE, related_name = 'quests')
    monsters = models.ManyToManyField('bestiary.Monster', blank = True)

    def __str__(self): return self.title

