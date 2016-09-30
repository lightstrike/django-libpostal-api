from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView


class ExpandAPIView(APIView):
    def get(self, request, format=None):
        expanded = {'hey': 'expanded'}
        return JsonResponse(expanded, status=status.HTTP_200_OK)


class ParseAPIView(APIView):
    def get(self, request, format=None):
        expanded = {'hey': 'parsed'}
        return JsonResponse(expanded, status=status.HTTP_200_OK)
