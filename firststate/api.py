from .models import Course_1
from rest_framework import viewsets,permissions
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course_1.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseSerializer