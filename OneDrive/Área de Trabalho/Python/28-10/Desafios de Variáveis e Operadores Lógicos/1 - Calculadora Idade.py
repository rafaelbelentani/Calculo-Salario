from datetime import datetime #importa a biblioteca datetime
dataAtual = datetime.now() #armazena a data atual na variavel

print("") #Pula uma linha
print("-"*90)   #Cria uma barra de inicialização do programa
print("") #Pula uma linha
print("") #Pula uma linha


print("\t Olá, seja Bem-Vindo à Conversora de idade") #Boas Vindas
print("") #Pula uma linha
print("\t Qual o dia do seu nascimento?") #Pergunta o dia do nascimentos
dia = int(input("")) #Armazena o dia na variavel
print("\t Qual o mes do seu nascimento?")#Pergunta o mes do nascimentos
mes = int(input("")) #Armazena o mes na variavel
if mes<=12: #cria uma condição - se o mes for menor ou igual a 12
    print("\t Qual o ano do seu nascimento?")  #Pergunta o ano do nascimento
    ano = int(input("")) #Armazena o ano na variavel
else: #Cria uma condição - se o mes for maior que 12
    print("\t Mes inválido") #Informa mes invalido
    print("\t Tente Novamente") #Fim do programa
    print("") #Pula uma linha
    print("-"*90)   #Cria uma barra de inicialização do programa

dataNascimento = datetime(year=ano, month=mes, day=dia) #Seta as variaveis - ano, dia e mes
diferenca = dataAtual - dataNascimento #Realiza o calculo da data informada com a data atual
diasFaltando = diferenca.days #Seta o calculo para apenas dias
print("-"*90)   #Cria uma barra de inicialização do programa
print("") #Pula uma linha

print("\t Voce tem aproximadamente {} dias".format(diasFaltando)) #Informa o resultado do calculo
print("") #Pula uma linha
print("-"*90)   #Cria uma barra de inicialização do programa
print("") #Pula uma linha

print("\t Obrigado por utilizar nosso programa... \n \t Volte Sempre".format(diasFaltando))
print("") #Pula uma linha
print("-"*90)   #Cria uma barra de inicialização do programa
