from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

# Create your views here.

class HelloApiView(APIView):
    """test api view"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """return a list of api view feautures"""

        an_apiview =[
            'Uses HTTP methods as function (get, put,post,delete)'

        ]
        return Response({'messages':'hello','an_apiview':an_apiview} )


    def post(self, request):
        """create a helli message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else :
            return Response (
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
        

    def put(self, request, pk=0):
        return Response({'method':'PUT'})
    

    def patch(self, request, pk=0):
        return Response({'method':'PATCH'})
    

    def delete(self, request, pk=0):
        return Response({'method':'DELETE'})


