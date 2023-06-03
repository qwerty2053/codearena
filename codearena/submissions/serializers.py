from django.contrib.auth.models import User
from rest_framework import serializers

from problemset.serializers import ProblemBriefSerializer
from .models import Submission, Language


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class SubmissionSerializer(serializers.ModelSerializer):
    problem = ProblemBriefSerializer()
    language = serializers.SerializerMethodField()
    author = UserSerializer()

    class Meta:
        model = Submission
        exclude = ['relative_time', 'source_code', 'points', 'contest']  # 'testset_dir'

    def get_language(self, instance):
        return instance.language.name


# TO DO: Include testset (input, output and expected output)
class SubmissionWithCodeSerializer(serializers.ModelSerializer):
    problem = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    contest = serializers.SerializerMethodField()
    author = UserSerializer()

    class Meta:
        model = Submission
        exclude = ['relative_time', 'points']

    def get_language(self, instance):
        return instance.language.name

    def get_contest(self, instance):
        if instance.contest:
            return instance.contest.title
        return None

    def get_problem(self, instance):
        return instance.problem.title
