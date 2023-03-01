import json
from django.http import JsonResponse
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rich import print as pprint

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def api_home(request, *args, **kwargs):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
        },
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
        return Response(data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)


# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  
  def get(self,request,*args,**kwargs):
    if request.user.is_authenticated:
        print('[*] User is authenticated.')
    else:
        print('[*] User is not authenticated.')
        raise PermissionDenied('U must be authenticated to access this.')
    pprint('[*] Request:', request, request.query_params, dir(request), 
          request.__dict__, sep='\n\n', end='\n\n') # debugging info
    
    print('[*]', request.query_params, end='\n\n') # debugging info
    user_id = request.query_params.get('id')
    
    
    if user_id is None:
        return Response({'error': 'id parameter is missing from the request.'}, status=400)
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': f'User with id {user_id} does not exist.'}, status=404)
    pprint('[*]', user_id, user)
    
    serializer = UserSerializer(user)
    return Response(serializer.data)


#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
  