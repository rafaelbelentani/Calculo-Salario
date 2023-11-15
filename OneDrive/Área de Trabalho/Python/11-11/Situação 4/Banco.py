verde="\033[1;42m" #Seta a cor verde
vermelho="\033[1;41m" #seta a cor vermelha
reset="\033[0m" #Reseta as cores

print("=-"*40) #Cria uma barra de separação
print("") #pula uma linha

print("\t Seja Bem-Vindo ao seu Banco.") #Saudação/inicialiozação do programa
print("") #pula uma linha
print("=-"*40) #Cria uma barra de separação

while True: #Cria uma estrutura de repetição
    try: #Repete esse bloco de comandos até que o usuario informe um comando válido
        print("\t Informe o dia do seu pagamento") #Pede que o usuario informe o dia do pagamento
        dia=int(input("")) #Armazena o dia na variavel

        if dia <= 31 and dia > 0: #Cria uma decisão - se o numero for menor ou igual a 31 e maior que 0
            print("") #pula uma linha 
            print("=-"*40) #Cria uma barra de separação
            break #Interrompe a repetição

        else: #cria uma decisão - se o numero for maior que 31
            print("") #pula uma linha
            print("=-"*40) #Cria uma barra de separação
            print("\t {} Error! Informe o dia correto {} ".format(vermelho,reset)) #Informa um erro ao usuario
            

    except ValueError: #Cria uma mensagem de error caso for digitado um tipo de argumento que não seja o esperado
        print("=-"*40) #Cria uma barra de separação
        print("") #pula uma linha
        print("{}\t  Error! Informe o dia correto {} ".format(vermelho,reset)) #Informa um erro ao usuario



while True: #Cria uma estrutura de repetição
    try: #Repete esse bloco de comandos até que o usuario informe um comando válido
        print("\t Informe o seu Saldo.") #Pede que o usuario informe o Saldo
        saldo=float(input("")) #Armazena o Saldo na variavel
        print("") #pula uma linha
        print("=-"*40) #Cria uma barra de separação

        if saldo < 0: #Cria uma decisão - Se o valor do saldo for menor que zero
            print("{}\t  Error! Informe o saldo correto {} ".format(vermelho,reset)) #Informa um erro ao usuario
        else: #cria uma decisão - se o numero for maior que zero
            break #Interrompe a repetição
    
    except ValueError: #Cria uma mensagem de error caso for digitado um tipo de argumento que não seja o esperado
        print("=-"*40) #Cria uma barra de separação
        print("") #pula uma linha
        print("{}\t  Error! Informe o saldo correto {} ".format(vermelho,reset)) #Informa um erro ao usuario


repeticao=True #Cria a variavel do bloco de repetição de valores gasto nos dias subsequentes

while repeticao: #Cria uma estrutura de repetição
    print("") #pula uma linha
    print("\t{} Seu saldo é de R${} {} ".format(verde,saldo,reset)) #Informa o saldo para o cliente
    print("") #pula uma linha
    if dia==31: #Cria uma decisão - se o dia for igual a 31
        dia=0 #A variavel dia passa a ser 0
    
    while True: #Cria uma estrutura de repetição
        try: #Repete esse bloco de comandos até que o usuario informe um comando válido
            print("\t Qual valor foi gasto no dia {} ".format(dia+1)) #Pede para que o usuario informe o valor gasto no dia subsequente
            vg=float(input(" "))     #Armazena o valor gasto na variavel
            print("") #pula uma linha
            print("=-"*40) #Cria uma barra de separação
            if vg< 0: #Cria uma decisão - Se o valor informado for menor que zero
                print("{}\t  Error! Informe o saldo correto {} ".format(vermelho,reset)) #Informa um erro ao usuario e repete o bloco de comandos
            else: # Cria uma decisão - Se o valor for maior que zero
                break #Interrompe a repetição

        except ValueError:  #Cria uma mensagem de error caso for digitado um tipo de argumento que não seja o esperado
            print("=-"*40) #Cria uma barra de separação
            print("") #pula uma linha
            print("{}\t  Error! Informe o valor correto {} ".format(vermelho,reset)) #Informa um erro ao usuario
 
    if saldo>=vg: #Cria uma decisão - se o saldo for maior ou igual ao valor gasto
        saldo=saldo-vg #Realiza o calculo para saber o novo saldo
        dia = dia + 1 #Soma mais um dia


    else: #Cria uma decisão - Se o valor do saldo for menor que o valor gasto
        print("") #pula uma linha
        print("\t{} SALDO INSUFICIENTE {} ".format(vermelho,reset)) #Informa ao usuario que o saldo é insuficiente
        print("") #pula uma linha
        print("=-"*40) #Cria uma barra de separação
        

        menu = True #Cria a variavel do bloco de repetição do menu de seleção
        while menu: #Cria uma estutura de repetição
            try: #Repete esse bloco de comandos até que o usuario informe um comando válido
                print("\t Selecione uma opção")
                print('''\t    [1] Fazer uma Nova Compra
            [2] Fazer um Novo Deposito
            [3] Utilizar limite''') #Informa o menu ao usuario e pede que ele escolha uma opção
                opcao=int(input(""))  #armazena a opção escololhida na variavel
                print("") #pula uma linha
                print("=-"*40) #Cria uma barra de separação
            

                if opcao == 1: #Cria uma decisão - Se a opção escolhida for a 1
                    menu=False #Interrompe a estrutura de repetição do menu e volta para a estrutura de repetição do valor gasto


                elif opcao == 2: #Cria uma decisão - Se a opção escolhida for a 2
                    menu_novoSaldo=True #Cria a variavel para o bloco de repetição de valores gastos nos dias subsequentes
                    while menu_novoSaldo: #Cria uma estutura de repetição
                        try: #Repete esse bloco de comandos até que o usuario informe um comando válido
                            print("\t Informe o seu Novo Saldo.") #Pede que usuario informe o valor do novo saldo
                            saldo2=float(input("")) #Armazena o novo saldo na variavel
                            novosaldo = saldo+saldo2 #Realiza o calculo do saldo anterior mais o novo saldo
                            print("") #pula uma linha
                            print("=-"*40) #Cria uma barra de separação
                            print("") #pula uma linha

                            if saldo2< 0: #Cria uma condição - Se o valor do novo saldo for menor que zero
                                print("{}\t  Error! Informe o saldo correto {} ".format(vermelho,reset)) #Informa erro ao usuario
                            else: #Cria uma condição - Se o valor do novo saldo for maior que zero

                                while True: #Cria uma estutura de repetição
                                    try:  #Repete esse bloco de comandos até que o usuario informe um comando válido
                                        if dia==31: #Cria um condição - Se o dia for igual a 31
                                            dia=0 #Valor da variavel dia passa a ser zero
                                        print("\t{} Seu saldo é de R${} {} ".format(verde,novosaldo,reset)) #Informa ao usuario o valor do saldo
                                        print("\t Qual valor foi gasto no dia {} ".format(dia+1)) #Pede que o usuario informe o valor gasto no dia subsequente
                                        vg=float(input(" "))     #Armazena o valor na variavel
                                        print("") #pula uma linha
                                        print("=-"*40) #Cria uma barra de separação
    
                                        if vg< 0: #Cria uma condição - Se o valor gasto for menor que zero
                                            print("{}\t  Error! Informe o saldo correto {} ".format(vermelho,reset)) #Informa erro ao usuario
                                        else:#Cria uma condição - Se o valor gasto for maior que zero
                                            if novosaldo>=vg: #Cria uma condição - se o valor do saldo for maior ou igual ao valor gasto
                                                novosaldo=novosaldo-vg #Realiza o calculo do novo saldo
                                                dia = dia + 1 #Acrescenta mais um dia na variavel dia

                                            else: #Cria uma condição - se o valor do saldo for menor ao valor gasto
                                                print("") #pula uma linha
                                                print("\t{} SALDO INSUFICIENTE {} ".format(vermelho,reset)) #Informa erro ao usuario
                                                print("") #pula uma linha
                                                print("=-"*40) #Cria uma barra de separação
                                                print("") #pula uma linha
                                                print("\t{} CONTA BLOQUEADA {} ".format(vermelho,reset)) #Informa que a conta foi bloqueada e encerra o programa
                                                print("") #pula uma linha
                                                print("=-"*40) #Cria uma barra de separação
                                                menu_novoSaldo=False #Interrompe a repetição do bloco do novo saldo
                                                menu=False #Interrompe a repetição do bloco do menu
                                                repeticao=False #Interrompe a repetição do bloco de valores gasto
                                                break #Interrompe a repetição do bloco valores gasto do novo saldo

                                    except ValueError:  #Cria uma mensagem de error caso for digitado um tipo de argumento que não seja o esperado
                                        print("=-"*40) #Cria uma barra de separação
                                        print("") #pula uma linha
                                        print("{}\t  Error! Informe o valor correto {} ".format(vermelho,reset)) #Informa erro ao usuario e repete o bloco
                    
                        except ValueError: #Cria uma mensagem de error caso for digitado um tipo de argumento que não seja o esperado
                            print("=-"*40) #Cria uma barra de separação
                            print("") #pula uma linha
                            print("{}\t  Error! Informe o valor correto {} ".format(vermelho,reset)) #Informa erro ao usuario e repete o bloco
                    

                elif opcao == 3: #Cria uma decisão - Se a opção escolhida for a 3
                    opcao3=True #Cria uma variavel para o bloco de repetição do limite pré aprovado
                    while opcao3: #Cria uma estrutura de repetição
                        try: #Repete esse bloco de comandos até que o usuario informe um comando válido
                            print("\t Voce tem um limite pré aprovado de 50% do valor do seu Saldo.") #Informa ao usuario que ele tem um limite pré aprovado de 50% do valor do saldo
                            limite=saldo*0.5 #Realiza o calculo do limite
                            saldolimite = saldo + limite #Realiza o calculo do saldo + o limite
                            print("{} \t Seu Saldo é de R${} e seu novo limite é R${} {} ".format(verde,saldo,limite,reset)) #Informa ao usuario seu saldo e o limite
                            print("{} \t Você tem um total de R${} {} ".format(vermelho,saldolimite,reset)) #Informa ao usuario seu novo saldo
                            print("") #pula uma linha
                            print("=-"*40) #Cria uma barra de separação
                            print("") #pula uma linha


                            while saldolimite>=0: #Cria uma estrutura de repetição - se o limite for maior ou igual a zero
                                if dia==31: #Cria uma condição - se o dia for igual a 31
                                    dia=0 #Valor da variavel dia passa a ser zero
                                print("\t{} Seu saldo é de R${} {} ".format(verde,saldolimite,reset)) #Informa ao usuario seu saldo
                                print("\t Qual valor foi gasto no dia {} ".format(dia+1)) #Pede que o usuario informe o valor gasto no dia subsequente
                                vg=float(input(" "))     #Armazena o valor na variavel
                                print("") #pula uma linha
                                print("=-"*40) #Cria uma barra de separação
    
                                if vg< 0: #Cria uma condição - Se o valor gasto for menor que zero
                                    print("{}\t  Error! Informe o saldo correto {} ".format(vermelho,reset)) #Informa erro ao usuario
                                else:#Cria uma condição - Se o valor gasto for maior que zero
                                    if saldolimite>=vg: #Cria uma condição - Se o valor for maior ou igual ao saldo
                                        saldolimite=saldolimite-vg #Realiza o calculo do saldo
                                        dia = dia + 1 #soma mais um dia na variavel dia


                                    else: #Cria uma condição - Se o valor for menor ao saldo
                                        print("") #pula uma linha
                                        print("\t{} SALDO INSUFICIENTE {} ".format(vermelho,reset)) #Informa que o saldo é insuficiente
                                        print("") #pula uma linha
                                        print("=-"*40) #Cria uma barra de separação
                                        print("") #pula uma linha
                                        print("\t{} CONTA BLOQUEADA {} ".format(vermelho,reset)) #Informa que a conta foi Bloqueada e termina o programa
                                        print("") #pula uma linha
                                        print("=-"*40) #Cria uma barra de separação
                                        repeticao=False #Interrompe o bloco de repetição de valores gastos
                                        menu=False  #Interrompe o bloco de repetição do menu
                                        opcao3=False #Interrompe o bloco de repetição de limite
                                        break #Interrompe o bloco de repetição o valor gasto do limite

                        except ValueError:#Cria uma mensagem de error caso for digitado um tipo de argumento que não seja o esperado
                            print("=-"*40) #Cria uma barra de separação
                            print("") #pula uma linha
                            print("{}\t  Error! Informe o valor correto {} ".format(vermelho,reset))   #Informa erro ao usuario e repete o bloco
            
            except ValueError: #Cria uma mensagem de error caso for digitado um tipo de argumento que não seja o esperado
                print("=-"*40) #Cria uma barra de separação
                print("") #pula uma linha
                print("{}\t  Error! Informe o valor correto {} ".format(vermelho,reset)) #Informa erro ao usuario e repete o bloco