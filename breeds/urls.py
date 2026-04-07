from rest_framework.routers import DefaultRouter
from .views import BreedViewSet

router = DefaultRouter()
router.register(r'breeds', BreedViewSet)

urlpatterns = router.urls