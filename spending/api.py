from spending.models import Spending
from rest_framework import viewsets, permissions
from .serializer import SpendingSerializers

class SpendingViewSet(viewsets.ModelViewSet):
    queryset = Spending.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SpendingSerializers