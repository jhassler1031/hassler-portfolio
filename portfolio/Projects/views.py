from django.shortcuts import render
from django.http.response import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from Projects.models import Project
from Projects.serializers import ProjectSerializer


# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to John Hassler's Web Development Portfolio!")

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
        project_description = request.POST["project_description"]

        Project.objects.create(title=title, tech_used=tech_used, github_link=github_link, project_description=project_description)
        return Response({})

class ProjectDetailAPIView(APIView):
    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        serialized_project = ProjectSerializer(project)
        return Response(serialized_project.data)

    
