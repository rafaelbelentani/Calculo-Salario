verde = "\033[92m"    #Seta a Cor Verde
reset= "\033[0m"     #Seta a Cor Original
print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90) #Cria uma linha de inicilização
print("") #Pula uma linha
print("") #Pula uma linha
print("\t Olá, Qual é o seu nome?") #Inicialização do programa - pergunta o nome do usuario
nome=input("") #Armazena o nome na variavel 
print("\t Bem Vindo {}{}{}, este é um programa que vai auxiliar a mediar a área de um triangulo.".format(verde,nome,reset)) #Boas Vindas
print("\t Qual é a medida da base do seu triangulo?") #Pergunta a medida da base do triangulo
base=float(input("")) #Armazena a medida na variavel
print("\t Qual é a medida da altura do seu triangulo?") #Pergunta a medida da altura do triangulo
altura=float(input("")) #Armazena a medida na variavel
area=(base*altura)/2 #Realiza o calculo da area
print("\t A área do seu triangulo é: {}{}{}".format(verde,area,reset)) #Informa a area do triangulo
print("") #Pula uma linha
print("\t Muito Obrigado por utilziar nosso programa... \n \t Volte Sempre") #Finalização do programa
print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90) #Cria uma linha de inicilização