__author__ = 'Morya Jr'
from rest_framework import serializers
from projectidea.models  import Idea
from django.utils import timezone
from ideaproject.settings import consumer_key, consumer_secret, access_token, access_token_secret, text_api_id_key, text_api_secret
import tweepy
from aylienapiclient import textapi
from django.contrib.auth.models import User




class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ('id', 'title', 'idea',
                  'created_at', 'updated_last', 'category', 'sentiment')
        read_only_fields = ('created_at', 'updated_last', 'sentiment')


    def create(self, validated_data):
        idea = Idea.objects.create(**validated_data)
        client = textapi.Client(text_api_id_key, text_api_secret)
        sentiment = client.Sentiment({'text': idea.idea})
        idea.sentiment = sentiment.get('polarity')
        return idea

    def update(self, instance, validated_data):
        client = textapi.Client(text_api_id_key, text_api_secret)
        instance.sentiment = client.Sentiment({'text': instance.idea}).get('polarity')
        instance.title = validated_data.get('title', instance.title)
        instance.idea = validated_data.get('idea', instance.idea)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_last = timezone.now()
        instance.save()
        return  instance
