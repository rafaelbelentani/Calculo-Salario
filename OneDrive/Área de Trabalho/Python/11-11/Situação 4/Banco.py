verde="\033[1;42m"
vermelho="\033[1;41m"
reset="\033[0m"

print("=-"*40) #Cria uma barra de separação
print("") #pula uma linha

print("\t Seja Bem-Vindo ao seu Banco.")
print("") #pula uma linha
print("=-"*40) #Cria uma barra de separação

while True:
    try:
        print("\t Informe o dia do seu pagamento")
        dia=int(input(""))

        if dia <= 31:
            print("") #pula uma linha
            print("=-"*40) #Cria uma barra de separação
            break

        else:
            print("") #pula uma linha
            print("=-"*40) #Cria uma barra de separação
            print("\t {} Error! Informe o dia correto {} ".format(vermelho,reset))
            

    except ValueError:
        print("=-"*40) #Cria uma barra de separação
        print("") #pula uma linha
        print("{}\t  Error! Informe o dia correto {} ".format(vermelho,reset))



while True:
    try:
        print("\t Informe o seu Saldo.")
        saldo=float(input(""))
        print("") #pula uma linha
        print("=-"*40) #Cria uma barra de separação

        if saldo < 0:
            print("{}\t  Error! Informe o saldo correto {} ".format(vermelho,reset))
        else:
            break
    
    except ValueError:
        print("=-"*40) #Cria uma barra de separação
        print("") #pula uma linha
        print("{}\t  Error! Informe o saldo correto {} ".format(vermelho,reset))


repeticao=True

while repeticao:
    print("") #pula uma linha
    print("\t{} Seu saldo é de R${} {} ".format(verde,saldo,reset))
    print("") #pula uma linha
    if dia==31:
        dia=0
    
    while True:
        try:
            print("\t Qual valor foi gasto no dia {} ".format(dia+1))
            vg=float(input(" "))    
            print("") #pula uma linha
            print("=-"*40) #Cria uma barra de separação
            if vg< 0:
                print("{}\t  Error! Informe o saldo correto {} ".format(vermelho,reset))
            else:
                break

        except ValueError:
            print("=-"*40) #Cria uma barra de separação
            print("") #pula uma linha
            print("{}\t  Error! Informe o valor correto {} ".format(vermelho,reset))

    if saldo>=vg:
        saldo=saldo-vg
        dia = dia + 1


    else:
        print("") #pula uma linha
        print("\t{} SALDO INSUFICIENTE {} ".format(vermelho,reset))
        print("") #pula uma linha
        print("=-"*40) #Cria uma barra de separação
        

        menu = True
        while menu:
            try:
                print("\t Selecione uma opção")
                print('''\t    [1] Fazer uma Nova Compra
            [2] Fazer um Novo Deposito
            [3] Utilizar limite''')
                opcao=int(input(""))
                print("") #pula uma linha
                print("=-"*40) #Cria uma barra de separação
                

                if opcao == 1:
                    menu_novoSaldo=False
                elif opcao == 2:
                    menu_novoSaldo=True
                    while menu_novoSaldo:
                        try:
                            print("\t Informe o seu Novo Saldo.")
                            saldo2=float(input(""))
                            novosaldo = saldo+saldo2
                            print("") #pula uma linha
                            print("=-"*40) #Cria uma barra de separação
                            print("") #pula uma linha

                            if saldo2< 0:
                                print("{}\t  Error! Informe o saldo correto {} ".format(vermelho,reset))
                            else:            
                                while True:
                                    try:
                                        novosaldo>=0
                                        if dia==31:
                                            dia=0

                                        print("\t{} Seu saldo é de R${} {} ".format(verde,novosaldo,reset))
                                        print("\t Qual valor foi gasto no dia {} ".format(dia+1))
                                        vg=float(input(" "))    
                                        print("") #pula uma linha
                                        print("=-"*40) #Cria uma barra de separação
    
                                        if vg< 0:
                                            print("{}\t  Error! Informe o saldo correto {} ".format(vermelho,reset))
                                        else:
                                            if novosaldo>=vg:
                                                novosaldo=novosaldo-vg
                                                dia = dia + 1

                                            else:
                                                print("") #pula uma linha
                                                print("\t{} SALDO INSUFICIENTE {} ".format(vermelho,reset))
                                                print("") #pula uma linha
                                                print("=-"*40) #Cria uma barra de separação
                                                print("") #pula uma linha
                                                print("\t{} CONTA BLOQUEADA {} ".format(vermelho,reset))
                                                print("") #pula uma linha
                                                print("=-"*40) #Cria uma barra de separação
                                                opcao=False
                                                menu_novoSaldo=False
                                                menu=False                        
                                                repeticao=False
                                                break

                                    except ValueError:
                                        print("=-"*40) #Cria uma barra de separação
                                        print("") #pula uma linha
                                        print("{}\t  Error! Informe o valor correto {} ".format(vermelho,reset))
                    
                        except ValueError:
                            print("=-"*40) #Cria uma barra de separação
                            print("") #pula uma linha
                            print("{}\t  Error! Informe o valor correto {} ".format(vermelho,reset))
                    

                elif opcao == 3:
                    opcao3=True
                    while opcao3:
                        try:
                            print("\t Voce tem um limite pré aprovado de 50% do valor do seu Saldo.")
                            limite=saldo*0.5
                            saldolimite = saldo + limite
                            print("{} \t Seu Saldo é de R${} e seu novo limite é R${} {} ".format(verde,saldo,limite,reset))
                            print("{} \t Você tem um total de R${} {} ".format(vermelho,saldolimite,reset))
                            print("") #pula uma linha
                            print("=-"*40) #Cria uma barra de separação
                            print("") #pula uma linha


                            while saldolimite>=0:
                                if dia==31:
                                    dia=0
                                print("\t{} Seu saldo é de R${} {} ".format(verde,saldolimite,reset))
                                print("\t Qual valor foi gasto no dia {} ".format(dia+1))
                                vg=float(input(" "))    
                                print("") #pula uma linha
                                print("=-"*40) #Cria uma barra de separação
    

                                if saldolimite>=vg:
                                    saldolimite=saldolimite-vg
                                    dia = dia + 1


                                else:
                                    print("") #pula uma linha
                                    print("\t{} SALDO INSUFICIENTE {} ".format(vermelho,reset))
                                    print("") #pula uma linha
                                    print("=-"*40) #Cria uma barra de separação
                                    print("") #pula uma linha
                                    print("\t{} CONTA BLOQUEADA {} ".format(vermelho,reset))
                                    print("") #pula uma linha
                                    print("=-"*40) #Cria uma barra de separação
                                    repeticao=False
                                    menu=False
                                    opcao3=False
                                    break

                        except ValueError:
                            print("=-"*40) #Cria uma barra de separação
                            print("") #pula uma linha
                            print("{}\t  Error! Informe o valor correto {} ".format(vermelho,reset))  
            
            except ValueError:
                print("=-"*40) #Cria uma barra de separação
                print("") #pula uma linha
                print("{}\t  Error! Informe o valor correto {} ".format(vermelho,reset))