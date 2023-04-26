from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import PostSerializer, CategorySerializer, CommentSerializer
from .models import Post, Category, Comments
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]  # настройка фильтров
    filterset_fields = ['category', 'date', 'author']  # настройка фильтров


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSet(ListModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer  # разрешенные методы так же (viewsets.ReadOnlyModelViewSet) только чтение
    permission_classes = (IsAuthenticatedOrReadOnly,)
