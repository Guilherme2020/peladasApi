from django.db import models


# Create your models here.


class Jogadores(models.Model):
    DIREITO, ESQUERDO = "D", "E"
    MELHOR_PE = (
        (DIREITO, ("Direito")),
        (ESQUERDO, ("Esquerdo")),
    )
    NOTA_CHOICES = tuple([(x, x) for x in range(1, 6)])

    nome = models.CharField(max_length=255, )
    rating = models.SmallIntegerField(verbose_name='Nota', choices=NOTA_CHOICES, default=3)
    pelada = models.ForeignKey('Pelada', related_name='jogadores', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Times(models.Model):
    nome = models.CharField(max_length=255)
    jogadores = models.ForeignKey(Jogadores, related_name='jogadores', on_delete=models.CASCADE)
    pelada = models.ManyToManyField('Pelada', related_name='times')


class Partidas(models.Model):
    gols = models.ForeignKey("Gol", on_delete=models.CASCADE)
    times = models.ForeignKey("Times", related_name="partidas", on_delete=models.CASCADE)


class Pelada(models.Model):
    nome = models.CharField(max_length=200)
    configuracao = models.OneToOneField('Configuracao', on_delete=models.CASCADE)

    @property
    def create_times(self):
        if self.configuracao.tipo_sorteio == self.configuracao.ORDEM_CHEGADA:
            qtd_jogadores = self.jogadores.all().count()
            jogadores = self.jogadores.all().order_by('created_at')


class Gol(models.Model):
    jogador = models.OneToOneField("Jogadores", related_name='gols_jogador', on_delete=models.CASCADE)
    time = models.OneToOneField("Times", related_name='gols_time', on_delete=models.CASCADE)


class Configuracao(models.Model):
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

