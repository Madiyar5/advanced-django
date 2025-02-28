from rest_framework import generics
from .models import SalesOrder
from .serializers import SalesOrderSerializer
from rest_framework.permissions import IsAuthenticated

class SalesOrderListCreateView(generics.ListCreateAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
    permission_classes = [IsAuthenticated]

