from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@csrf_exempt
def singer_list(request):
    if request.method == 'GET':
        singer = Singer.objects.all()

        singerseriliazer = SingerSerializer(singer, many=True)
        return JsonResponse(singerseriliazer.data, safe=False)


    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = SingerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)    

@csrf_exempt
def singer_details(request, pk):
    try:
        singer = Singer.objects.get(pk=pk)
    except Singer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = SingerSerializer(singer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)

        serializer = SingerSerializer(singer, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


    elif request.method == 'DELETE':
        singer.delete()
        return HttpResponse(status=204)                    


@api_view(['GET','POST'])
def singerlist(request):
    if request.method == 'GET':

        singer = Singer.objects.all()
    
        singerserializer = SingSerializer(singer, many=True)

        return Response(singerserializer.data)

    elif request.method == 'POST':
        serializer = SingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


@api_view(['GET','PUT','DELETE'])
def singerdetails(request, pk):
    try:
       singer = Singer.objects.get(pk=pk)
    except Singer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SingSerializer(singer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SingSerializer(singer, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    elif request.method == 'DELETE':
        singer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        



@api_view(['GET','POST'])
def songlist(request):
    if request.method == 'GET':

        song = Song.objects.all()
    
        songserializer = SongSerializer(song, many=True)

        return Response(songserializer.data)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)