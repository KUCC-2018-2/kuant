from rest_framework import serializers
from .models import Content, WorkType, WorkPlace


class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class WorktypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = '__all__'


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        fields = '__all__'
