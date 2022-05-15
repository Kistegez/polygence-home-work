from rest_framework import serializers
from spending.models import Spending

class SpendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spending
        fields = '__all__'
