'''Questão 7 (1 ponto): Faça um programa que receba o valor de uma dívida e mostre uma tabela com
os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Tabela de juros sobre a quantidade de parcelas
Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
1 0
3 10
6 15
9 20
12 25

Exemplo de saída do programa:

|Dívida | Juros |Quantidade de Parcelas | Valor da Parcela|
|R$ 1.000,00 | 0 | 1 | R$ 1.000,00 |
|R$ 1.100,00 | 100 | 3 | R$ 366,00 |
|R$ 1.150,00 | 150 | 6 | R$ 191,67 |
'''
# Solicitar o valor da dívida ao usuário
def calcular_juros(divida, taxa):
    return divida * (taxa / 100)

def exibir_tabela(divida):
    # Cabeçalho da tabela
    print(f"{'| Dívida':<15}{'| Juros':<10}{'| Qtd Parcelas':<15}{'| Valor da Parcela':<20}|")
    print("-" * 60)

    # Tabela de parcelas e taxas
    parcelas = [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]

    for quantidade, taxa in parcelas:
        juros = calcular_juros(divida, taxa)
        total = divida + juros
        parcela = total / quantidade
        print(f"| R$ {total:10.2f} | R$ {juros:7.2f} | {quantidade:12} | R$ {parcela:17.2f} |")

def main():
    try:
        divida = float(input("Digite o valor da dívida: R$ "))
        exibir_tabela(divida)
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

if __name__ == "__main__":
    main()
