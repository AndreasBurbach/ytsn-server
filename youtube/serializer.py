
from django.apps import apps
from django.db.models import QuerySet
from rest_framework import serializers

from the_social_network.serializers.contentSerializers import StatementSerializer, ReactionSerializer
from the_social_network.models import Statement

from youtube.models import YoutubeVideoStatement

class YoutubeStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = YoutubeVideoStatement
        fields = ['videoTime', 'statement', "vote"]