numero = int(input("Digite um número entre 1 e 10 para saber sua tabuada: "))
if 1 <= numero <= 10: #ou if numero >=1 & numero <=10
    print(f"Tabuada do número {numero}")

    for i in range(1,11):
        print(f'{numero} x {i} = {numero * i}')
else:
    print("Número inválido")