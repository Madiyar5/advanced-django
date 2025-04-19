from django.db import models
from django.conf import settings
# Create your models here.
class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    #AI based
    skills = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    recommendations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.file.name}"