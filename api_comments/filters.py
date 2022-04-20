from django_filters import FilterSet

from api_comments.models import Comment


class CommentsFilter(FilterSet):

    class Meta:
        model = Comment
        fields = {
            'level': ['gte', 'lte']
        }
