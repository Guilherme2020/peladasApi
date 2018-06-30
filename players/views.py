from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Pelada, Configuracao
from . import serializers
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.
class PeladaViewSet(generics.ListAPIView):

    name = 'pelada-list'
    serializer_class = serializers.PeladaSerializers
    model = Pelada
    queryset =  Pelada.objects.all()

class PeladaDetailViewSet(generics.RetrieveUpdateDestroyAPIView):

    name = 'pelada-detail'
    queryset =  Pelada.objects.all()
    serializer_class = serializers.PeladaSerializerDetail
    model = Pelada

class ConfiguracaoDetailViewSet(generics.RetrieveUpdateDestroyAPIView):

    name = 'configuracao-detail'
    queryset =  Configuracao.objects.all()
    serializer_class = serializers.ConfiguracaoSerializerDetail
    model = Configuracao


class PeladaListUser(APIView):

    def get_object(self):
        return Pelada.objects.all()

    """
       List all snippets, or create a new snippet.
       """

    def get(self, request, format=None):
        peladas = self.get_object().filter(dono=request.user)
        serializer_context = {
            'request': request,
        }
        serializer = serializers.PeladaSerializerDetail(peladas, many=True, context=serializer_context)
        return Response(serializer.data)
