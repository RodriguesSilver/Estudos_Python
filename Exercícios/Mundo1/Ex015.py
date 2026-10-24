# Alguel de um carro

dias = int(input('Por quantos dias você alugou o carro? '))
kms = float(input('Digite a quantidade de KMS percorridos '))
valor = 60 * dias + 0.15 * kms

print(f'Valor a pagar: R${valor:.2f}')

