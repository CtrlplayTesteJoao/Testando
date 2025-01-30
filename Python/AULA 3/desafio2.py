N = [
    int(input("Digite o valor para a posição 0: ")),
    int(input("Digite o valor para a posição 1: ")),
    int(input("Digite o valor para a posição 2: ")),
    int(input("Digite o valor para a posição 3: ")),
    int(input("Digite o valor para a posição 4: ")),
    int(input("Digite o valor para a posição 5: ")),
    int(input("Digite o valor para a posição 6: ")),
    int(input("Digite o valor para a posição 7: ")),
    int(input("Digite o valor para a posição 8: ")),
    int(input("Digite o valor para a posição 9: "))
]

N[0],N[9] = N[9],N[0]
N[1],N[8] = N[8],N[1]
N[2],N[7] = N[7],N[2]
N[3],N[6] = N[6],N[3]
N[4],N[5] = N[5],N[4]

print(f"N[0] = {N[0]}")
print(f"N[1] = {N[1]}")
print(f"N[2] = {N[2]}")
print(f"N[3] = {N[3]}")
print(f"N[4] = {N[4]}")
print(f"N[5] = {N[5]}")
print(f"N[6] = {N[6]}")
print(f"N[7] = {N[7]}")
print(f"N[8] = {N[8]}")
print(f"N[9] = {N[9]}")