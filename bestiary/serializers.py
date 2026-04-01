from rest_framework import serializers
from .models import Monster, BeastsGroup, HowToWin

class BeastsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeastsGroup
        fields = '__all__'

class HowToWinSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowToWin
        fields = '__all__'

class MonsterSerializer(serializers.ModelSerializer):
    kind = BeastsGroupSerializer(read_only = True)
    what_to_use = HowToWinSerializer(many = True, read_only = True)

    class Meta:
        model = Monster
        fields = '__all__'
        read_only_fields = ['hunter']