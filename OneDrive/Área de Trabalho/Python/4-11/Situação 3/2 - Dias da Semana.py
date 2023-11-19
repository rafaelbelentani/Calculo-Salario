verde = "\033[4;92m"    #Seta a Cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[4;91m" #Seta a Cor Vermelha


while True: #Cria uma estrutura de Repetição
    print(" ") #Pula uma linha
    print("{}-{}".format(verde,reset)*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha

    print("Olá, seja Bem-Vindo ao Programa de Comparação de números") #Boas Vindas
    print(" ") #Pula uma linha

    print("\t Insira um número de 1 a 7") #Pede que usuario informe um numero de 1 a 7
    numero = int(input(" ")) #Armazena o numero informado na variavel


    if numero == 1: #Cria uma decisao - se o numero digitado for igual a 1
        print(" ") #Pula uma linha
        print("-"*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
        print("O número inserido se refere a {}Domingo{}".format(verde,reset)) #Informa o dia correpondente ao numero
        print(" ") #Pula uma linha
        print("{}-{}".format(vermelha,reset)*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
    elif numero == 2: #Cria uma decisao - se o numero digitado for igual a 2
        print(" ") #Pula uma linha
        print("-"*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
        print("O número inserido se refere a {}Segunda-Feira{}".format(verde,reset)) #Informa o dia correpondente ao numero
        print(" ") #Pula uma linha
        print("{}-{}".format(vermelha,reset)*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
    elif numero == 3: #Cria uma decisao - se o numero digitado for igual a 3
        print(" ") #Pula uma linha
        print("-"*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
        print("O número inserido se refere a {}Terça-Feira{}".format(verde,reset)) #Informa o dia correpondente ao numero
        print(" ") #Pula uma linha
        print("{}-{}".format(vermelha,reset)*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
    elif numero == 4: #Cria uma decisao - se o numero digitado for igual a 4
        print(" ") #Pula uma linha
        print("-"*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
        print("O número inserido se refere a {}Quarta-Feira{}".format(verde,reset)) #Informa o dia correpondente ao numero
        print(" ") #Pula uma linha
        print("{}-{}".format(vermelha,reset)*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
    elif numero == 5: #Cria uma decisao - se o numero digitado for igual a 5
        print(" ") #Pula uma linha
        print("-"*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
        print("O número inserido se refere a {}Quinta-Feira{}".format(verde,reset)) #Informa o dia correpondente ao numero
        print(" ") #Pula uma linha
        print("{}-{}".format(vermelha,reset)*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
    elif numero == 6: #Cria uma decisao - se o numero digitado for igual a 6
        print(" ") #Pula uma linha
        print("-"*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
        print("O número inserido se refere a {}Sexta-Feira{}".format(verde,reset)) #Informa o dia correpondente ao numero
        print(" ") #Pula uma linha
        print("{}-{}".format(vermelha,reset)*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
    elif numero == 7: #Cria uma decisao - se o numero digitado for igual a 7
        print(" ") #Pula uma linha
        print("-"*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
        print("O número inserido se refere a {}Sábado{}".format(verde,reset)) #Informa o dia correpondente ao numero
        print(" ") #Pula uma linha
        print("{}-{}".format(vermelha,reset)*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
    else: #Cria uma decisao - se o numero digitado for diferente 
        print(" ") #Pula uma linha
        print("-"*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
        print("Você Digitou um número inválido. \n{}Tente Novamente{}".format(vermelha,reset)) #Informa que o numero digitado é um numero invalido
        print(" ") #Pula uma linha
        print("{}-{}".format(vermelha,reset)*90) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha