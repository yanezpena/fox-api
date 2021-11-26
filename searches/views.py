from django.http.response import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from searches.models import Result

from .serializers import ResultSerializer

import subprocess

cmd = ['cat', '/home/carlosy/Projects/django/fox/countries.json']

# Create your views here.


@api_view(['GET'])
def home(request):
    api_availables = {
        "List": "result-list/",
    }
    return Response(api_availables)


@api_view(['GET'])
def ResultList(request):
    result = subprocess.run(
        cmd,
        capture_output=True)
    res = eval(result.stdout.decode('utf-8'))
    print(request.query_params)
    # results = Result.objects.all()
    # serializer = ResultSerializer(results, many=True)
    # return JsonResponse(result.stdout, safe=False)
    return JsonResponse(res, safe=False)
