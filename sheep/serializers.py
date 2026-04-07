from rest_framework import serializers
from .models import Sheep

class SheepSerializer(serializers.ModelSerializer):
    age_months_calculated = serializers.SerializerMethodField()

    class Meta:
        model = Sheep
        fields = "__all__"

    def get_age_months_calculated(self, obj):
        return obj.get_age_months()