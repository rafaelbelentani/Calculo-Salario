verde = "\033[4;92m"    #Seta a Cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[1;91m" #Seta a Cor Vermelha

print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90)   #Cria uma barra de inicialização do programa
print("") #Pula uma linha

print("\t Bem Vindo à Calculadora de Subtração") #Saudações Iniciais
print("") #Pula uma linha


print("\t Digite o Primeiro Número: ") #Pergunta o primeiro número
n1 = float(input("")) #Armazena o primeiro número na variavel N1
print("") #Pula uma linha

print("\t Digite o Segundo Número: ") #Pergunta o segundo número
n2 = float(input("")) #Armazena o segundo número na variavel N2
print("") #Pula uma linha

total=n1-n2 #Realiza a Subtração
total_r=round(total,4) #Arredonda as casas decimais em 4 casas

print("\t A Subtração é: {}{}{}".format(vermelha,total_r,reset)) #Informa o Valor do calculo

print("") #Pula uma linha
print("") #Pula uma linha
print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Saudações Finais

print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90)   #Cria uma barra de Finalização do programa