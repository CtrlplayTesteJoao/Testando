numeros = []

for i in range(10):
    valor = int(input(f"Digite o {i+1}º números: "))
    numeros.append(valor)

maior_valor = max(numeros)

posicao = numeros.index(maior_valor) + 1

print(f"O maior valor é {maior_valor} e está na posição {posicao} ")