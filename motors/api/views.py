from motors.models import Motor
from motors.api.serializer import MotorSerializer
from rest_framework import serializers

class MotorViewSet(serializers.ModelSerializer):
    query = Motor.objects.all()
    serializer_class = MotorSerializer

    def get_queryset(self):
        return self.query

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

