from rest_framework import generics
from .models import AnalyticsReport
from .serializers import AnalyticsReportSerializer
from rest_framework.permissions import IsAuthenticated

class AnalyticsReportListView(generics.ListAPIView):
    queryset = AnalyticsReport.objects.all()
    serializer_class = AnalyticsReportSerializer
    permission_classes = [IsAuthenticated]
