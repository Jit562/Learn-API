from logging import exception
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

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
