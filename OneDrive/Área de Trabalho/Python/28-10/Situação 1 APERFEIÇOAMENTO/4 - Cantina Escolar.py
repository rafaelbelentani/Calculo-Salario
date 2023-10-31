verde = "\033[4;92m"    #Seta a Cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[1;91m" #Seta a Cor Vermelha


print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90) #Cria uma barra de inicialização
print("") #Pula uma linha
print("") #Pula uma linha
print("\t Olá, seja bem vindo ao seu programa. \n\t Qual é o seu nome?") #Boas vindas
nome=input("")  #Armazena o nome do usuario na variavel nome

print("\t Muito bem {}{}{}. Nós vamos realizar os calculos e informar qual a melhor opção para você.".format(verde,nome,reset)) #Informação sobre o programa
print("\t Nós vamos auxiliar a converter garrafas de refrigerantes em copos de 250ml")  #Informação sobre o programa
print("") #Pula uma linha
print("\t Quantos mililitros(ml) tem a sua garrafa?") #Pergunta a quantidade da garrafa
garrafa=int(input()) #Armazena a quantidade na variavel garrafa
print("\t Muito bem. Qual o valor dessa garrafa?") #Pergunta o valor da garrafa
valor=float(input()) #Armazena o valor na variavel Valor
print("\t Qual a porcentagem de lucro que voce quer obter?") #Pergunta a porcentagem de lucro esperada
lucro=float(input())  #Armazena a porcentagem do lucro na variavel Lucro

copo=garrafa//250 #Faz o calculo de quantos copos de 250ml haverá com a quantidade da garrafa informada

valor_copo=valor/copo #Faz o calculo do valor do copo sem o lucro
valor_copo_r=round(valor_copo, 2) #Limita as casas decimais

lucro_venda=(valor*(lucro/100)) + valor  #Faz o calculo do lucro total 
lucrofinal= lucro_venda/copo #divide o lucro total pela quantidade de copos
lucro_final_r=round(lucrofinal, 2) #Limita as casas decimais

sobra=garrafa%250 #Calculo de sobra
sobra_r=round(sobra, 2) #Limita as casas decimais

print("-"*90) #Cria uma barra de separação
print("") #Pula uma linha
print("\t Cada copo pode ser vendido por {}R${}{}".format(verde,valor_copo_r,reset)) #Informa ao usuario o valor a ser vendido sem o lucro desejado

if sobra != 0:  #Faz um decisão. Se haver sobra
    print("\t Sobrará uma quantia de {}{}mls{}".format(vermelha,sobra_r,reset)) #Se haver sobra ele informa a quantidade que foi sobrada

print("") #Pula uma linha
print("\t Para obter o lucro de {}{}%{} voce deve vender cada copo por: {}R${}{}".format(verde,lucro,reset,verde,lucro_final_r,reset)) #Informa o valor do copo com o lucro desejado
print("") #Pula uma linha
print("") #Pula uma linha
print("\t Obrigado por utilizar nosso serviços... \n \t Volte Sempre") #Agradecimentos finais
print("") #Pula uma linha
print("-"*90) #Cria uma barra de finalização

