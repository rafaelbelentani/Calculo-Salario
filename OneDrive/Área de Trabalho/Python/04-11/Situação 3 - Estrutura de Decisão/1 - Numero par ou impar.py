verde = "\033[4;92m"    #Seta a Cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[4;91m" #Seta a Cor Vermelha

print(" ") #Pula uma linha
print("-"*90) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha

print("Olá, seja Bem-Vindo ao Programa que informa se um número é par ou ímpar") #Boas Vindas
print(" ") #Pula uma linha

print("\t Insira qualquer número") #Pede que usuario informe qualquer numero
numero = float(input(" ")) #Armazena o numero informado na variavel

calculo = numero % 2 #Realiza o calculo

if calculo == 0: #Se o resto da divisão for igual a zero, o numero é par
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Seu numero é {}PAR{}".format(verde,reset)) #Informa o resultado ao usuario
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
else: #Se não.O resto da divisão for diferente de zero, o numero é impar
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Seu numero é {}IMPAR{}".format(verde,reset)) #Informa o resultado ao usuario
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa