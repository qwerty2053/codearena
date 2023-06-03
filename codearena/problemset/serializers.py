from rest_framework import serializers

from .models import Problem, Tag
from contests.serializers import ContestBriefSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProblemDetailSerializer(serializers.ModelSerializer):
    contest = ContestBriefSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Problem
        exclude = ['created_at', 'updated_at']


class ProblemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Problem
        fields = ['id', 'title', 'tags', 'solved_count', 'points']


class ProblemBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['id', 'title']
