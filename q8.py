'''Questão 8 (2 pontos): Desenvolver um programa para verificar a nota do aluno em uma prova com
10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com
o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
Após todos os alunos terem respondido informar:
a. Maior e Menor Acerto;
b. Total de Alunos que utilizaram o sistema;
c. A Média das Notas da Turma.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
'''

gabarito = 'ABCDEDCDAB'
acertos = []

while True:
    respostas = [input(f"Questão {i + 1}: ").strip().upper() for i in range(len(gabarito))]
    acertos.append(sum(r == g for r, g in zip(respostas, gabarito)))
    
    if input("Outro aluno? (s/n): ").strip().lower() != 's':
        break

if acertos:
    print(f"\nMaior Acerto: {max(acertos)}")
    print(f"Menor Acerto: {min(acertos)}")
    print(f"Total de Alunos: {len(acertos)}")
    print(f"Média das Notas: {sum(acertos) / len(acertos):.2f}")


