from django_filters import FilterSet

from api_comments.models import Comment


class CommentsFilter(FilterSet):

    class Meta:
        model = Comment
        fields = {
            'parent': ['exact'],
            'owner': ['exact'],
            # 'number_of_pages': ['gte', 'exact', 'lte']
        }
