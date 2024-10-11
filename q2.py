'''Questão 2 (1 ponto): Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números ímpares.
'''
pares = impares = 0

for _ in range(10):
    if int(input("Digite um número: ")) % 2 == 0:
        pares += 1
    else:
        impares += 1

print(pares, "Pares,", impares, "Ímpares")


