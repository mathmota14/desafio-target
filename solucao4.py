interruptor = [1, 2, 3]
ordem = []

print("Para descobrir qual interruptor controla qual lâmpada iremos por partes, então vamos descobrir o da sala 1 primeiro")
print("Para isso, vamos ligar o interruptor 1 por 10 minutos, desligar e em seguida ligar o interruptor 2 e entrar na sala 1")
print("As opções possíveis são as seguintes:")
print("")
print("1. A lâmpada está quente")
print("2. A lâmpada está acesa")
print("3. A lâmpada não está nem quente nem acesa")
print("")

lampada_sala1 = int(input(("Escolha como está a lâmpada (1/2/3)? ")))
print(f"O interruptor {lampada_sala1} controla a lâmpada da sala 1!")
ordem.append(lampada_sala1)
interruptor.remove(lampada_sala1)

print("")
print("Nisso já se foi 1 ida. Para a segunda ida iremos descobrir o da segunda sala, onde automaticamente descobriremos o da terceira também")
print(f"Para isso vamos ligar o interruptor {interruptor[0]} e entrar na sala 2")
print("As opções possíveis são as seguintes:")
print("")
print("1. A lâmpada está ligada")
print("2. A lâmpada está desligada")
print("")

lampada_sala2 = int(input(("Escolha como está a lâmpada (1/2)? ")))

if lampada_sala2 == 1:
    print(f"O interruptor {interruptor[0]} controla a lâmpada da sala 2!")
    ordem.append(interruptor[0])
    interruptor.remove(interruptor[0])

elif lampada_sala2 == 2:
    print(f"O interruptor {interruptor[1]} controla a lâmpada da sala 2!")
    ordem.append(interruptor[1])
    interruptor.remove(interruptor[1])

ordem.append(interruptor[0])

print("")
print("Então descobrimos em duas idas que:")
print(f". O interruptor {ordem[0]} controla a lâmpada da sala 1")
print(f". O interruptor {ordem[1]} controla a lâmpada da sala 2")
print(f". O interruptor {ordem[2]} controla a lâmpada da sala 3")