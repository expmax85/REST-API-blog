from pprint import pprint

from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api_comments.filters import CommentsFilter
from api_comments.models import Comment, Post
from api_comments import serializers

User = get_user_model()


class PostViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class CommentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Comment.objects.select_related('parent', 'post').all()
    serializer_class = serializers.CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = CommentsFilter

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.GET.get('nested'):
            queryset = instance.get_descendants(include_self=request.GET.get('include_self', False))
            serializer = self.get_serializer(queryset, many=True)
        else:
            serializer = self.get_serializer(instance)
        return Response(serializer.data)
