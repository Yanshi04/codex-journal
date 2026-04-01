from django.db import models
from profiles.models import Profile

class Weapon(models.Model):
    name = models.CharField(max_length = 100)
    damage = models.PositiveIntegerField()
    description = models.TextField(blank = True)
    owner = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name ='weapons')

    def __str__(self):
        return self.name