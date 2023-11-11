verde = "\033[4;92m"    #Seta a Cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[4;91m" #Seta a Cor Vermelha

print(" ") #Pula uma linha
print("-"*90) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha

print("Olá, seja Bem-Vindo de Doação de Sangue. Para fazer a doação voce deve ter entre 18 e 67 anos") #Boas Vindas
print(" ") #Pula uma linha

print("\t Insira a sua Idade") #Pede que usuario informe qualquer numero
numero = int(input(" ")) #Armazena o numero informado na variavel



if numero >= 18 and numero <= 67: #Cria uma condição - se a idade for maior ou igual a 18 e menor ou igual a 67
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Voce pode fazer a Doação.") #Informa ao usuario que ele pode ser um doador
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
else: #Cria uma condição - Se a idade for menor que 18 e maior que 67
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Desculpe, voce não pode ser um Doador.") #Informa ao usuario que ele não pode ser um doador
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa