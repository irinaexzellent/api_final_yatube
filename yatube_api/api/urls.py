from rest_framework.routers import SimpleRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

from django.urls import include, path

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
