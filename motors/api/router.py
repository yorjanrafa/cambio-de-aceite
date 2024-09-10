from rest_framework.routers import DefaultRouter

from motors.api.views import MotorViewSet

router = DefaultRouter()
router.register(prefix='motors', basename='motors', viewset=MotorViewSet)