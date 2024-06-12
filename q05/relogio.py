#5)Leia um número inteiro entre 0 e 23, este valor representa a hora do relógio. 

hora = int(input("digite um numero entre 0 e 23: "))

if 6 <= hora < 12:
        print(f'São {hora}h da Manhã')
elif 12 <= hora < 18:
         print(f'São {hora}h da Tarde')
elif 17 < hora <= 23:
         print(f'São {hora}h da noite') 
elif 0 <= hora <= 5:
        print(f'São {hora}h da Madrugada')
else:
    print('esse Numero Não Esta No Intervalo de (0 a 23)')
