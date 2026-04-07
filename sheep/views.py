from rest_framework import viewsets
from .models import Sheep
from .serializers import SheepSerializer

class SheepViewSet(viewsets.ModelViewSet):
    queryset = Sheep.objects.all()
    serializer_class = SheepSerializer
