from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ProjectSerializer, ExperienceSerializer, EducationSerializer
from .models import Project, Experience, Education


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all().order_by('title')
    serializer_class = ProjectSerializer


class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all().order_by('start_time')
    serializer_class = ExperienceSerializer


class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all().order_by('start_time')
    serializer_class = EducationSerializer
