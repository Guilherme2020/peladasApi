from django.db import models


# Create your models here.


class Jogadores(models.Model):
    DIREITO, ESQUERDO = "D", "E"
    MELHOR_PE = (
        (DIREITO, ("Direito")),
        (ESQUERDO, ("Esquerdo")),
    )
    nome = models.CharField(max_length=255, )
    nivel = models.IntegerField(max_length=10)
    pelada = models.ForeignKey('Pelada', related_name='jogadores', on_delete=models.CASCADE)


class Times(models.Model):
    nome = models.CharField(max_length=255)
    jogadores = models.ForeignKey(Jogadores, related_name='jogadores', on_delete=models.CASCADE)
    pelada = models.ForeignKey('Pelada', related_name='times', on_delete=models.CASCADE)


class Partidas(models.Model):
    gols = models.ForeignKey("Gol")
    times = models.ForeignKey("Times", related_name="partidas")
    pelada = models.ForeignKey('Pelada', related_name='times', on_delete=models.CASCADE)

class Pelada(models.Model):
    nome = models.CharField(max_length=200)
    configuracao = models.OneToOneField('Configuracao')


class Gol(models.Model):
    jogador = models.OneToOneField("Jogador", related_name='gols_jogador')
    time = models.OneToOneField("Time", related_name='gols_time')


class Configuracao(models.model):
    TEMPO1, TEMPO2 = "T1", "T2"
    TEMPOS = (
        (TEMPO1, ("1 Tempo")),
        (TEMPO2, ("2 Tempos")),
    )
    LIMITE_GOLS = (
        ("1", "1 GOL"),
        ("2", "2 GOLS"),
        ("3", "3 GOLS"),
        ("4", "4 GOLS"),
        ("5", "5 GOLS"),
    )
    QTD_JOGADORES = (
        ("5", "5 Jogadores"),
        ("6", "6 Jogadores"),
        ("7", "7 Jogadores"),
        ("8", "8 Jogadores"),
        ("9", "9 Jogadores"),
        ("10", "10 Jogadores"),
        ("11", "11 Jogadores"),
        ("12", "12 Jogadores"),
    )
    ORDEM_CHEGADA, SEM_SORTEIO, NIVEL_TECNICO = 'O', 'S', 'N'
    TIPO_SORTEIO = (
        (ORDEM_CHEGADA, "Ordem de chegada"),
        (SEM_SORTEIO, "Sem sorteio"),
        (NIVEL_TECNICO, "Nivel Tecnico")
    )
    tempos = models.CharField(max_length=1, choices=TEMPOS)
    tempo_duracao = models.TimeField()
    limite_gols = models.CharField(max_length=1, choices=LIMITE_GOLS)
    qtd_jogadores = models.CharField(max_length=1, choices=QTD_JOGADORES)
    tipo_sorteio = models.CharField(max_length=1, choices=TIPO_SORTEIO)
