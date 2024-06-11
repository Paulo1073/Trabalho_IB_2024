#7)Escreva um algoritmo que leia o nome do aluno, o nome da disciplina, 2 notas, calcule a média,
#e informe se está aprovado ou reprovado como na saída: {nome} está {situacao} na disciplina {disciplina}.

nome = input("Digite seu Nome: ")
disciplina = input("Qual foi a disciplina: ")
n1 = int(input("qual a primeira nota: "))
n2 = int(input("Qual a segunda nota: "))

m = (n1 + n2)/2

if m >= 6:
    print(f"{nome} está APROVADO na diciplina {disciplina}")
else:
    print(f"{nome} está REPROVADO na diciplina {disciplina}")