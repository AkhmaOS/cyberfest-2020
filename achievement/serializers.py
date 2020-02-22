from rest_framework import serializers

from .models import AchievementModel


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementModel
        fields = '__all__'
