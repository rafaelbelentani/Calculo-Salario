verde = "\033[92m"    #Seta a Cor Verde
reset= "\033[0m"     #Seta a Cor Original


print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90) #Cria uma linha de inicilização
print("") #Pula uma linha
print("") #Pula uma linha
print("\t Olá, Digite um número e eu vou escrever o Antecessor dele...") #Pergunta o número desejado
n1=int(input("")) #Armazena o numero na variavel N1
 
ant=n1-1 #Realiza o Calculo do numero -1

print("\t O Antecessor do número {}{}{} é {}{}{}".format(verde,n1,reset,verde,ant,reset)) #Informa o numero antecessor ao usuario
print("") #Pula uma linha
print("") #Pula uma linha
print("\t Obrigado por utilziar nosso programa... \n \t Volte Sempre") #Saudações finais
print("-"*90) #Cria uma linha de Finalização