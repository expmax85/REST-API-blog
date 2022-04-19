from rest_framework import routers

from api_comments.api import PostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
urlpatterns = router.urls

router.register('comments', CommentViewSet, basename='Comment')
urlpatterns += router.urls