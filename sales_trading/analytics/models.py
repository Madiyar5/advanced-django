from django.db import models

class AnalyticsReport(models.Model):
    report_type = models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)
