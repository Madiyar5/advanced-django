from django.urls import path
from .views import AnalyticsReportListView

urlpatterns = [
    path('analytics/', AnalyticsReportListView.as_view(), name='sales-list'),
]
