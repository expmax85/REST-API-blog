from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'posts', 'comments']

    def to_representation(self, instance):
        rep = super(UserSerializer, self).to_representation(instance)
        rep['posts'] = instance.posts.all().values('id', 'title', 'created')
        return rep