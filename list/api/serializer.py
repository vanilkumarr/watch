from rest_framework import serializers
from list.models import Watchlist,StreamPlatform,Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Reviews
        fields = "__all__"


class WatchlistSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True, read_only=True)
    class Meta:
        model=Watchlist
        fields="__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist=WatchlistSerializer(many=True,read_only=True)
    class Meta:
        model=StreamPlatform
        fields="__all__"

















    # objects = None
    # id = serializers.IntegerField(read_only=True)
    # Name = serializers.CharField()
    # Description=serializers.CharField()

    # def create(self, validated_data):
    #     return Movies.objects.create(**validated_data)
    # def update(self,instance,validated_data):
    #     instance.Name=validated_data.get("Name",instance.Name)
    #     instance.Description=validated_data.get("Description",instance.Description)
    #     instance.save()
    #     return instance