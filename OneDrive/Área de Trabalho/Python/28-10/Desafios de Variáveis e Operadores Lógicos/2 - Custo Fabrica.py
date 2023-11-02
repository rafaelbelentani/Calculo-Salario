verde = "\033[92m"    #Seta a Cor Verde
reset= "\033[0m"     #Seta a Cor Original

print("") #Pula uma linha
print("-"*90)   #Cria uma barra de inicialização do programa
print("") #Pula uma linha
print("") #Pula uma linha


print("\t Olá, seja Bem-Vindo à Calculadora de veículos") #Boas Vindas
print("") #Pula uma linha

print("\t Qual o custo de fabrica do veículo?") #Pergunta o valor do custo de fabrica do veiculo
CustoFabrica = float(input("")) #Armazena o valor na variavel

Distribuidor = CustoFabrica * 0.48 #Realiza o calculo do Distribuidor
Distribuidor_r = round(Distribuidor, 2) #Arredonda as casas decimais
Imposto = CustoFabrica * 0.45 #Realiza o calculo do Imposto
Imposto_r = round(Imposto, 2) #Arredonda as casas decimais
CustoTotal = CustoFabrica + Imposto + Distribuidor #Realiza o calculo do valor total do veiculo
CustoTotal_r = round(CustoTotal, 2) #Arredonda as casas decimais


print("-"*90)   #Cria uma barra de inicialização do programa
print("") #Pula uma linha
print("\t O valor do Imposto do veículo é {}R${}{} \n \t O valor do Distribuidor do veículo é {}R${}{} \n \t O Custo Total do veículo é {}R${}{}".format(verde,Imposto_r,reset,verde,Distribuidor_r,reset,verde,CustoTotal_r,reset)) #Informa os valores

print("") #Pula uma linha
print("-"*90)   #Cria uma barra de inicialização do programa
print("") #Pula uma linha
print("\t Obrigado por utilizar nosso programa... \n \t Volte Sempre") #Finalização do programa
print("") #Pula uma linha
print("-"*90)   #Cria uma barra de inicialização do programa
