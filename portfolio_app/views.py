from django.shortcuts import render
from django.http.response import HttpResponse

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.generic import TemplateView

from portfolio_app.models import Project, File
from portfolio_app.serializers import ProjectSerializer, FileSerializer

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class ProjectListAPIView(APIView):
    def get(self, request):
        all_projects = Project.objects.all()
        serialized_projects = ProjectSerializer(all_projects, many=True)
        return Response(serialized_projects.data)

    def post(self, request):
        print(request.POST)
        title = request.POST["title"]
        tech_used = request.POST["tech_used"]
        github_link = request.POST["github_link"]
        description = request.POST["description"]

        Project.objects.create(title=title, tech_used=tech_used, github_link=github_link, description=description)
        return Response({})

class ProjectDetailAPIView(APIView):
    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        serialized_project = ProjectSerializer(project)
        return Response(serialized_project.data)

    def put(self, request, pk):
        project = Project.objects.get(id=pk)
        project.title = request.POST["title"]
        project.tech_used = request.POST["tech_used"]
        project.github_link = request.POST["github_link"]
        project.description = request.POST["description"]
        project.save()
        return Response({})

    def delete(self, request, pk):
        project = Project.objects.get(id=pk)
        project.delete()
        return Response({})

class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        files = File.objects.all()
        serialized_files = FileSerializer(files, many=True)
        return Response(serialized_files.data, 200)

    def post(self, request, *args, **kwargs):
      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
        file_serializer.save()
        return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileDestroyView(APIView):

    def delete(self, request, pk):
        file = File.objects.get(id=pk)
        file.delete()
        return Response("", 204)
