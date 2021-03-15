"""
Faça um programa no qual o usuário fornece uma quantidade (especificada por ele) de valores e armazena em um vetor. Imprima esse vetor da forma como o usuário digitou e, na sequência, faça o seguinte:
1 - Solicite ao usuário a digitação de dois valores.
2 - Encontre no vetor a primeira instância de cada um dos dois valores digitados.
3.1 - Caso algum dos valores não esteja presente no vetor, imprima uma mensagem avisando ao usuário.
3.2 - Caso encontre os dois valores, troque-os de lugar e imprima o vetor resultante.

"""

lista = []
pos1, pos2 = 0, 0
qtd_num = int(input('Qual a quantidade de números que deseja digitar?'))
for i in range(qtd_num):
  lista.append(float(input('Digite o número:')))
print('Os números digitados foram: ',lista)
valor1 = float(input('Digite um valor:'))
valor2 = float(input('Digite mais um valor:'))
if valor2 in lista and valor1 in lista:
  pos1 = lista.index(valor2) 
  pos2 = lista.index(valor1)
  lista[pos1] = valor1
  lista[pos2] = valor2 
  print('Trocada as posições:',lista)
else:
  print('Um dos valores digitados não se encontra na lista')