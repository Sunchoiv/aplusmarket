from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import AssignmentSerializer   
from .models import Assignment

# Create your views here.
class AssignmentViewSet(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer