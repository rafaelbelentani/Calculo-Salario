cor_verde = "\033[92m"    #Seta a Cor Verde
cor_reset = "\033[0m"     #Seta a Cor Original
cor_vermelha = "\033[91m" #Seta a Cor Vermelha

print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90)   #Cria uma barra de inicialização do programa
print("") #Pula uma linha
print("") #Pula uma linha

print("\t Bem-Vindo à Conversão de Temperatura \n\t Qual seu Nome?") #Inicialização do programa
nome = input("") #Salva o nome do cliente na variavel NOME

print("\t Olá {}{}{} Digite a Temperatura em Fahrenheit".format(cor_verde,nome,cor_reset)) #Pergunta a Temperatura em Fahrenheit
Temperatura = float(input()) #Armazena a Temperatura na variavel TEMPERATURA


Celsius = 5 * ((Temperatura-32)/9) #Faz a Conversão para Celsius
Celsius_ar = round(Celsius, 4)  #Arredonda as casas decimais

print("A Temperatura é {}{}ºC{}".format(cor_verde,Celsius_ar,cor_reset)) #Mostra ao Usuario a Temperatura Convertida

print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90)   #Cria uma barra de inicialização do programa