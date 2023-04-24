from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'blog', views.PostViewSet)
router.register(r'cat', views.CategoryViewSet)
router.register(r'comm', views.CommentViewSet)

Spectacular = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
urlpatterns = router.urls + Spectacular
