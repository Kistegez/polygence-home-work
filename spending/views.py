from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from spending.serializer import SpendingSerializer
from .models import Spending


@api_view(['GET', 'POST'])
def spending_list(request, format=None):
    if request.method == 'GET':
        spendings = Spending.objects.all()
        serializer = SpendingSerializer(spendings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SpendingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def spending_list_filter(request, filter, format=None):
    try:
        spending = Spending.objects.get(currency=filter)
    except Spending.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SpendingSerializer(spending)
    return Response(serializer.data)