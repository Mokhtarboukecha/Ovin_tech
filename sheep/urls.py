from rest_framework.routers import DefaultRouter
from .views import SheepViewSet

router = DefaultRouter()
router.register(r'sheep', SheepViewSet)

urlpatterns = router.urls