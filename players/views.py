from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Pelada, Configuracao, Jogador, Time
from . import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import generics, status, viewsets, exceptions
from players import permissions

# Create your views here.
class PeladaViewSet(generics.ListAPIView):

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

    name = 'jogador-detail'
    queryset =  Jogador.objects.all()
    serializer_class = serializers.JogadoresSerializerDetail
    model = Jogador

class TimeDetailViewSet(generics.RetrieveUpdateDestroyAPIView):

    name = 'times-detail'
    queryset =  Time.objects.all()
    serializer_class = serializers.TimesSerializerDetail
    model = Time

class ConfiguracaoDetailViewSet(generics.RetrieveUpdateDestroyAPIView):

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

    # def get_object(self):
    #     return Pelada.objects.all()
    #
    # """
    #    List all snippets, or create a new snippet.
    #    """
    #
    # def get(self, request, format=None):
    #     peladas = self.get_object().filter(dono=request.user)
    #     serializer_context = {
    #         'request': request,
    #     }
    #     serializer = serializers.PeladaSerializerDetail(peladas, many=True, context=serializer_context)
    #     return Response(serializer.data)
