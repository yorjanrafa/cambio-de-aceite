from rest_framework import serializers

from .models import Motors

class MotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motors
        fields = '__all__'
