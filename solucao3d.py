contador = 0
numero = 1

while contador < 5:

    if numero % 2 == 0:
        potencia = numero**2
        contador += 1
    
    numero += 1

print(potencia)