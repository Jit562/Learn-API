from nbformat import read
from .models import *
from rest_framework import serializers



class SingerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(required = True, allow_blank = True, max_length = 60)
    name = serializers.CharField(max_length=80, required = True, allow_blank = True)
    apdate = serializers.DateTimeField()
    city = serializers.CharField(max_length=70)

    def create(self, validated_data):
        return Singer.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.name = validated_data.get('name', instance.name)
        instance.apdate = validated_data.get('apdate', instance.apdate)
        instance.city = validated_data.get('city', instance.city)
        
        instance.save()

        return instance



class SongSerializer(serializers.ModelSerializer):
    # singer = SingSerializer(many = True, read_only=True)
    # singer = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # songs = serializers.PrimaryKeyRelatedField(many=True,  read_only=False, queryset=Song.objects.all())
    # songs = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    class Meta:
        model = Song
        fields = ['id','title','singer','duration'] 


class SingSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True, read_only=True)
    song = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ['id','name','gender','song']           