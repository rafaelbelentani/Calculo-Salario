verde = "\033[4;92m"    #Seta a Cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[91m" #Seta a Cor Vermelha

print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90)   #Cria uma barra de inicialização do programa
print("") #Pula uma linha

print("\t Bem Vindo à Calculadora de Gastos") #Saudações Iniciais
print("") #Pula uma linha
print("\t Qual o valor gasto mensal com {}ÁGUA?{}".format(verde,reset)) #Pergunta o gasto mensal com AGUA
agua = float(input("")) #Armazena o valor digitado na Variavel AGUA
print("") #Pula uma linha
print("\t Qual o valor gasto mensal com {}LUZ?{}".format(verde,reset)) #Pergunta o gasto mensal com LUZ
luz = float(input("")) #Armazena o valor digitado na Variavel LUZ
print("") #Pula uma linha
print("\t Qual o valor gasto mensal com {}MERCADO?{}".format(verde,reset)) #Pergunta o gasto mensal com MERCADO
mercado = float(input("")) #Armazena o valor digitado na Variavel MERCADO
print("") #Pula uma linha
print("\t Qual o valor gasto mensal com {}DESPESAS MÉDICAS?{}".format(verde,reset)) #Pergunta o gasto mensal com DESPESAS MEDICAS
medico = float(input("")) #Armazena o valor digitado na Variavel MEDICO
print("") #Pula uma linha

mes =  agua+luz+mercado+medico #Realiza o calculo total do mes
mes_r = round(mes,2)           #Arredonda as casas decimais
tmeses = 3 * mes               #Realiza o calculo total de 3 meses
tmeses_r=round(tmeses,2)        #Arredonda as casas decimais
smeses = 6 * mes               #Realiza o calculo total de 6 meses
smeses_r = round(smeses,2)      #Arredonda as casas decimais
ano = 12 * mes                  #Realiza o calculo total de 12 meses
ano_r=round(ano,2)             #Arredonda as casas decimais

print("\t O Valor total gasto no próximo {}mês{} será de: {}R$:{}{}".format(verde,reset,vermelha,mes_r,reset)) #Informa o valor gasto no mes
print("") #Pula uma linha
print("\t O Valor total gasto nos próximos {}3 meses{} será de: {}R$:{}{}".format(verde,reset,vermelha,tmeses_r,reset)) #Informa o valor gasto em 3 meses
print("") #Pula uma linha
print("\t O Valor total gasto nos próximos {}6 meses{} será de: {}R$:{}{}".format(verde,reset,vermelha,smeses_r,reset)) #Informa o valor gasto em 6 meses
print("") #Pula uma linha
print("\t O Valor total gasto no próximo {}ANO{} será de: {}R$:{}{}".format(verde,reset,vermelha,ano_r,reset))  #Informa o valor gasto em 12 meses

print("") #Pula uma linha
print("") #Pula uma linha
print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Saudações Finais

print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90)   #Cria uma barra de Finalização do programa