from .models import Song, Singer
from rest_framework import serializers


class SonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True,read_only=True)
    # song = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    # song = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
    class Meta:
        model = Singer
        fields = ['id','name','gender','song']
