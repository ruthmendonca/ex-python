#Desafio: Criar o jogo JOKENPO

from random import randint
from time import sleep

#Menu do meu jogo
print("-="*14)
print('''Boas-vindas ao jogo
PYTHON JOKENPO
Suas opções:
(0)- PEDRA
(1)- PAPEL
(2)-TESOURA''')
print("-="*14)

jokenpo = ['pedra','papel', 'tesoura']

#minha jogada
j = int(input('Realize a sua jogada:'))
c = randint(0, 2)
print("-="*14)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print("-="*14)

print(f'O computador jogou {jokenpo[c]}')

#Verificar se a jogada é legal
if j > 2 or j < 0:
    print("Você tentou trapacear!!!!")
else:
    print(f"A sua jogada foi {jokenpo[j]}")

print("-="*14)
print("O vencedor da partida foi...")
sleep(5)

if (j == 0 and c == 0) or (j == 1 and c == 1) or (j == 2 and c == 2):
    print('Empate!')

elif (j == 0 and c == 2) or (j == 1 and c == 0) or (j == 2 and c == 1):
    print("Você venceu!")

elif (c == 0 and j == 2) or (c == 1 and j == 0) or (c == 2 and j == 1):
    print("O computador venceu!")
else:
    print("O computador venceu!")
print("-="*14)
