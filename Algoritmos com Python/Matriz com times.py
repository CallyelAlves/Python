"""
Faça um programa no qual o usuário preenche duas matrizes de 10 x 2. Na primeira matriz, cada linha possui os nomes de dois times que se enfrentam, enquanto na segunda matriz estão os placares dos jogos.

O usuário deve, inicialmente, fornecer os nomes de todos os times que se enfrentam. Na sequência, ele fornece o placar de cada jogo. O programa deve indicar os times que venceram seus jogos. Caso todos os jogos tenham terminado empatados, o programa indica isso com uma mensagem.

"""

#criação de variáveis
empate = 0
linhas = 10
colunas = 2
times = []
placar = []
vencedores = []

#criando as matrizes
for i in range(linhas):
    times.append([0] * (colunas))

for i in range(linhas):
    placar.append([0] * (colunas))

#add valores as matrizes
for i in range(linhas):
  print('Patida', i+1)
  for a in range(colunas):
   print('Digite o time', a+1)
   times[i][a] = input()

print()

for i in range(linhas):
  for a in range(colunas):
    print('Digite quantos gols fez', times[i][a])
    placar[i][a] = int(input())

#ediçao de saída da matriz
for i in range(linhas):
  for a in range(colunas):
    print(times[i][a],' ', end='')
  print()

print()
for i in range(linhas):
  for a in range(colunas):
    print(placar[i][a],' ', end='')
  print()
print()

#condições das matrizes
for i in range(linhas):
  if placar[i][0] > placar[i][1]:
    vencedores.append(times[i][0])
  elif placar[i][0] < placar[i][1]:
    vencedores.append(times[i][1])
  else:
    empate +=1
if empate == linhas:
  print('Todos os jogos foi empate')
else:
  print('Times que venceram seus jogos', *vencedores, sep=' - ')