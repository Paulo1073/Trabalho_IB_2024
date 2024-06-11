#10)Peça ao usuário para inserir um número e use um loop for para imprimir a tabuada desse número (de 1 a 10).

numero = int(input("Digite um número para ver sua tabuada: "))

# Usar um loop for para imprimir a tabuada
print(f"Tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")