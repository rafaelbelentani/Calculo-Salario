verde = "\033[4;92m"    #Seta a Cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[91m" #Seta a Cor Vermelha


import datetime     #Importa a data e a hora atual
data = datetime.datetime.now() #Armazena a data e a hora atual na variavel
formato = "%d-%m-%Y %H:%M" #Define o formato da data e da hora
dataformatada = data.strftime(formato) #armazena a data formatada na variavel

Skol = 2.95 #armazena o valor na variavel
Brahma = 2.79 #armazena o valor na variavel
Antarctica = 2.55 #armazena o valor na variavel
Heineken = 6.90 #armazena o valor na variavel
Smirnoff = 44.50 #armazena o valor na variavel
Absolut = 96.90 #armazena o valor na variavel
Ciroc = 158.40 #armazena o valor na variavel
Coca = 2.49 #armazena o valor na variavel
Sprite = 2.65 #armazena o valor na variavel
Fanta = 2.99 #armazena o valor na variavel
Red = 63.25 #armazena o valor na variavel
Black = 139.90 #armazena o valor na variavel
Jack = 162.99 #armazena o valor na variavel

print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90)   #Cria uma barra de inicialização do programa
print("") #Pula uma linha

print('''\t [1] Cerveja
\t [2] Refrigerante
\t [3] Vodka
\t [4] Whisky   
''') #Mostra ao usuário as opções de escolha  - as 3 aspas permite a utilização de strings em múltiplas linhas
print("\t Selecione a opção desejada") #Pede ao usuário que escolha as opções
opcao=input("") #Armazena a opção na variavel
print("-"*90)   #Cria uma barra de inicialização do programa
print("") #Pula uma linha

if opcao == "1": #Cria uma condição - Se escolheu a opção 1 Cervveja
    print("Voce escolheu a opção 1 Cerveja. Aqui estão as cervejas disponíveis")
    print('''\t [1] Skol
\t [2] Brahma
\t [3] Antarctica
\t [4] Heineken
''') #Mostra ao usuário as opções de escolha - as 3 aspas permite a utilização de strings em múltiplas linhas
    
    print("\t Selecione a opção desejada") #Pede ao usuário que escolha as opções
    opcao2=input("") #Armazena a opção na variavel
    print("-"*90)   #Cria uma barra de inicialização do programa
    print("") #Pula uma linha


    if opcao2 == "1": #Cria uma condição - Se escolheu a opção 1 Skol
        print("\t Voce escolheu a opção 1 Skol. \n \t A unidade sai {}{}{} \n \t Acima de 10 unidades tem {}10% de desconto{}".format(verde,Skol,reset,vermelha,reset)) #Informa a opção escolhida e oferece desconto
        print("\t Quantas unidades voce deseja?") #Pergunta ao usuário quantas unidades ele pretende comprar
        unidade=int(input("")) #Armazena a quantidade na variavel

        if unidade>10: #Cria uma condição - Se comprar acima de 10 unidades ele obtem desconto de 10%
            precototal=unidade*Skol  #Realiza o Calculo total
            desconto=precototal*0.10 #Realiza o calculo do desconto
            precofinal=precototal-desconto #Realiza o calculo final com desconto
            preco_r=round(precofinal, 2) #Arredonda as casas decimais
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("\t O valor Total é {}R${}{}".format(verde,preco_r,reset)) #Informa o valor total
            print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("") #Pula uma linha

        else: #Cria uma condição - Se não houver o desconto
            preco=unidade*Skol #Realiza o Calculo total
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("\t O valor Total é {}R${}{}".format(verde,preco,reset)) #Informa o valor total
            print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("") #Pula uma linha


    elif opcao2 == "2": #Cria uma condição - Se escolheu a opção 2 Brahma
        print("\t Voce escolheu a opção 2 Brahma. \n \t A unidade sai {}{}{} \n \t Acima de 10 unidades tem {}10% de desconto{}".format(verde,Brahma,reset,vermelha,reset)) #Informa a opção escolhida e oferece desconto
        print("\t Quantas unidades voce deseja?") #Pergunta ao usuário quantas unidades ele pretende compra
        unidade=int(input("")) #Armazena a quantidade na variavel

        if unidade>10: #Cria uma condição - Se comprar acima de 10 unidades ele obtem desconto de 10%
            precototal=unidade*Brahma  #Realiza o Calculo total
            desconto=precototal*0.10 #Realiza o calculo do desconto
            precofinal=precototal-desconto #Realiza o calculo final com desconto
            preco_r=round(precofinal, 2) #Arredonda as casas decimais
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("\t O valor Total é {}R${}{}".format(verde,preco_r,reset)) #Informa o valor total
            print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("") #Pula uma linha

        else: #Cria uma condição - Se não houver o desconto
            preco=unidade*Brahma #Realiza o Calculo total
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("\t O valor Total é {}R${}{}".format(verde,preco,reset)) #Informa o valor total
            print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("") #Pula uma linha

    elif opcao2 == "3": #Cria uma condição - Se escolheu a opção 3 Antarctica
        print("\t Voce escolheu a opção 3 Antarctica. \n \t A unidade sai {}{}{} \n \t Acima de 10 unidades tem {}10% de desconto{}".format(verde,Antarctica,reset,vermelha,reset)) #Informa a opção escolhida e oferece desconto
        print("\t Quantas unidades voce deseja?") #Pergunta ao usuário quantas unidades ele pretende compra
        unidade=int(input("")) #Armazena a quantidade na variavel
 
        if unidade>10: #Cria uma condição - Se comprar acima de 10 unidades ele obtem desconto de 10%
            precototal=unidade*Antarctica  #Realiza o Calculo total
            desconto=precototal*0.10 #Realiza o calculo do desconto
            precofinal=precototal-desconto #Realiza o calculo final com desconto
            preco_r=round(precofinal, 2) #Arredonda as casas decimais
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("\t O valor Total é {}R${}{}".format(verde,preco_r,reset)) #Informa o valor total
            print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("") #Pula uma linha

        else: #Cria uma condição - Se não houver o desconto
            preco=unidade*Antarctica #Realiza o Calculo total
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("\t O valor Total é {}R${}{}".format(verde,preco,reset)) #Informa o valor total
            print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("") #Pula uma linha

    elif opcao2 == "4": #Cria uma condição - Se escolheu a opção 4 Heineken
        print("\t Voce escolheu a opção 4 Heineken. \n \t A unidade sai {}{}{} \n \t Acima de 10 unidades tem {}10% de desconto{}".format(verde,Heineken,reset,vermelha,reset)) #Informa a opção escolhida e oferece desconto
        print("\t Quantas unidades voce deseja?") #Pergunta ao usuário quantas unidades ele pretende compra
        unidade=int(input("")) #Armazena a quantidade na variavel

        if unidade>10: #Cria uma condição - Se comprar acima de 10 unidades ele obtem desconto de 10%
            precototal=unidade*Heineken  #Realiza o Calculo total
            desconto=precototal*0.10 #Realiza o calculo do desconto
            precofinal=precototal-desconto #Realiza o calculo final com desconto
            preco_r=round(precofinal, 2) #Arredonda as casas decimais
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("\t O valor Total é {}R${}{}".format(verde,preco_r,reset)) #Informa o valor total
            print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("") #Pula uma linha

        else: #Cria uma condição - Se não houver o desconto
            preco=unidade*Heineken #Realiza o Calculo total
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("\t O valor Total é {}R${}{}".format(verde,preco,reset)) #Informa o valor total
            print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
            print("-"*90)   #Cria uma barra de inicialização do programa
            print("") #Pula uma linha

    else: #Cria uma condição
        print("{}\t Opção Inválida. Tente Novamente{}".format(vermelha,reset)) #Informa se o usuario escolher uma opção invalida
        print("") #Pula uma linha
        print("-"*90)   #Cria uma barra de inicialização do programa



elif opcao == "2": #Cria uma condição - Se o usuario escolher a opção 2 Refrigerantes
    print("Voce escolheu a opção 2 Refrigerante. Aqui estão os Refrigerantes disponíveis")
    print('''\t [1] Coca-Colka
\t [2] Sprite
\t [3] Fanta
''') #Mostra ao usuário as opções de escolha  - as 3 aspas permite a utilização de strings em múltiplas linhas
    print("\t Selecione a opção desejada") #Pede ao usuario escolher as opções
    opcaoRefri=input("") #Armazena a escolha na variavel
    print("-"*90)   #Cria uma barra de inicialização do programa
    print("") #Pula uma linha

    if opcaoRefri == "1": #Cria uma condição - Se escolher a opção 1 Coca Cola
        print("\t Voce escolheu a opção 1 Coca-Cola. \n \t A unidade sai {}{}{} ".format(verde,Coca,reset)) #Informa a opção escolhida
        print("\t Quantas unidades voce deseja?") #Pede ao usuario informar a quantidade desejada
        unidade=int(input("")) #Armazena a quantidade na variavel

        precoRefri=unidade*Coca #Realiza o calculo total
        precoRefri_r=round(precoRefri, 2) #Arredonda as casas decimais
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("\t O valor Total é {}R${}{}".format(verde,precoRefri_r,reset)) #Informa o valor total ao usuario
        print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("") #Pula uma linha

    elif opcaoRefri == "2": #Cria uma condição - Se escolher a opção 2 Sprite
        print("\t Voce escolheu a opção 2 Sprite. \n \t A unidade sai {}{}{} ".format(verde,Sprite,reset)) #Informa a opção escolhida
        print("\t Quantas unidades voce deseja?") #Pede ao usuario informar a quantidade desejada
        unidade=int(input("")) #Armazena a quantidade na variavel

        precoRefri=unidade*Sprite #Realiza o calculo total
        precoRefri_r=round(precoRefri, 2) #Arredonda as casas decimais
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("\t O valor Total é {}R${}{}".format(verde,precoRefri_r,reset)) #Informa o valor total ao usuario
        print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("") #Pula uma linha


    elif opcaoRefri == "3": #Cria uma condição - Se escolher a opção 3 Fanta
        print("\t Voce escolheu a opção 3 Fanta. \n \t A unidade sai {}{}{} ".format(verde,Fanta,reset)) #Informa a opção escolhida
        print("\t Quantas unidades voce deseja?") #Pede ao usuario informar a quantidade desejada
        unidade=int(input("")) #Armazena a quantidade na variavel

        precoRefri=unidade*Fanta #Realiza o calculo total
        precoRefri_r=round(precoRefri, 2) #Arredonda as casas decimais
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("\t O valor Total é {}R${}{}".format(verde,precoRefri_r,reset)) #Informa o valor total ao usuario
        print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("") #Pula uma linha


    else: #Cria uma Condição
        print("{}\t Opção Inválida. Tente Novamente{}".format(vermelha,reset)) #Informa se o usuario escolher uma opção invalida
        print("") #Pula uma linha
        print("-"*90)   #Cria uma barra de inicialização do programa


elif opcao == "3": #Cria uma condição - Se escolheu a opção 3 Vodka
    print("Voce escolheu a opção 3 Vodka. Aqui estão as Vodkas disponíveis") #Informa a opção escolhida
    print('''\t [1] Smirnoff
\t [2] Absolut
\t [3] Ciroc
''') #Informa as opções disponiveis
    print("\t Selecione a opção desejada") #Pede para que o usuario informe a opção desejada
    opcaoVodka=input("") #Armazena a opção na variavel
    print("-"*90)   #Cria uma barra de inicialização do programa
    print("") #Pula uma linha

    if opcaoVodka == "1": #Cria uma condição - Se escolheu a opção 1 Smirnoff
        print("\t Voce escolheu a opção 1 Smirnoff. \n \t A unidade sai {}{}{} ".format(verde,Smirnoff,reset)) #Informa a opção escolhida
        print("\t Quantas unidades voce deseja?") #Pede para o usuario informar a quantidade desejada
        unidade=int(input("")) #Armazena a qunatidade na variavel

        precoRefri=unidade*Smirnoff #Realiza o Calculo total
        precoRefri_r=round(precoRefri, 2) #Arredonda as casas decimais
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("\t O valor Total é {}R${}{}".format(verde,precoRefri_r,reset)) #Informa o valor total
        print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("") #Pula uma linha

    elif opcaoVodka == "2": #Cria uma condição - Se escolheu a opção 2 Absolut
        print("\t Voce escolheu a opção 2 Absolut. \n \t A unidade sai {}{}{} ".format(verde,Absolut,reset)) #Informa a opção escolhida
        print("\t Quantas unidades voce deseja?") #Pede para o usuario informar a quantidade desejada
        unidade=int(input("")) #Armazena a qunatidade na variavel

        precoRefri=unidade*Absolut #Realiza o Calculo total
        precoRefri_r=round(precoRefri, 2) #Arredonda as casas decimais
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("\t O valor Total é {}R${}{}".format(verde,precoRefri_r,reset)) #Informa o valor total
        print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("") #Pula uma linha

    elif opcaoVodka == "3": #Cria uma condição - Se escolheu a opção 3 Ciroc
        print("\t Voce escolheu a opção 3 Ciroc. \n \t A unidade sai {}{}{} ".format(verde,Ciroc,reset)) #Informa a opção escolhida
        print("\t Quantas unidades voce deseja?") #Pede para o usuario informar a quantidade desejada
        unidade=int(input("")) #Armazena a quantidade na variavel

 
        precoRefri=unidade*Ciroc #Realiza o Calculo total
        precoRefri_r=round(precoRefri, 2) #Arredonda as casas decimais
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("\t O valor Total é {}R${}{}".format(verde,precoRefri_r,reset)) #Informa a opção escolhida
        print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("") #Pula uma linha

    else: #Cria uma condição
        print("{}\t Opção Inválida. Tente Novamente{}".format(vermelha,reset)) #Informa se o usuario escolher uma opção invalida
        print("") #Pula uma linha
        print("-"*90)   #Cria uma barra de inicialização do programa

 
elif opcao == "4": #Cria uma condição - Se escolheu a opção 4 Whisky
    print("Voce escolheu a opção 4 Whisky. Aqui estão as cervejas disponíveis") #Informa ao usuario a opção escolhida
    print('''\t [1] Red Label
\t [2] Black Label
\t [3] Jack Daniels
''') #Informa as opções disponíveis
    print("\t Selecione a opção desejada") #Pede para o usuario informar a quantidade desejada
    opcaoVodka=input("")  #Armazena a opção escolhida na variavel
    print("-"*90)   #Cria uma barra de inicialização do programa
    print("") #Pula uma linha

    if opcaoVodka == "1": #Cria uma condição - se escolheu a opção 1 Red Label
        print("\t Voce escolheu a opção 1 Red Label. \n \t A unidade sai {}{}{} ".format(verde,Red,reset)) #Informa ao usuario a opção escolhida
        print("\t Quantas unidades voce deseja?") #Pede para o usuario informar a quantidade
        unidade=int(input("")) #Armazena a quantidade escolhida na variavel

        precoRefri=unidade*Red  #Realiza o Calculo total
        precoRefri_r=round(precoRefri, 2) #Arredonda as casas decimais
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("\t O valor Total é {}R${}{}".format(verde,precoRefri_r,reset)) #Informa a opção escolhida
        print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("") #Pula uma linha

    elif opcaoVodka == "2": #Cria uma condição - se escolheu a opção 2 Black Label
        print("\t Voce escolheu a opção 2 Black Label. \n \t A unidade sai {}{}{} ".format(verde,Black,reset)) #Informa ao usuario a opção escolhida
        print("\t Quantas unidades voce deseja?") #Pede para o usuario informar a quantidade
        unidade=int(input("")) #Armazena a quantidade escolhida na variavel

        precoRefri=unidade*Black  #Realiza o Calculo total
        precoRefri_r=round(precoRefri, 2) #Arredonda as casas decimais
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("\t O valor Total é {}R${}{}".format(verde,precoRefri_r,reset)) #Informa a opção escolhida
        print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("") #Pula uma linha

    elif opcaoVodka == "3": #Cria uma condição - se escolheu a opção 3 Jack Daniels
        print("\t Voce escolheu a opção 3 Jack Daniels. \n \t A unidade sai {}{}{} ".format(verde,Jack,reset)) #Informa ao usuario a opção escolhida
        print("\t Quantas unidades voce deseja?") #Pede para o usuario informar a quantidade
        unidade=int(input("")) #Armazena a quantidade escolhida na variavel
 
        precoRefri=unidade*Jack #Realiza o Calculo total
        precoRefri_r=round(precoRefri, 2) #Arredonda as casas decimais
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("\t O valor Total é {}R${}{}".format(verde,precoRefri_r,reset)) #Informa a opção escolhida
        print("Seu pedido foi registrado {}{}{} e chegará em até 40 minutos. Obrigado".format(verde,dataformatada,reset)) #Informa o registro do pedido com a data e hora
        print("-"*90)   #Cria uma barra de inicialização do programa
        print("") #Pula uma linha

    else: #Cria uma condição
        print("{}\t Opção Inválida. Tente Novamente{}".format(vermelha,reset)) #Informa se o usuario escolher uma opção invalida
        print("") #Pula uma linha
        print("-"*90)   #Cria uma barra de inicialização do programa

else: #Cria uma condição
        print("{}\t Opção Inválida. Tente Novamente{}".format(vermelha,reset)) #Informa se o usuario escolher uma opção invalida
        print("") #Pula uma linha
        print("-"*90)   #Cria uma barra de finalização do programa

