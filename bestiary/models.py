from django.db import models

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
    monster_name = models.CharField(max_length = 100)
    my_notes = models.TextField()
    level_of_danger = models.PositiveIntegerField(choices = DANGER_CHOICES)
    image_url = models.URLField(blank = True, null =True)
    kind = models.ForeignKey(BeastsGroup, on_delete = models.CASCADE)
    what_to_use = models.ManyToManyField(HowToWin)

    def __str__(self):
        return self.monster_name