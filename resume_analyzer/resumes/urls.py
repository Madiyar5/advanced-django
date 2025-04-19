from django.urls import path
from .views import ResumeUploadView, user_resumes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', ResumeUploadView.as_view(), name='upload-resume'),
    path('info/', user_resumes, name='user-resumes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)