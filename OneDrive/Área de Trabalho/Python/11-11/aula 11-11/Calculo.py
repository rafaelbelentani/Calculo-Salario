numero = int(input("Digite um número: "))

while numero != 0:
    calculo = numero % 2
    if calculo == 0:
        numero = numero / 2
        print("Seu numero é = {}".format(numero))
        

    else:
        numero = numero - 1
        print("Seu numero é = {}".format(numero))
        