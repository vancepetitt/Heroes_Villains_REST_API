from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Super
from supers.serializers import SuperSerializer


# Create your views here.
#@api_view is included in Django REST framework, allows for GET,POST,PUT,DELETE functionality.
@api_view(['GET'])
def supers_list(request):

    supers = Super.objects.all()
    serializer = SuperSerializer(supers, many = True)

    return Response(serializer.data)
