from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from api.models import Tutorials
from rest_framework import status
from rest_framework.parsers import JSONParser
from api.serializers import TutorialSerializer

# Create your views here.
@api_view(['GET','POST','DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorials.objects.all()
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Tutorials.objects.all().delete()
        return JsonResponse({
            'message':'{} tutorials were deleted successfully! '.format(count[0])
        },status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def tutorial_details(request,pk):
    try:
        tutorial = Tutorials.objects.get(pk=pk)

        if request.method == 'GET':
            tutorial_serializer = TutorialSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

        elif request.method == 'PUT':
            tutorial_data = JSONParser().parse(request)
            tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(tutorial_serializer.data)

        elif request.method == 'DELETE':
            tutorial.delete()
            return JsonResponse({
                'message': "tutorial was deleted successfully!"
            },status=status.HTTP_204_NO_CONTENT)

    except Tutorials.DoesNotExist:
        return JsonResponse({
            'message':"tutorial does not exist"
        },status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorials.objects.filter(published=True)

    if request.method == 'GET':
        tutorial_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorial_serializer.data, safe=True)
