verde = "\033[1;37;42m"    #Seta o fundo na cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[91m" #Seta a Cor Vermelha
azul = "\033[34m" #Seta a Cor Vermelha

print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha

print("Olá, seja Bem-Vindo ao Programa, vamos te auxliar a comprar o melhor produto") #Boas Vindas
print(" ") #Pula uma linha

print("\t Insira o Primeiro Produto") #Pede que usuario informe qualquer produto
p1 = input(" ") #Armazena o produto informada na variavel
print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa

print("\t Insira o Valor do Primeiro Produto") #Pede que usuario informe qualquer produto
v1 = input("R$ ") #Armazena o valor do produto informado na variavel
print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa

print("\t Insira o Segundo Produto") #Pede que usuario informe qualquer produto
p2 = input(" ") #Armazena o produto informada na variavel
print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa

print("\t Insira o Valor do Segundo Produto") #Pede que usuario informe qualquer produto
v2 = input("R$ ") #Armazena o valor do produto informado na variavel
print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa

print("\t Insira o Terceiro Produto") #Pede que usuario informe qualquer produto
p3 = input(" ") #Armazena o produto informada na variavel
print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa

print("\t Insira o Valor do Terceiro Produto") #Pede que usuario informe qualquer produto
v3 = input("R$ ") #Armazena o valor do produto informado na variavel
print(" ") #Pula uma linha

if v1<v2 and v1<v3: #Cria uma Condição - Se o primeiro produto for menor que o segundo e o terceiro
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t{} Voce deve comprar o produto {} {}".format(verde,p1,reset)) #informa que o usuario deve comprar primeiro produro
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

elif v1==v2 and v1<v3: #Cria uma Condição - Se o primeiro e o segundo produto forem iguais e menor que o terceiro
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t{} Voce deve comprar os produtos: {} e {} {}".format(verde,p1,p2,reset)) #informa que o usuario deve comprar primeiro e o segundo produro
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

elif v1==v3 and v1<v2: #Cria uma Condição - Se o primeiro e o terceiro produto forem iguais e menor que o segundo
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t{} Voce deve comprar os produtos: {} e {} {}".format(verde,p1,p3,reset)) #informa que o usuario deve comprar primeiro e o terceiro produro
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

elif v2==v3 and v2<v1: #Cria uma Condição - Se o segundo e o terceiro produto forem iguais e menor que o primeiro
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t{} Voce deve comprar os produtos: {} e {} {}".format(verde,p2,p3,reset)) #informa que o usuario deve comprar segundo e o terceiro produro
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

else: #Cria uma Condição - Se os produtos tiverem o mesmo valor
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t{} Os Tres produtos tem o mesmo Valor {}".format(verde,reset)) #informa que o usuario deve comprar segundo e o terceiro produro
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa