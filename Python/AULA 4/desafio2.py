codigo = int(input("Digite o código do item entre 1 e 5: "))
quantidade = int(input("Digite a quantidade de items que você deseja: "))

if codigo == 1:
    preco = 4.00 * quantidade
    print(f"O valor total será de R${preco:.2f}")
elif codigo == 2:
    preco = 4.5 * quantidade
    print(f"O valor total será de R${preco:.2f}")
elif codigo == 3:
    preco = 5.00 * quantidade
    print(f"O valor total será de R${preco:.2f}")
elif codigo == 4:
    preco = 2.00 * quantidade
    print(f"O valor total será de R${preco:.2f}")
elif codigo == 5:
    preco = 1.5 * quantidade
    print(f"O valor total será de R${preco:.2f}")
