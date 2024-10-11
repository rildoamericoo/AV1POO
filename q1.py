'''Questão 1 (1 ponto): Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída
deve ser conforme o exemplo abaixo:

* Tabuada de 5:

* 5 X 1 = 5
* 5 X 2 = 10
* ...
* 5 X 10 = 50
'''


while True:
    try:
        t = int(input("Digite um número para ver sua tabuada (ou 0 para sair): "))
        if t == 0:
            print("Encerrando o programa.")
            break
        print(f"\nTabuada do {t}:")
        for n in range(1, 11):
            print(f"{t} x {n} = {t * n}")
        print()  # Para espaçar melhor entre as tabuadas
    except ValueError:
        print("Por favor, digite um número inteiro válido.\n")
