from django.urls import path
from .views import SalesOrderListCreateView

urlpatterns = [
    path('sales/', SalesOrderListCreateView.as_view(), name='sales-list'),
]
