from rest_framework import serializers
from .models import Project, Experience, Education


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'role', 'description', 'tags', 'pictures')


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experience
        fields = ('job_title', 'company', 'description', 'start_time', 'end_time')


class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = ('school', 'major', 'description', 'start_time', 'end_time')
