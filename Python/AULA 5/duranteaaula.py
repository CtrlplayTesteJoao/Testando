'''numeros = [1,2,3,4,5,6,7,8,9,10]

for num in numeros:
    print(num)

for num in range(1,11,2):
    print(num)

for num in range(1,11):
    if (num %2 == 0):
        print(num)

for letra in "Ctrl+Play":
    print(letra)

soma = 0
numeros = range(1,1000)
i = 0
while soma < 100:
    soma = soma + numeros[i]
    i = i + 1
print(soma)
x = 0
while x < 5:
    print("valor de x: ", x)
    print("X ainda é menor do que 5, vamos somar 1")
    x = x + 1
else:
    print("FIM!")'''
 
soma = 0
x = 0
while x < 1000:
    x= x + 1
    if x%3 == 0:
        print(x)
        soma +=x
    else:
        if x%5 == 0:
            pass
        else:
            print('buscando...')
            continue
    if soma > 300:
        print(soma)
        break
