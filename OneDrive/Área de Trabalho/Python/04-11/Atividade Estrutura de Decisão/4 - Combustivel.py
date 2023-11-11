verde = "\033[1;37;42m"    #Seta o fundo na cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[1;37;41m" #Seta o fundo na cor Vermelha
respostasPositivas = 0 #Variavel para armazenar quantidade de respostas positivas
alcool = 2.21 #Variavel para armazenar o preço do combustivel
gasolina = 5.82 #Variavel para armazenar o preço do combustivel

print("-="*40) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha

print("\t Olá, seja Bem-Vindo ao Programa de Desconto de Combustivel.") #Boas Vindas
print(" ") #Pula uma linha

print('''
            Nossos Valores são:
{}          Álcool = R$ 2,21                   {}
{}      Até 20 litros = 3% de desconto         {}
{}      Acima de 20 litros = 5% de desconto    {}
{}          Gasolina = R$5,82                  {}
{}      Até 20 litros = 4% de desconto         {}
{}      Acima de 20 litros = 6% de desconto    {}
      '''.format(verde,reset,verde,reset,verde,reset,vermelha,reset,vermelha,reset,vermelha,reset)) #Informa o preço e descontos oferecidos
print(" ") #Pula uma linha
print("-="*40) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha
print('''\tEscolha o Tipo de Combustivel Desejado
{}      [A] Álcool         {}
{}      [G] Gasolina       {}
      '''.format(verde,reset,vermelha,reset)) #Pede ao usuario selecionar uma opção
opcao = input('') #Armazena a opção na variavel
print(" ") #Pula uma linha


if opcao == 'a' or opcao == 'A': #Cria uma condição - Se a opção escolhida for A - Alcool
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Quantos litros deseja abastecer? ") #Pergunta ao usuario quantos litros ele deseja abastecer
    litros=float(input("")) #Armazena a quantidade de litros na variavel

    if litros  <= 20:  #Cria uma condição - Se a quantidade for igual ou menor a 20 litros
        desconto = alcool * 0.03 #Realiza o calculo de desconto
        vcomb = alcool-desconto #Aplica o desconto no valor do litro
        total = vcomb * litros #Realiza o calculo final do valor
        totalr=round(total,2) #Arredonda para 2 casas decimais
        print(" ") #Pula uma linha
        print("-="*40) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
        print("\t O Valor total com 3% de Desconto é: {} R${} {}".format(verde,totalr,reset) ) #Informa o valor ao usuario
        print(" ") #Pula uma linha
        print("-="*40) #Cria uma barra de inicialização do programa

    else: #Cria uma condição - Se a quantidade for maior que 20 litros
        desconto = alcool * 0.05 #Realiza o calculo de desconto
        vcomb = alcool-desconto #Aplica o desconto no valor do litro
        total = vcomb * litros #Realiza o calculo final do valor
        totalr=round(total,2) #Arredonda para 2 casas decimais
        print(" ") #Pula uma linha
        print("-="*40) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
        print("\t O Valor total com 5% de Desconto é: {} R${} {}".format(verde,totalr,reset) ) #Informa o valor ao usuario
        print(" ") #Pula uma linha
        print("-="*40) #Cria uma barra de inicialização do programa

elif opcao == 'g' or opcao == 'G': #Cria uma condição - Se a opção escolhida for G - Gasolina
    print("\t Quantos litros deseja abastecer? ") #Pergunta ao usuario quantos litros ele deseja abastecer
    litros=float(input("")) #Armazena a quantidade de litros na variavel

    if litros  <= 20: #Cria uma condição - Se a quantidade for igual ou menor a 20 litros
        desconto = gasolina * 0.04 #Realiza o calculo de desconto
        vcomb = alcool-desconto #Aplica o desconto no valor do litro
        total = vcomb * litros #Realiza o calculo final do valor
        totalr=round(total,2) #Arredonda para 2 casas decimais
        print(" ") #Pula uma linha
        print("-="*40) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
        print("\t O Valor total com 3% de Desconto é: {} R${} {}".format(verde,totalr,reset) ) #Informa o valor ao usuario
        print(" ") #Pula uma linha
        print("-="*40) #Cria uma barra de inicialização do programa

    else: #Cria uma condição - Se a quantidade for maior que 20 litros
        desconto = gasolina * 0.06 #Realiza o calculo de desconto
        vcomb = alcool-desconto #Aplica o desconto no valor do litro
        total = vcomb * litros #Realiza o calculo final do valor
        totalr=round(total,2) #Arredonda para 2 casas decimais
        print(" ") #Pula uma linha
        print("-="*40) #Cria uma barra de inicialização do programa
        print(" ") #Pula uma linha
        print("\t O Valor total com 5% de Desconto é: {} R${} {}".format(verde,totalr,reset) ) #Informa o valor ao usuario
        print(" ") #Pula uma linha
        print("-="*40) #Cria uma barra de inicialização do programa

else: #Cria uma condição - Se a opção escolhida for invalida
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t{} Opção Inválida. Tente Novamente {}".format(vermelha,reset) ) #Informa opção invalida ao usuario
    print(" ") #Pula uma linha
    print("-="*40) #Cria uma barra de inicialização do programa