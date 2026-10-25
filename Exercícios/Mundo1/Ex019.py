# Sorteio
import random

al1 = input('Digite o primeiro aluno: ')
al2 = input('Digite o segundo aluno: ')
al3 = input('Digite o terceiro aluno: ')
lista = [al1, al2, al3]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')




