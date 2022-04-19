from django.contrib.auth import get_user_model

import django_filters
from rest_framework import viewsets

from users import serializers

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
