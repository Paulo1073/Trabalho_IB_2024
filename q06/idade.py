#6)Sabendo que a idade mínima para um cidadão estar apto a votar é de 16 anos. Escreva um algoritmo que lê o nome do cidadão,
#sua idade e informa se ele pode emitir o seu título de eleitor ou não. 

nome = input("Digite seu nome: ")
idade = int(input("Qual sua idade: "))

if idade >= 16:
    print(f'ola {nome} você tem {idade} ano(s),você poderá tirar o titulo')
else:
    print(f'ola {nome} você tem {idade} ano(s),você não poderá tirar o titulo')