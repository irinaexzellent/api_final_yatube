from django.shortcuts import get_object_or_404

from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, FollowSerializer
from .serializers import GroupSerializer, PostSerializer

from posts.models import Comment, Follow, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """
    Простой ViewSet для просмотра и редактирования постов.
    Разрешения уровня запросов 'GET', 'HEAD', 'OPTIONS' --
    доступ разрешен аутифенцированному и неаутифенцированному пользователю.
    Объектный уровень разрешений -- позволяет
    редактировать объект только автору объекта.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@action(detail=True, methods=['get'])
class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Простой ViewSet для просмотра групп.
    Разрешения уровня запросов 'GET', 'HEAD', 'OPTIONS'--
    доступ разрешен неаутифенцированному пользователю.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Простой ViewSet для просмотра и редактирования комментариев постов.

    Разрешения уровня запросов 'GET', 'HEAD', 'OPTIONS' --
    доступ разрешен аутифенцированному и
    неаутифенцированному пользователю.

    Объектный уровень разрешений -- позволяет
    редактировать комментарий только автору объекта.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, post_id=self.kwargs.get('post_id')
        )

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()


@action(detail=True, gmethods=['get', 'post'])
class FollowViewSet(viewsets.ModelViewSet):
    """
    Простой ViewSet для выполнения подписок на авторов.

    Разрешения уровня запросов -- доступ разрешен аутифенцированному
    пользователю.

    Объектный уровень разрешений -- позволяет
    выполнять подписки только аутифицированному пользователю.
    """
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
