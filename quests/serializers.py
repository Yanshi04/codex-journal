from rest_framework import serializers
from .models import Quest
from bestiary.serializers import MonsterSerializer

class QuestSerializer(serializers.ModelSerializer):
    monsters = MonsterSerializer(many = True, read_only = True)

    class Meta:
        model = Quest
        fields = '__all__'
        read_only_fields = ['profile']