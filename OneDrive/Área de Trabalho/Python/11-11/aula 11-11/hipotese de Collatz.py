verde="\033[1;42m"
vermelho="\033[1;41m"
reset="\033[0m"
from time import sleep
numero = int(input("Digite um número: "))

while numero != 1:
    calculo = numero % 2
    if calculo == 0:
        numero = numero / 2
        print("{} Seu numero é = {} {}".format(verde,numero,reset))
        sleep(1)

    else:
        numero = (3*numero) + 1
        print("{} Seu numero é = {} {}".format(vermelho,numero,reset))
        sleep(1)

print("{} Seu numero é 0 {}".format(vermelho,reset))