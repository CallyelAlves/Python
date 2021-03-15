"""
Jogo do imprensadinho

Neste programa, o usuário disputa uma partida contra o computador. 
Inicialmente, o computador “pensa” (ou seja, sorteia aleatoriamente) um número entre 1 e 100, sem incluir nem 1 nem 100, mas não informa ao usuário.
A partir daí, o usuário digita palpites sobre qual seria o número, dentro do intervalo fornecido. A cada novo palpite, o computador atualiza o intervalo para o jogador fornecer um novo palpite.
O objetivo do computador é fazer com que o usuário dê o palpite exato. Nesse caso, ele é o vencedor.
O objetivo do jogador é “imprensar” o número pensado com o intervalo, ou seja, fazer com que o intervalo seja formado pelos números imediatamente anterior e posterior ao número pensado.
O jogo acaba assim que o usuário acertar o número (vitória do computador) ou imprensar o número (vitória do jogador).

Exemplo de partida (C: computador; U: usuário)
número pensado = 39
C: Dê um palpite entre 1 e 100
U: 50
C: Entre 1 e 50
U: 20
C: Entre 20 e 50
U: 40
C: Entre 20 e 40
U: 38
C: Entre 38 e 40. Você venceu!

"""
import random
import sys
num = random.randint(2, 99)
menor = 1
maior = 100
print('Digite um numero entre 1 é 100:')
chute = int(input('Res.:'))
if chute == num:
  print('Vitória do computador')
if chute < menor or chute > maior:
  print('Valor inválido')
  sys.exit()
while chute != num:
  if chute < num:
    menor = chute
    print('Entre', menor,'e', maior)
    if (menor+1) == num and (maior-1) == num:
     print('Você venceu!!!')
     break
  else:
    maior = chute
    print('Entre', menor,'e', maior)
    if (menor+1) == num and (maior-1) == num:
     print('Você venceu!!!')
     break
  chute = int(input('Res.:'))
  if chute == num:
   print('Vitória do computador')