from rest_framework import serializers
from blog.models import Comment, Post, LANGUAGE_CHOICES


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'username', 'comment_text', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True, read_only=True) # 1대 N의 관계
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'date', 'body', 'language', 'comments']
        