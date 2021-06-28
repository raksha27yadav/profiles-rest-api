from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from profiles_api import models
from rest_framework import viewsets
from .models import UserProfile
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticatedOrReadOnly
from . import permissions
class HelloApiView(APIView):
    '''Test API View'''
    serializer_class=serializers.HelloSerializer
    def get(self,request,format=None):
        an_apiview=['Uses HTTP method as a function(get,post,patch,put,delete)',
        'Its similar to the traditional django',
        'gives yoy the most control over your application logic',
        'Is mapped manually to URLs']
        return Response({'message':'hello!','an_apiview':an_apiview})
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hellooo {name}!'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None):
        '''Handle updating an object'''
        return Response({'method':'PUT'})
    def patch(self,request,pk=None):
        '''Handle partially updating an object'''
        return Response({'method':'PATCH'})
    def delete(self,request,pk=None):
        '''Handle deleting an object'''
        return Response({'method':'DELETE'})
class HelloViewSet(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer
    def list(self,request):
        a_view=['uses actions(list,create,retreive,update,partial_update)',
        'automatically maps to URLs using routers',
        'Provides more functionality with less code']
        return Response({'message':'Hello','a_view':a_view})
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})
    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})
    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})
    def delete(self,request,pk=None):
        return Response({'http_method':'Delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)

class UserLoginApiView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.ProfileFeedItemSerializer
    queryset=models.ProfileFeedItem.objects.all()
    permission_classes={
    permissions.UpdateOwnStatus,IsAuthenticatedOrReadOnly
    }
    def perform_create(self,serializer):
        serializer.save(user_profile=self.request.user)



# Create your views here.
