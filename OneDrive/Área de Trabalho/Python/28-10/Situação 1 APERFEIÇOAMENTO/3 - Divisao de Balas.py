verde = "\033[4;92m"    #Seta a Cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[1;91m" #Seta a Cor Vermelha

print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90)   #Cria uma barra de inicialização do programa
print("") #Pula uma linha

print("\t Bem Vindo à Calculadora de Divisão") #Saudações Iniciais
print("") #Pula uma linha

print("\t Qual a Quantidade de {}Balas?{} ".format(verde,reset)) #Pergunta o primeiro número
n1 = int(input("")) #Armazena o primeiro número na variavel N1
print("") #Pula uma linha

print("\t Quantas {}Crianças{} serão contempladas?".format(verde,reset)) #Pergunta o primeiro número
n2 = int(input("")) #Armazena o primeiro Segundo na variavel N2
print("") #Pula uma linha


if n2 == 0: #Cria uma decisão, onde o numero não pode ser igual a zero
    print("{}\t Não é possível fazer a divisão por 0 Crianças{}".format(vermelha,reset)) #Informa ao usuario
    print("") #Pula uma linha
    print("") #Pula uma linha
    print("{}\t Tente Novamente{}".format(vermelha,reset)) #Finaliza o programa
    print("") #Pula uma linha
    print("") #Pula uma linha
    print("-"*90)   #Cria uma barra de Finalização do programa


total=n1//n2 #Realiza a divisao arredondando para baixo o numero de balas por crianças
sobra = n1%n2 #Realiza o calculo da sobra das balas


print("\t Serão um total de {}{}{} Balas para cada criança".format(verde, total, reset)) #informa para o usuario o resultado do calculo

if sobra != 0:      #Cria uma condição. Se a sobra for diferente de zero ele informa ao usuario quantas balas sobraram
    print("\t E sobraram {}{}{} Bala(s)".format(verde,sobra,reset)) #Informar ao usuario quantas balas sobraram

print("") #Pula uma linha
print("") #Pula uma linha
print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Saudações Finais

print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90)   #Cria uma barra de Finalização do programa