from collections import OrderedDict

from django.http import JsonResponse
from postal.expand import expand_address
from postal.parser import parse_address
from rest_framework import status
from rest_framework.views import APIView


class ExpandAPIView(APIView):
    def get(self, request, format=None):
        try:
            address = request.query_params['address']
        except KeyError:
            error_message = {
                'error': 'You must pass `address` as a query parameter.'
            }
            return JsonResponse(error_message, status=status.HTTP_400_BAD_REQUEST)

        expanded_list = expand_address(address)
        expanded = {
            'results': expanded_list,
        }
        return JsonResponse(expanded, status=status.HTTP_200_OK)


class ParseAPIView(APIView):
    def get(self, request, format=None):
        try:
            address = request.query_params['address']
        except KeyError:
            error_message = {
                'error': 'You must pass `address` as a query parameter.'
            }
            return JsonResponse(error_message, status=status.HTTP_400_BAD_REQUEST)
        parser_results = parse_address(address)
        if 'raw' in request.query_params:
            parsed_dict = OrderedDict(parser_results)
        else:
            # Reverse items to get one unique classification key per query
            reversed_items = [(item[1], item[0]) for item in parser_results]
            parsed_dict = OrderedDict(reversed_items)
        return JsonResponse(parsed_dict, status=status.HTTP_200_OK)
