from django.contrib.auth import get_user_model
from django.db.models import Q, Count, QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api_comments.filters import CommentsFilter
from api_comments.models import Post, Comment
from api_comments import serializers

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    # filter_backends = [DjangoFilterBackend]
    # filter_class = CommentsFilter

    def get_queryset(self):
        queryset = Comment.objects.all()
        reply_level = self.request.query_params.get('reply_level')
        if reply_level:
            queryset = queryset.filter(level__lte=reply_level)
        level_from = self.request.query_params.get('level_from')
        if level_from:
            queryset = queryset.filter(level__gte=level_from)
        return queryset
