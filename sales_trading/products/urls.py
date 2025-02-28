from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductListCreateView, CategoryViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'category', CategoryViewSet)  # Теперь `/category/`

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('', include(router.urls)),  # Подключаем ViewSet
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)