from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('Vamos jogar?')
print('''Sua opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Faça sua jogada: "))
print('ONE')
sleep(1)
print('TWO')
sleep(1)
print('THREE!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11) 
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print("JOGADA INVÁLIDA")
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
