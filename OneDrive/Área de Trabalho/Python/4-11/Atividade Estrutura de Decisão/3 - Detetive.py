verde = "\033[1;37;42m"    #Seta o fundo na cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[1;37;41m" #Seta o fundo na cor Vermelha
respostasPositivas = 0

print("-="*40) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha

print("\t Olá, seja Bem-Vindo ao Programa de Detetive.") #Boas Vindas
print(" ") #Pula uma linha

print("\t Nós vamos auxiliar a resolver um Crime com algumas Perguntas.") #Boas Vindas
print(" ") #Pula uma linha

print("\t Responda Apenas com SIM ou NÃO.") #Boas Vindas
print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha


print("\t Telefonou para a Vítima? ") #Pede que o usuario informe o valor de A
p1=input(" ") #Armazena o valor digitado na variavel
print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa

if p1 == "SIM" or p1 == "sim":
    respostasPositivas += 1 
    

print("\t Esteve no Local do Crime? ") #Pede que o usuario informe o valor de A
p2=input(" ") #Armazena o valor digitado na variavel
print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa

if p2 == "SIM" or p2 == "sim":
    respostasPositivas += 1


print("\t Mora perto da Vítima? ") #Pede que o usuario informe o valor de A
p3=input(" ") #Armazena o valor digitado na variavel
print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa

if p3 == "SIM" or p3 == "sim":
    respostasPositivas += 1


print("\t Devia para a Vítima? ") #Pede que o usuario informe o valor de A
p4=input(" ") #Armazena o valor digitado na variavel
print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa

if p4 == "SIM" or p4 == "sim":
    respostasPositivas += 1


print("\t Já trabalhou com a Vítima? ") #Pede que o usuario informe o valor de A
p5=input(" ") #Armazena o valor digitado na variavel
print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa

if p5 == "SIM" or p5 == "sim":
    respostasPositivas += 1


if respostasPositivas == 2:
    print(" ") #Pula uma linha
    print("\t Você é um {} SUSPEITO {}".format(verde,reset))
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

elif respostasPositivas >= 3 and respostasPositivas <= 4:
    print(" ") #Pula uma linha
    print("\t Você é um {} CÚMPLICE {}".format(verde,reset))
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

elif respostasPositivas == 5:
    print(" ") #Pula uma linha
    print("\t Você é um {} ASSASSINO {}".format(verde,reset))
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

else:
    print(" ") #Pula uma linha
    print("\t Você é {} INOCENTE {}".format(verde,reset))
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa