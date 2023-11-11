print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha

print("Olá, seja Bem-Vindo ao Programa que informa o Maior Número Inserido") #Boas Vindas
print(" ") #Pula uma linha

print("\t Insira o primeiro número") #Pede que usuario informe qualquer numero
n1 = float(input(" ")) #Armazena o numero informado na variavel
print(" ") #Pula uma linha

print("-="*40) #Cria uma barra de inicialização do programa
print("\t Insira o segundo número") #Pede que usuario informe qualquer numero
n2 = float(input(" ")) #Armazena o numero informado na variavel
print(" ") #Pula uma linha

print("-="*40) #Cria uma barra de inicialização do programa
print("\t Insira o segundo número") #Pede que usuario informe qualquer numero
n3 = float(input(" ")) #Armazena o numero informado na variavel
print(" ") #Pula uma linha

if n1>n2 and n1>n3: #Cria uma Condição - Se o n1 for maior que o n2 e o n3
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t O Primeiro Número Digitado ({}) é o maior".format(n1)) #Informa que o n1 é o maior numero
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

elif n1==n2 and n1>n3: #Cria uma Condição - Se o n1 for igual ao n2 e n1 maior que n3
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t O Primeiro e o Segundo Número Digitado ({}) são MAIORES e IGUAIS".format(n1)) #Informa que o n1 e n2 são iguais e maiores
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

elif n1==n3 and n1>n2: #Cria uma Condição - Se o n1 for igual ao n3 e n1 maior que n2
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t O Primeiro e o Terceiro Número Digitado ({}) são MAIORES e IGUAIS".format(n1)) #Informa que o n1 e n3 são iguais e maiores
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

elif n2>n1 and n2>n3: #Cria uma Condição - Se o n2 for maior que o n1 e o n3
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t O Segundo Número Digitado ({}) é o maior".format(n2)) #Informa que o n2 é o maior numero
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

elif n2==n3 and n2>n1: #Cria uma Condição - Se o n2 for igual ao n3 e n1 maior que n1
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t O Segundo e o Terceiro Número Digitado ({}) são MAIORES e IGUAIS".format(n2)) #Informa que o n2 e n3 são iguais e maiores
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

elif n3>n1 and n3>n2: #Cria uma Condição - Se o n3 for maior que o n1 e o n2
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t O Terceiro Número Digitado ({}) é o maior".format(n3)) #Informa que o n3 é o maior numero
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

else:  #Cria uma Condição - Se os numeros forem iguais
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Os Números são Iguais") #Informa os numeros são iguais
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa