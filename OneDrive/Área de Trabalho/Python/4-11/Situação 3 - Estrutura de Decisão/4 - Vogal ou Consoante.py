verde = "\033[1;37;42m"    #Seta o fundo na cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[91m" #Seta a Cor Vermelha
azul = "\033[34m" #Seta a Cor Vermelha

print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha

print("Olá, seja Bem-Vindo ao Programa que informa se a letra digitada é uma Vogal ou Consoante") #Boas Vindas
print(" ") #Pula uma linha

print("\t Insira uma Letra") #Pede que usuario informe qualquer letra
letra = input(" ") #Armazena a letra informada na variavel
print(" ") #Pula uma linha


if letra.lower()=='a' or letra.lower()=='e' or letra.lower()=='i' or letra.lower()=='o' or letra.lower()=='u': #Cria uma condição - Se a letra for uma Vogal(a, e, i, o ou u)
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t{} A Letra Digitada é uma VOGAL {}".format(verde,reset)) #Informa ao usuario que a letra é uma vogal
    print(" ") #Pula uma linha 
    print("-="*40) #Cria uma barra de inicialização do programa



else: #Cria uma condição - Se a letra não for uma vogal
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t{} A Letra Digitada é uma CONSOANTE {}".format(verde,reset)) #Informa ao usuario que a letra é uma consoante
    print(" ") #Pula uma linha 
    print("-="*40) #Cria uma barra de inicialização do programa