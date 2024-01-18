# ratings/serializers.py
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    average_rate = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = '__all__'


class RateRegisterSerializer(serializers.Serializer):
    rateNumber = serializers.IntegerField(required=True,min_value=0,max_value=5)
    postID = serializers.IntegerField(required=True)

