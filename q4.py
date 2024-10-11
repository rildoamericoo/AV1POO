'''Questão 4 (1.5 pontos): A população de um país A é de 80.000 habitantes, com uma taxa anual de
crescimento de 3%. A população do país B é de 200.000 habitantes, com uma taxa de crescimento de
1.5%. Faça um programa que calcule quantos anos serão necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantendo as taxas de crescimento.
'''

a, b, anos = 80000, 200000, 0

while a < b:
    a *= 1.03
    b *= 1.015
    anos += 1

print(anos)

