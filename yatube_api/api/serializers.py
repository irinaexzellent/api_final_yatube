from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from posts.models import Comment, Post, Group, Follow, User


class CommentSerializer(serializers.ModelSerializer):
    """Класс для преобразования сложных данных в простые типы данных Python,
    которые конвертируются в JSON.
    """
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username',
                            queryset=User.objects.all(),
                            default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        fields = ("id", "user", "following")
        model = Follow

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]

    def validate(self, data):
        """
        Проверяет: 'user не равен 'following'.
        """
        if data['user'] == data['following']:
            raise serializers.ValidationError('Вы не можете'
                                              'подписаться на себя.')
        return data


class PostSerializer(serializers.ModelSerializer):
    """Класс для преобразования сложных данных в простые типы данных Python,
    которые конвертируются в JSON.
    """
    author = SlugRelatedField(slug_field='username',
                              read_only=True)

    class Meta:
        fields = ('id', 'text', 'author',
                  'group', 'image', 'pub_date')
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Класс для преобразования сложных данных в простые типы данных Python,
    которые конвертируются в JSON.
    """
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group
