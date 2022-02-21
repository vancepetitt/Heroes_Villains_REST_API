from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from supers.serializers import SuperSerializer


# Create your views here.
#@api_view is included in Django REST framework, allows for GET,POST,PUT,DELETE functionality.


@api_view(['GET', 'POST']) #used for getting an entire super object
def supers_list(request):

    if request.method == 'GET':
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data) #populated the serializer with the incoming data
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['GET']) #used when looking for a specific super or an object in the class, via their pk. URLS end in /pk/
def super_detail(request,pk):

    super = get_object_or_404(Super,pk=pk)

    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)

    else:
        pass