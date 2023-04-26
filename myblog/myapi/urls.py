from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'blog', views.PostViewSet)
router.register(r'cat', views.CategoryViewSet)
router.register(r'comm', views.CommentViewSet)


urlpatterns = router.urls
