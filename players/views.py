from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView
from rest_framework_jwt.serializers import JSONWebTokenSerializer, VerifyJSONWebTokenSerializer, \
    RefreshJSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView

from .models import Pelada, Configuracao, Jogador, Time
from . import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import generics, status, viewsets, exceptions
from players import permissions
from .permissions import PublicEndpoint


# Create your views here.

class ObtainJSONWebToken(JSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.
    Returns a JSON Web Token that can be used for authenticated requests.
    """

    throttle_scope = 'obtain-token'
    throttle_classes = (ScopedRateThrottle,)

    serializer_class = JSONWebTokenSerializer

class VerifyJSONWebToken(JSONWebTokenAPIView):
    """
    API View that checks the veracity of a token, returning the token if it
    is valid.
    """

    throttle_scope = 'obtain-token'
    throttle_classes = (ScopedRateThrottle,)
    serializer_class = VerifyJSONWebTokenSerializer


class RefreshJSONWebToken(JSONWebTokenAPIView):
    """
    API View that returns a refreshed token (with new expiration) based on
    existing token
    If 'orig_iat' field (original issued-at-time) is found, will first check
    if it's within expiration window, then copy it to the new token
    """

    throttle_scope = 'obtain-token'
    throttle_classes = (ScopedRateThrottle,)
    serializer_class = RefreshJSONWebTokenSerializer



class PeladaViewSet(generics.ListAPIView):

    permission_classes = (PublicEndpoint,)
    name = 'pelada-list'
    serializer_class = serializers.PeladaSerializers
    model = Pelada
    queryset = Pelada.objects.all()

class PeladaDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        permissions.IsOwnerPelada,

    )
    name = 'pelada-detail'
    queryset =  Pelada.objects.all()
    serializer_class = serializers.PeladaSerializerDetail
    model = Pelada

class JogadorDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        permissions.IsPelada,

    )

    name = 'jogador-detail'
    queryset =  Jogador.objects.all()
    serializer_class = serializers.JogadoresSerializerDetail
    model = Jogador

class TimeDetailViewSet(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (
        permissions.IsPelada,

    )

    name = 'times-detail'
    queryset =  Time.objects.all()
    serializer_class = serializers.TimesSerializerDetail
    model = Time

class ConfiguracaoDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        permissions.IsPelada,

    )

    name = 'configuracao-detail'
    queryset =  Configuracao.objects.all()
    serializer_class = serializers.ConfiguracaoSerializerDetail
    model = Configuracao


class PeladaListUser(generics.ListCreateAPIView):

    serializer_class = serializers.PeladaSerializerDetail

    def get_queryset(self):
        return Pelada.objects.filter(dono=self.request.user)

    def validate(self, data):
        errors = {}
        dono = data.get('dono')

        if self.request.user != dono:
            errors['error'] = 'O usuario não pode criar'
            raise serializers.ValidationError(errors)

        return data

    def post(self, request, *args, **kwargs):
        dono = request.data['dono']
        dono = dono.split('/')
        tamanho = len(dono)
        dono = int(dono[tamanho - 1])
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if dono == self.request.user.id:

            if serializer.is_valid():
                pelada = serializer.save()

                print(self.request.user.id)
                return Response(status=status.HTTP_201_CREATED,
                                    data=serializers.PeladaSerializers(pelada, context={'request': request}).data)
        else:
            raise exceptions.NotAcceptable(detail=('O usuario só pode criar peladas para ele.'))

