from rest_framework import serializers

from .models import Post, Category, Comments


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'category', 'title', 'description', 'author', 'date', 'img')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('post', 'id', 'description', 'author')


