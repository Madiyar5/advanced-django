from django.urls import path
from .views import  create_cv, cv_list, share_cv_email
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',create_cv ),
    path('create_cv', create_cv, name='create_cv'),
    path('cv_list', cv_list, name='cv_list'),
    path('share/email/<int:cv_id>/', share_cv_email, name='share_cv_email'),
    path('share/email/<int:cv_id>/', share_cv_email, name='share_cv_email'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
