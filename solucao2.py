numero1 = 0
numero2 = 1
soma = 0
numero_informado = int(input("Digite um número para verificar se ele faz parte da sequência de Fibonacci: "))

while numero_informado >= soma:
    
    if numero_informado == soma:
        print("O número informado faz parte da sequência de Fibonacci.")
        break

    soma = numero1 + numero2
    numero1 = numero2
    numero2 = soma

else:
    print("O número informado não faz parte da sequência de Fibonacci.")