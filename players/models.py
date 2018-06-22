from django.db import models

# Create your models here.


class Jogadores(models.Model):
    nome = models.CharField(max_length=255,)
    nivel = models.IntegerField(max_length=10)

class Times(models.Model):
    nome = models.CharField(max_length=255)
    jogadores  = models.ForeignKey(Jogadores,related_name='jogadores',on_delete=models.CASCADE)

class Partidas(models.Model):
    por_quantidade_gols = 'quantidade_gols'
    por_tempo =  'por_tempo'
    CHOISE = (por_quantidade_gols,por_tempo)
    tempo_duracao = models.TimeField()
    tipo_partida = models.CharField(max_length=2,choices=CHOISE)

class Pelada(models.Model):
    times = models.ForeignKey(Times, related_name='times',on_delete=models.CASCADE)
    local = models.CharField(max_length=255)
    horario = models.TimeField()
