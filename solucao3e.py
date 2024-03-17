numero1 = 0
numero2 = 1

for i in range(7):
    soma = numero1 + numero2
    numero1 = numero2
    numero2 = soma

print(numero1)