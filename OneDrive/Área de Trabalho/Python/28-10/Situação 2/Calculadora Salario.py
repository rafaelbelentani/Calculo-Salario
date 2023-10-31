cor_verde = "\033[92m"    #Seta a Cor Verde
cor_reset = "\033[0m"     #Seta a Cor Original
cor_vermelha = "\033[91m" #Seta a Cor Vermelha

print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90)   #Cria uma barra de inicialização do programa

print("\t Bem-Vindo à Calculadora de Salário \n\t Qual seu Nome?") #Inicialização do programa
nome = input("") #Salva o nome do cliente na variavel NOME

print("\t Olá {}{}{} qual o seu Salário Atual?".format(cor_verde,nome,cor_reset)) #Pergunta o Salário Atual
SalarioAtual = float(input("R$")) #Armazena o salario atual na variavel SalarioAtual

print("\t Qual a Porcentagem de aumento?") #Pergunta a Porcentagem de Aumento
Porc=float(input("")) #Armazena a Porcentagem na variavel Porc

Aumento = SalarioAtual*Porc/100 #Realiza o Calculo de Aumento do Salario Bruto
SalarioBruto = SalarioAtual+Aumento #Realiza o Calculo do Salario Bruto
SalarioBruto_arredondado=round(SalarioBruto, 2)

IR=SalarioBruto * 0.07               #Realiza o Calculo de desconto do Imposto de Renda
IR_arredondado = round(IR, 2)          #Arredonda as casas decimais
Sindicato=SalarioBruto * 0.03        #Realiza o Calculo de desconto do Sindicato
Sindicato_arredondado = round(Sindicato, 2) #Arredonda as casas decimais
PS=SalarioBruto * 0.08               #Realiza o Calculo de Aumento do Plano de Saude
PS_arredondado = round(PS, 2) #Arredonda as casas decimais
 

NovoSalario=SalarioAtual+Aumento-IR-Sindicato-PS    #Realiza o Calculo do Salario Liquido
NovoSalario_arredondado= round(NovoSalario, 2) #Arredonda as casas decimais

print("\t Você teve um aumento de {}{}%{} no seu salário.".format(cor_verde,Porc,cor_reset)) #Informa ao Usuario a porcentagem de aumento
print("\t Seu Salário Bruto é de {}R${}{}".format(cor_verde,SalarioBruto_arredondado,cor_reset)) #Informa ao Usuario o Salario Bruto
print("\t Foi Descontado os valores a seguir...") 
print("") #Pula uma linha
print("Imposto de Renda: {}R${}{}".format(cor_vermelha,IR_arredondado,cor_reset)) #Informa ao Usuario o Valor Descontado do Imposto de Renda
print("Sindicato: {}R${}{}".format(cor_vermelha,Sindicato_arredondado,cor_reset)) #Informa ao Usuario o Valor Descontado do Sindicato
print("Plano de Saúde: {}R${}{}".format(cor_vermelha,PS_arredondado,cor_reset))   #Informa ao Usuario o Valor Descontado do Plano de Saude

print("") #Pula uma linha
print("Seu Salário Líquido Atual é de: {}R${}{}".format(cor_verde,NovoSalario_arredondado,cor_reset)) #Informa o Salario Atual
print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Saudações Finais
print("") #Pula uma linha
print("-"*90)   #Cria uma barra de Finalização do programa