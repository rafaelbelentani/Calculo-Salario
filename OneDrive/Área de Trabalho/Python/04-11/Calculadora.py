print("-"*90) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha


while True:
    print("\t Olá, seja Bem-Vindo a Calculadora") #Boas Vindas - Inicialização do programa
    print(" ") #Pula uma linha
    print('''[1] Soma
    [2] Subtração
    [3] Multiplicação
    [4] Divisão
    [5] Area de um Quadrado
    [6] Area de um Triangulo
    [7] Area de um Circulo''') #Informa ao usuário as opções oferecidas - as 3 aspas permite a utilização de strings em múltiplas linhas
    print(" ") #Pula uma linha
    print("\t Escolha uma opção") #Pergunta a opção desejada
    escolha = int(input("")) #Salva a escolha do usuario na variavel
    print(" ") #Pula uma linha

    if escolha == 1: #Cria uma condição - Se escolhar a opção 1
        print("Digite o primeiro número") #Pergunta o primeiro numero para realizar o calculo
        n1 = float(input("")) #Salva o numero na variavel
        print("Digite o segundo número") #Pergunta o segundo numero para realizar o calculo
        n2 = float(input("")) #Salva o numero na variavel
        calculo = n1 + n2 #Realiza o calculo
        calculo_r=round(calculo, 2) #Arredonda para 2 casas decimais
        print("-"*90) #Cria uma barra de separação
        print(" ") #Pula uma linha
        print("\t O Resultado é: {}".format(calculo_r)) #Informa o resultado
        print(" ") #Pula uma linha
        print("-"*90) #Cria uma barra de separação
       
    
    elif escolha == 2: #Cria uma condição - Se escolhar a opção 1
        print("Digite o primeiro número") #Pergunta o primeiro numero para realizar o calculo
        n1 = float(input("")) #Salva o numero na variavel
        print("Digite o segundo número") #Pergunta o segundo numero para realizar o calculo
        n2 = float(input("")) #Salva o numero na variavel
        calculo = n1 - n2 #Realiza o calculo
        calculo_r=round(calculo, 2) #Arredonda para 2 casas decimais
        print("-"*90) #Cria uma barra de separação
        print(" ") #Pula uma linha
        print("\t O Resultado é: {}".format(calculo_r)) #Informa o resultado
        print(" ") #Pula uma linha
        print("-"*90) #Cria uma barra de separação
    
    elif escolha == 3:
        print("Digite o primeiro número") #Pergunta o primeiro numero para realizar o calculo
        n1 = float(input("")) #Salva o numero na variavel
        print("Digite o segundo número") #Pergunta o segundo numero para realizar o calculo
        n2 = float(input("")) #Salva o numero na variavel
        calculo = n1 * n2 #Realiza o calculo
        calculo_r=round(calculo, 2) #Arredonda para 2 casas decimais
        print("-"*90) #Cria uma barra de separação
        print(" ") #Pula uma linha
        print("\t O Resultado é: {}".format(calculo_r)) #Informa o resultado
        print(" ") #Pula uma linha
        print("-"*90) #Cria uma barra de separação
    elif escolha == 4:
        print("Digite o primeiro número") #Pergunta o primeiro numero para realizar o calculo
        n1 = float(input("")) #Salva o numero na variavel
        print("Digite o segundo número") #Pergunta o segundo numero para realizar o calculo
        n2 = float(input("")) #Salva o numero na variavel
        if n2 != 0:
            calculo = n1 / n2 #Realiza o calculo
            calculo_r=round(calculo, 2) #Arredonda para 2 casas decimais
            print("-"*90) #Cria uma barra de separação
            print(" ") #Pula uma linha
            print("\t O Resultado é: {}".format(calculo_r)) #Informa o resultado
            print(" ") #Pula uma linha
            print("-"*90) #Cria uma barra de separação
        else:
            print("-"*90) #Cria uma barra de separação
            print(" ") #Pula uma linha
            print("Não é possível realizar a divisão por Zero! Tente Novamente") #Informa que o numero ecolhido é um numero invalido
            print(" ") #Pula uma linha
            print("-"*90)  #Cria uma barra de separação
        
    elif escolha == 5:
        print("Digite a Base do seu quadrado") #Pergunta o primeiro numero para realizar o calculo
        n1 = float(input("")) #Salva o numero na variavel
        print("Digite a Altura do seu quadrado") #Pergunta o segundo numero para realizar o calculo
        n2 = float(input("")) #Salva o numero na variavel
        calculo = n1 * n2 #Realiza o calculo
        calculo_r=round(calculo, 2) #Arredonda para 2 casas decimais
        print("-"*90) #Cria uma barra de separação
        print(" ") #Pula uma linha
        print("\t A Área do seu Quadrado é: {}".format(calculo_r)) #Informa o resultado
        print(" ") #Pula uma linha
        print("-"*90)  #Cria uma barra de separação
    
    elif escolha == 6:
        print("Digite a Base do seu quadrado") #Pergunta o primeiro numero para realizar o calculo
        n1 = float(input("")) #Salva o numero na variavel
        print("Digite a Altura do seu quadrado") #Pergunta o segundo numero para realizar o calculo
        n2 = float(input("")) #Salva o numero na variavel
        calculo = (n1 * n2)/2 #Realiza o calculo
        calculo_r=round(calculo, 2) #Arredonda para 2 casas decimais
        print("-"*90) #Cria uma barra de separação
        print(" ") #Pula uma linha
        print("\t A Área do seu Triangulo é: {}".format(calculo_r)) #Informa o resultado
        print(" ") #Pula uma linha
        print("-"*90) #Cria uma barra de separação
    
    elif escolha == 7:
        print("Digite a o Raio do seu Circulo") #Pergunta o primeiro numero para realizar o calculo
        n1 = float(input("")) #Salva o numero na variavel
        pi = 3.14
        calculo =  pi * n1 **2 #Realiza o calculo
        calculo_r=round(calculo, 2) #Arredonda para 2 casas decimais
        print("-"*90) #Cria uma barra de separação
        print(" ") #Pula uma linha
        print("\t A Área do seu Circulo é: {}".format(calculo_r)) #Informa o resultado
        print(" ") #Pula uma linha
        print("-"*90) #Cria uma barra de separação
    
    
    else:
        print("-"*90)  #Cria uma barra de separação
        print(" ") #Pula uma linha
        print("Você escolheu uma opção inválida. Tente Novamente") #Informa que a opção escolhida é uma opção inválida
        print(" ") #Pula uma linha
        print("-"*90)  #Cria uma barra de finalização