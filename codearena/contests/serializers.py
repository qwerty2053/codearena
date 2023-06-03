from django.contrib.auth.models import User
from rest_framework import serializers

from problemset.models import Problem
from .models import Contest


class ProblemBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['id', 'title', 'points']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ContestDetailSerializer(serializers.ModelSerializer):
    problems = ProblemBriefSerializer(many=True)
    author = UserSerializer()

    class Meta:
        model = Contest
        fields = ['title', 'start_time', 'duration', 'problems', 'author']


class ContestSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Contest
        fields = '__all__'


class ContestBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = ['id', 'title']
