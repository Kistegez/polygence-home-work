from rest_framework import serializers
from spending.models import Spending

class SpendingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Spending
        fields = '__all__'
