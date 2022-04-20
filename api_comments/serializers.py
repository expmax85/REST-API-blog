from typing import Dict

from django.contrib.auth import get_user_model
from rest_framework import serializers

from api_comments.models import Post, Comment

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created', 'owner', 'comments']

    def to_representation(self, instance: Post) -> Dict:
        rep = super(PostSerializer, self).to_representation(instance)
        rep['created'] = instance.created.strftime('%Y-%m-%d %H:%M:%S')
        return rep


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'created', 'post', 'parent']

    def to_representation(self, instance: Comment) -> Dict:
        rep = super(CommentSerializer, self).to_representation(instance)
        rep['post'] = instance.post.title
        rep['created'] = instance.created.strftime('%Y-%m-%d %H:%M:%S')
        return rep
