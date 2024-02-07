from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED
from django.http import JsonResponse
# Create your views here.


@api_view(["GET","POST"])
def testing(request):
    testingmyData = testData.objects.all()
    testLocl = testDataSr(data=testingmyData, many=True)
    if request.method == 'GET':
      
        return JsonResponse({'DATA':"THIS IS WORKING AND LIVE"})
    
    if request.method == 'POST':
        if testLocl.is_valid():
            testLocl.save()
            return Response(testLocl.data,status=201)
