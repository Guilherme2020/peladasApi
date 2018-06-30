import datetime

from django.contrib.auth.models import User

dono = User.objects.create(username="dono1", email="dono@dono.com",
                           password="dono1", is_staff=True)
dono.set_password("dono1")
dono.save()
from players.models import Configuracao, Pelada, Jogador

configuracao1 = Configuracao.objects.create(tempos=Configuracao.TEMPO1, tempo_duracao=datetime.time(0, 5, 0),
                                            limite_gols=Configuracao.LIMITE_GOLS[1],
                                            qtd_jogadores=Configuracao.QTD_JOGADORES[0][0],
                                            tipo_sorteio=Configuracao.ORDEM_CHEGADA
                                            )
pelada1 = Pelada.objects.create(nome="PELADA 1", configuracao=configuracao1, dono=dono)
# #criando jogadores
jogadores1 = Jogador.objects.create(nome="Willian", rating=4, pelada=pelada1)
jogadores2 = Jogador.objects.create(nome="Neymar", rating=4, pelada=pelada1)
jogadores3 = Jogador.objects.create(nome="Cristiano Ronaldo", rating=4, pelada=pelada1)
jogadores4 = Jogador.objects.create(nome="Messi", rating=4, pelada=pelada1)
jogadores5 = Jogador.objects.create(nome="Neuer", rating=4, pelada=pelada1)
jogadores6 = Jogador.objects.create(nome="Buffon", rating=4, pelada=pelada1)
jogadores7 = Jogador.objects.create(nome="Casemiro", rating=4, pelada=pelada1)
jogadores8 = Jogador.objects.create(nome="Marcelo", rating=4, pelada=pelada1)
jogadores9 = Jogador.objects.create(nome="Rogerio Ceni", rating=4, pelada=pelada1)
jogadores10 = Jogador.objects.create(nome="Kane", rating=4, pelada=pelada1)

print(jogadores1.nome)
print(jogadores2.nome)
print(jogadores3.nome)
print(jogadores4.nome)
print(jogadores5.nome)
