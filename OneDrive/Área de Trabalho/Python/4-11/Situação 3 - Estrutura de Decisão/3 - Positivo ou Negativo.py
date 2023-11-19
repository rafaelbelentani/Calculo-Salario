verde = "\033[92m"    #Seta a Cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[91m" #Seta a Cor Vermelha
azul = "\033[34m" #Seta a Cor azul

print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha

print("Olá, seja Bem-Vindo ao Programa que informa se o número digitado é Positivo ou Negativo") #Boas Vindas
print(" ") #Pula uma linha

print("\t Insira um Número") #Pede que usuario informe qualquer numero
n1 = float(input(" ")) #Armazena o numero informado na variavel
print(" ") #Pula uma linha

if n1 > 0: #Cria uma condição - Se o numero for maior que zero
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t O Número Informado é {}POSITIVO{}".format(verde,reset)) #Informa ao usuario que o numero é positivo
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

elif n1 < 0: #Cria uma condição - Se o numero for menor que zero
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t O Número Informado é {}NEGATIVO{}".format(vermelha,reset)) #Informa ao usuario que o numero é negativo
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

else:  #Cria uma condição - Se o numero for igual a zero
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t O Número Informado é um número {}NEUTRO{}".format(azul,reset)) #Informa ao usuario que o numero é neutro
    print(" ") #Pula uma linha 
    print("-="*40) #Cria uma barra de inicialização do programa
