from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """return a list of api view feautures"""

        an_apiview =[
            'Uses HTTP methods as function (get, put,post,delete)'

        ]
        return Response({'messages':'hello','an_apiview':an_apiview} )


