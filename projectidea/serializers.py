__author__ = 'Morya Jr'
from rest_framework import serializers
from projectidea.models  import Idea, Category
from django.utils import timezone
from ideaproject.settings import consumer_key, consumer_secret, access_token, access_token_secret, text_api_id_key, text_api_secret
import tweepy
from aylienapiclient import textapi

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class IdeaSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = Idea.user.username
    class Meta:
        model = Idea
        fields = ('id', 'user', 'title', 'idea',
                  'created_at', 'updated_last', 'category', 'sentiment')
        read_only_fields = ('user', 'created_at', 'updated_last', 'sentiment', 'tweet_id')


    def create(self, validated_data):
        idea = Idea.objects.create(**validated_data)
        client = textapi.Client(text_api_id_key, text_api_secret)
        idea.sentiment = client.Sentiment({'text': idea.idea})
        return Idea.objects.create(**validated_data)

    def update(self, instance, validated_data):
        client = textapi.Client(text_api_id_key, text_api_secret)
        instance.sentiment = client.Sentiment({'text': instance.idea})
        instance.user = validated_data.get('user', instance.user)
        instance.title = validated_data.get('title', instance.title)
        instance.idea = validated_data.get('idea', instance.idea)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_last = timezone.now()
        instance.category = validated_data.get('category', instance.category)
        instance.save()
