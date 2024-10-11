'''Questão 6 (1 ponto): Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se
que esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00. Faça um programa
que determine o salário desse funcionário em 2025, sabendo que:
* Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
* A partir de 1997 (inclusive),
'''

salario_inicial = 1000.00
ano_inicial = 1996
ano_final = 2025
aumento_inicial = 1.015
aumento_anual = 1.02

# Aplicar o aumento inicial de 1,5% em 1996
salario = salario_inicial * aumento_inicial

# Aplicar os aumentos anuais de 2% de 1997 até 2025
for _ in range(ano_inicial + 1, ano_final + 1):
    salario *= aumento_anual

print(f"Salário em {ano_final}: R$ {salario:.2f}")


