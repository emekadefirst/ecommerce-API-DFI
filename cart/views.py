from rest_framework import status
from rest_framework import viewsets
from .models import CartItem, Cart
from rest_framework.response import Response
from django.http import Http404
from .serializers import *


class CartItemView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing cartitem instances.
    """
    serializer_class = CreateCartItemSerializer
    queryset = CartItem.objects.all()
