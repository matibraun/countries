import requests
from .pagination import CountryPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import CountrySerializer
from .models import Country
from django.db import transaction
from django.shortcuts import get_object_or_404

class CountriesAPIView(APIView):
    """
    API endpoint that:
    - Retrieve countries information from REST Countries API and saves them to the database (post)
    - List all countries and their info (get)
    - Retrieve info from one specific country thru id (get /id)
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        """
        Handle POST requests:
        - Retrieve countries information from REST Countries API and saves them to the database (post)
        """
        try:

            url = "https://restcountries.com/v3.1/all?fields=name,flags,capital,population,continents,timezones,area,latlng"
            response = requests.get(url)
            response.raise_for_status()
            
            countries = response.json()
            
            with transaction.atomic():

                Country.objects.all().delete()
                
                serializer = CountrySerializer(data=countries, many=True)
                
                if serializer.is_valid():
                    serializer.save()
                    
                    return Response({
                        'message': 'Countries successfully imported',
                        'count': len(countries)
                    }, status=status.HTTP_201_CREATED)

                else:
                    return Response({
                        'error': 'Validation failed',
                        'details': serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
        
        except requests.RequestException as e:
            return Response({
                'error': 'Failed to fetch countries data',
                'details': str(e)
            }, status=status.HTTP_502_BAD_GATEWAY)
        
        except Exception as e:
            return Response({
                'error': 'An unexpected error occurred',
                'details': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get(self, request, pk=None, format=None):
        """
        Handle GET requests:
        - Retrieve all countries if no `pk` is provided.
        - Retrieve a specific country by `pk` if provided.
        """
        if pk:

            country = get_object_or_404(Country, pk=pk)
            serializer = CountrySerializer(country)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            countries = Country.objects.all()
            paginator = CountryPagination()
            paginated_countries = paginator.paginate_queryset(countries, request)
            serializer = CountrySerializer(paginated_countries, many=True)

            return paginator.get_paginated_response(serializer.data)


