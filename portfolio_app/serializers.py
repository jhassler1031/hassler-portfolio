from rest_framework import serializers
from portfolio_app.models import Project

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'tech_used', 'github_link', 'description']
