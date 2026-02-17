from django.contrib import admin
from .models import BeastsGroup, HowToWin, Monster

@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    list_display = ('monster_name', 'level_of_danger', 'kind')
    list_filter = ('kind',)
    search_fields = ('monster_name',)

admin.site.register(BeastsGroup)
admin.site.register(HowToWin)