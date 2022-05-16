from rest_framework.decorators import api_view
from rest_framework.response import Response

from spending.serializer import SpendingSerializer
from .models import Spending


@api_view(['GET'])
def spending_list(request, ordering, format=None):
    if request.GET.get('filtering') == 'USD' or request.GET.get('filtering') == 'HUF':
        spendings = Spending.objects.order_by(ordering).filter(currency=request.GET.get('filtering'))
        serializer = SpendingSerializer(spendings, many=True)
    else:
        spendings = Spending.objects.order_by(ordering)
        serializer = SpendingSerializer(spendings, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_spending(request, format=None):
    serializer = SpendingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
