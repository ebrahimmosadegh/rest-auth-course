from rest_framework import serializers

from blog.models import Article
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name"]


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedIdentityField(view_name='api:authors-detail')
    class Meta:
        model = Article
        fields = "__all__"

    def validate_title(self, value):
        filter_list = ["javascript", "laravel", "php"]
        for i in filter_list:
            if i not in value:
                raise serializers.ValidationError("word is not about this text: {}".format(i))
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"