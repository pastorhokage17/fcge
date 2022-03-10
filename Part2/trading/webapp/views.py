from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import User,Stock
from . serializers import UserSerializer, StockSerializer

# Create your views here.

class UserList(APIView):
    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)

    def post(self):
        pass


class StockList(APIView):
    def get(self, request):
        serializer = StockSerializer(Stock.objects.all(), many=True)
        return Response(serializer.data)

    def post(self):
        pass
