from rest_framework import serializers
from portfolio_app.models import Project, File

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'tech_used', 'github_link', 'description']

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ['id', 'file', 'remark', 'timestamp']
