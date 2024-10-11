'''Questão 5 (1 ponto): O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca
de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que
contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente
do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você
foi contratado para desenvolver o programa que monta esta tabela de preços e demonstra o
funcionamento dela quando a atendente insere a quantidade de itens. A tabela conterá os preços de
1 até 50 produtos, conforme o exemplo abaixo:

* Lojas Quase Dois - Tabela de preços

* 1 - R$ 1.99
* 2 - R$ 3.98
* ...
* 50 - R$ 99.50
'''
def main():
    print("* Lojas Quase Dois - Tabela de Preços *")
    for i in range(1, 51):
        print(f"{i} - R$ {1.99 * i:.2f}")

    while True:
        quantidade = int(input("\nQuantidade de itens (0 para sair): "))
        if quantidade == 0:
            break
        elif 1 <= quantidade <= 50:
            print(f"Valor total: R$ {1.99 * quantidade:.2f}")
        else:
            print("Por favor, digite um valor entre 1 e 50.")

if __name__ == "__main__":
    main()
