from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from . models import calc_data
from rest_framework.response import Response
# from . Seralizer import calc_dataSerializers
from django.http import HttpResponse

def home(request):
    response = HttpResponse('Calc API \n\n GET Method: <your url>/calc?value1=5&value2=4&operation=+ \n\nPOST Method: <your url>/calc\nParams: {value1: 5, value2: 4 , operation:+}', content_type="text/plain")
    return response

@api_view(['GET','POST'])
def calculation(request):
    if request.method == 'GET' or 'POST':
        num1 = int(request.GET['value1'])
        num2 = int(request.GET['value2'])
        opt =  str(request.GET['operation'])
            # return JsonResponse(data, safe=False)
        if opt=="-":
            result = num1 - num2
            data = {'Output': result}
            # return JsonResponse(data, safe=False)
        elif opt=="*":
            result = num1 * num2
            data = {'Output': result}
        elif opt==" ":
            result=num1 + num2
            data = {'Output': result}
        return JsonResponse(data, safe=False)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)



