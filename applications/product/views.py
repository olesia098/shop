from django.shortcuts import render

# Create your views here.
from rest_framework import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from applications.product.models import *


class ListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DeleteUdateRetriveView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer