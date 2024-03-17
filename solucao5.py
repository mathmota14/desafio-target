palavra = input("Digite uma palavra que será invertida: ")
invertido = []

for i in range(len(palavra)):
    invertido.append(palavra[-(i+1)])

print("A palavra invertida é", ''.join(invertido))