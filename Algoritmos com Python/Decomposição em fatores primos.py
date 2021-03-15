"""Fazer um programa que leia um número inteiro positivo e faça a decomposição em fatores primos deste número."""

numero = int(input("Digite um número positivo: "))
fator = 2
while numero > 1:
  if numero % fator == 0:
    numero = numero / fator
    print(fator,'*', sep='',end='')
  else:
    fator += 1