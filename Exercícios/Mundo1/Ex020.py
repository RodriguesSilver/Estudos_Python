# Sorteio
import random

al1 = input('Digite o primeiro aluno: ')
al2 = input('Digite o segundo aluno: ')
al3 = input('Digite o terceiro aluno: ')
al4 = input('Digite o quarto aluno: ')
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
