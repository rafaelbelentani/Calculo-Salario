print("-"*90) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha

print("Olá, seja Bem-Vindo ao Programa de Comparação de números") #Boas Vindas
print(" ") #Pula uma linha

print("\t Insira o primeiro numero") #Pede ao usuario que informe o primeiro numero
n1 = float(input(" ")) #Armazena o numero na variavel

print("\t Insira o segundo numero")#Pede ao usuario que informe o segundo numero
n2 = float(input(" ")) #Armazena o numero na variavel

print("\t Insira o terceiro numero")#Pede ao usuario que informe o terceiro numero
n3 = float(input(" ")) #Armazena o numero na variavel

if n1 > n2 and n1 > n3: #Cria uma decisao - se o primeiro numero for maior que o segundo e o terceiro
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("O Primeiro Número é o MAIOR") #Informa que o primeiro numero é o maior
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
elif n2 > n1 and n2 > n3:  #Cria uma decisao - se o segundo numero for maior que o primeiro e o terceiro
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("O Segundo Número é o MAIOR") #Informa que o segundo numero é o maior
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
elif n3 > n1 and n3 > n2: #Cria uma decisao - se o terceiro numero for maior que o primeiro e o segundo
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("O Terceiro Número é o MAIOR") #Informa que o terceiro numero é o maior
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
elif n1==n2 and n1!=n3: #Cria uma decisao - se o primeiro numero for igual ao segundo e diferente do terceiro
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("O Primeiro Número e o Segundo Número são os MAIORES e são IGUAIS") #Informa que o primeiro e o segundo numero são maiores e iguais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
elif n1==n3 and n1!=n2: #Cria uma decisao - se o primeiro numero for igual ao terceiro e diferente do segundo
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("O Primeiro Número e o Terceiro Número são os MAIORES e são IGUAIS") #Informa que o primeiro e o terceiro numero são maiores e iguais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
elif n2==n3 and n2!=n1: #Cria uma decisao - se o segundo numero for igual ao terceiro e diferente do primeiro
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("O Segundo Número e o Terceiro Número são os MAIORES e são IGUAIS") #Informa que o segundo e o terceiro numero são maiores e iguais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
if n1 < n2 and n1 < n3: #Cria uma decisao - se o primeiro numero for menor que o segundo e o terceiro
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("O Primeiro Número é o MENOR") #Informa que o primeiro numero é o menor
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
elif n2 < n1 and n2 < n3: #Cria uma decisao - se o segundo numero for menor que o primeiro e o terceiro
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("O Segundo Número é o MENOR") #Informa que o segundo numero é o menor
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
elif n3 < n1 and n3 < n2: #Cria uma decisao - se o terceiro numero for menor que o primeiro e o segundo
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("O Terceiro Número é o MENOR") #Informa que o terceiro numero é o menor
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
elif n1==n2 and n1!=n3: #Cria uma decisao - se o primeiro numero for igual ao segundo e diferente do terceiro
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("O Primeiro Número e o Segundo Número são os MENORES e são IGUAIS") #Informa que o primeiro e o segundo numero são menores e iguais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
elif n1==n3 and n1!=n2: #Cria uma decisao - se o primeiro numero for igual ao terceiro e diferente do segundo
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("O Primeiro Número e o Terceiro Número são os MENORES e são IGUAIS") #Informa que o primeiro e o terceiro numero são menores e iguais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
elif n2==n3 and n3!=n1:  #Cria uma decisao - se o segundo numero for igual ao terceiro e diferente do primeiro
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("O Segundo Número e o Terceiro Número são os MENORES e são IGUAIS") #Informa que o segundo e o terceiro numero são menores e iguais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
else:   #Cria uma decisao - se todos os numeros forem iguais
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("Os números são IGUAIS") #Informa que todos os numeros são iguais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa