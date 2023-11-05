print("-"*90) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha

print("Olá, seja Bem-Vindo a Calculadora de média") #Boas Vindas
print(" ") #Pula uma linha

print("Qual a primeira nota?") #Pede a primeira nota
n1=float(input(" ")) #Armazena a nota1 na variavel
print("Qual a segunda nota?") #Pede a segunda nota
n2=float(input(" ")) #Armazena a nota2 na variavel
print("Qual a terceira nota?")#Pede a segunda nota
n3=float(input(" "))#Armazena a nota3 na variavel
print("Qual a quarta nota?")#Pede a segunda nota
n4=float(input(" "))#Armazena a nota4 na variavel

media = (n1+n2+n3+n4)/4 #Realiza o calculo da media

if media >= 7: #Cria uma condição - Se a nota for maior ou igual a 7
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de separação do programa
    print(" ") #Pula uma linha
    print("Parabens, sua nota é {}. Voce foi aprovado".format(media)) #Informa que o aluno foi aprovado
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de separação do programa
elif media >= 5: #Cria uma condição - Se a nota for maior ou igual a 5
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de separação do programa
    print(" ") #Pula uma linha
    print("Sua nota é {}. Voce ficou de Recuperação".format(media)) #Informa que o aluno esta de recuperação
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de separação do programa
else: #Cria uma condição - Se a nota for menor que 5
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de separação do programa
    print(" ") #Pula uma linha
    print("Sua nota é {}. Voce foi reprovado".format(media)) #Informa que o aluno foi reprovado
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de separação do programa