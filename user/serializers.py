from rest_framework import serializers

from .models import User, Scrap, Message, Write, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = "__all__"

class ScrapSerializer(serializers.ModelSerializer):
    class Meta :
        model = Scrap
        fields = "__all__"

class WriteSerializer(serializers.ModelSerializer):
    class Meta :
        model = Write
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    class Meta :
        model = Message
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"