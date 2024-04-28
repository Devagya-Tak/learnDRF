from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
  courses = {
    'course-name': 'Python',
    'learn': ['flask', 'Django'],
    'course-provider': 'Scaler'
  }
  return Response(courses)