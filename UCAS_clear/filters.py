import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class CourseFilter(django_filters.FilterSet):
    university_name = CharFilter(field_name='university_name', lookup_expr='icontains')
    course_name = CharFilter(field_name='course_name', lookup_expr='icontains')

    class Meta:
        model = Course
        fields = [
            'university_name', 
            'course_name', 
        ]