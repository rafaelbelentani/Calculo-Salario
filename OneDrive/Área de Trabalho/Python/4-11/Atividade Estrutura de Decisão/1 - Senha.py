verde = "\033[1;37;42m"    #Seta o fundo na cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[1;37;41m" #Seta o fundo na cor Vermelha

print("-="*50) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha

print("\t Olá, seja Bem-Vindo a Autenticação de Senha.") #Boas Vindas
print(" ") #Pula uma linha

print("\t Informe a sua Senha: ") #Informações do Programa
password=input(" ") #Armazena a senha digitada na variavel
print(" ") #Pula uma linha
print("-="*50) #Cria uma barra de inicialização do programa

senha=str(1234) #Armazena a senha ja definida na variavel

if senha == password: #Cria uma condição - Se a senha for igual a senha digitada
    print(" ") #Pula uma linha
    print("{} ACESSO PERMITIDO {}".format(verde,reset)) #Informa que o acesso foi permitido
    print(" ") #Pula uma linha
    print("-="*50) #Cria uma barra de inicialização do programa
else: #Cria uma condição - Se a senha for diferente a senha digitada
    print(" ") #Pula uma linha
    print("{} ACESSO NEGADO {}".format(vermelha,reset)) #Informa que o acesso foi negado
    print(" ") #Pula uma linha
    print("-="*50) #Cria uma barra de inicialização do programa