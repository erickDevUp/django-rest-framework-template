from rest_framework import serializers
from .models import Course_1

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course_1
        fields=('id','text','description','url')