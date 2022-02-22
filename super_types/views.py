from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperTypeSerializer
from .models import SuperType
from super_types.serializers import SuperTypeSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def super_types_list(request):

    super_types = SuperType.objects.all()

    if request.method == 'GET':
        
        serializer = SuperTypeSerializer(super_types, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data) #populated the serializer with the incoming data
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE']) #used when looking for a specific super type, via their pk. URLS end in /pk/
def super_type_detail(request,pk):

    super_type = get_object_or_404(SuperType,pk=pk)

    if request.method == 'GET':
        serializer = SuperTypeSerializer(super_type)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = SuperTypeSerializer(super_type, data=request.data) #takes incoming serializer data for pk, and replaces with new values from API.
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        super_type.delete()
        return Response(status.HTTP_204_NO_CONTENT) #delete method already in framework, returns correct status message for display.