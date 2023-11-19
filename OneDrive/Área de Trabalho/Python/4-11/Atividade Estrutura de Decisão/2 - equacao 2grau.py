verde = "\033[1;37;42m"    #Seta o fundo na cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[1;37;41m" #Seta o fundo na cor Vermelha


print("-="*40) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha

print("\t Olá, seja Bem-Vindo a Calculadora de Equação do Segundo Grau.") #Boas Vindas
print(" ") #Pula uma linha




print("\t Informe o valor de A: ") #Pede que o usuario informe o valor de A
a=int(input(" ")) #Armazena o valor digitado na variavel
print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa

if a == 0: #Cria uma condição - Se o valor de A for igual a Zero
    print("{} ERROR! A equação não é do Segundo Grau {}".format(vermelha,reset)) #Informa o erro ao usuario
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

else: #Cria uma condição
    print("\t Informe o valor de B: ") #Pede que o usuario informe o valor de B
    b=int(input(" ")) #Armazena o numero digitado na variavel
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa
    
    print("\t Informe o valor de C: ") #Pede que o usuario informe o valor de C
    c=int(input(" ")) #Armazena o numero digitado na variavel
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa

    print(" ") #Pula uma linha
    print("\t Sua Equação do Segundo Grau é: {} ({}x²) + ({}x) + {} {}".format(verde,a,b,c,reset)) #Informa a equação do Segundo Grau
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa


    delta = (b**2)-(4*a*c) #Realiza o Calculo do Delta

    if delta < 0: #Cria uma condição - Se delta for menor que Zero
        print(" ") #Pula uma linha
        print("\t A Equação não possui raízes reais") #Informa ao usuario que a equação não possui raizes reais
        print(" ") #Pula uma linha
        print("-="*40) #Cria uma barra de inicialização do programa
    elif delta == 0: #Cria uma condição - Se delta for igual a Zero
        print(" ") #Pula uma linha
        print("\t A Equaçã possui apenas um raíz real") #Informa ao usuario que a equação possui uma raiz real
        print(" ") #Pula uma linha
        print("-="*40) #Cria uma barra de inicialização do programa
    else: #Cria uma condição - Se delta for maior que Zero
        print(" ") #Pula uma linha
        print("\t\ A Equação possui duas raízes reais") #Informa ao usuario que a equação possui duas raizes reais
        print(" ") #Pula uma linha
        print("-="*40) #Cria uma barra de inicialização do programa