from django.db import models
from django.core.exceptions import ValidationError

def validate_letters_and_spaces(value):
    if not value.replace(' ', '').isalpha():
        raise ValidationError('A true Witcher knows that beast names cannot contain numbers or symbols!')


class BeastsGroup(models.Model):
    group_name = models.CharField(max_length = 60)
    def __str__(self):
        return self.group_name

class HowToWin(models.Model):
    item_name = models.CharField(max_length = 130)
    def __str__(self):
        return self.item_name

class Monster(models.Model):
    DANGER_CHOICES = ((1, 'Easy'), (2, 'Normal'), (3, 'High'), (4, 'Extreme'))
    monster_name = models.CharField(max_length = 100, validators=[validate_letters_and_spaces])
    my_notes = models.TextField()
    level_of_danger = models.PositiveIntegerField(choices = DANGER_CHOICES)
    image_url = models.URLField(blank = True, null =True)
    kind = models.ForeignKey(BeastsGroup, on_delete = models.CASCADE)
    what_to_use = models.ManyToManyField(HowToWin)

    def __str__(self):
        return self.monster_name