from django.contrib.auth import get_user_model
from rest_framework import serializers

from api_comments.models import Post, Comment

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created', 'owner', 'comments']

    def to_representation(self, instance):
        rep = super(PostSerializer, self).to_representation(instance)
        rep['owner'] = instance.owner.username
        rep['created'] = instance.created.strftime('%Y-%m-%d %H:%M:%S')
        return rep


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'text', 'owner', 'post', 'parent']

    def to_representation(self, instance):
        rep = super(CommentSerializer, self).to_representation(instance)
        rep['owner'] = instance.owner.username
        rep['post'] = instance.post.title
        return rep