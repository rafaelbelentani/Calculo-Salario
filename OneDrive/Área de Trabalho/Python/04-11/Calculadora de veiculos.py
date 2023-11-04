verde = "\033[4;92m"    #Seta a Cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[91m" #Seta a Cor Vermelha

print("-"*90) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha

print("\t Olá, seja Bem-Vindo a Calculadora de Simulação de Compra de Veículo.") #Boas Vindas
print(" ") #Pula uma linha

print("\t Nós vamos te auxiliar a calcular o valor das parcelas do seu veículo") #Informações do Programa
print(" ") #Pula uma linha
print("-"*90) #Cria uma barra de inicialização do programa
print("\t Informe o valor do veículo desejado: ") #Pergunta ao usuário o valor do veículo
valor = float(input("R$ ")) #Armazena o valor na variavel
print("-"*90) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha


print("\t Certo, agora informe a forma de pagamento") #Pede ao usuario escolha a opção Desejada
print('''[1] À Vista
[2] 6 Vezes
[3] 12 Vezes
[4] 18 Vezes
[5] 24 Vezes
[6] 30 Vezes
[7] 36 Vezes
[8] 42 Vezes
[9] 48 Vezes
[10] 54 Vezes
[11] 60 Vezes''') #Informa as opções Disponíveis
escolha = int(input(""))

if escolha == 1: #Cria uma Condição - Se escolheu a opçao 1
    desconto = valor *0.2 #Realiza o calculo do desconto
    VF=valor-desconto #Aplica o desconto no valor final do veiculo
    VF_R=round(VF, 2) #Arredonda as casas decimais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Voce selecionou a opção {}1 - À Vista{}".format(verde,reset)) #Informa a opção escolhida
    print("\t Essa opção oferece {}20% de desconto{}.".format(verde,reset)) #Informa o desconto
    print("\t O Valor final do seu veículo é de {}R${}{}".format(verde,VF_R,reset)) #Informa o valor final do veiculo
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa

    

elif escolha == 2: #Cria uma Condição - Se escolheu a opçao 2
    desconto = valor *0.03 #Realiza o calculo do juros
    VF=valor+desconto #Aplica o juros no valor final do veiculo
    VF_R=round(VF, 2) #Arredonda as casas decimais
    parcelas = VF/6 #Realiza o calculo das parcelas
    parcelas_r=round(parcelas, 2)  #Arredonda as casas decimais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Voce selecionou a opção {}2 - Em 6 vezes{}".format(verde,reset)) #Informa a opção escolhida
    print("\t Essa opção tem {}3% de juros.{}".format(vermelha,reset)) #Informa o desconto
    print("\t O Valor final do seu veículo é de {}R${}{}".format(verde,VF_R,reset)) #Informa o valor final do veiculo
    print("\t As parcelas serão de: {}R${}{}".format(verde,parcelas_r,reset)) #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa

elif escolha == 3: #Cria uma Condição - Se escolheu a opçao 3
    desconto = valor *0.06 #Realiza o calculo do juros
    VF=valor+desconto #Aplica o juros no valor final do veiculo
    VF_R=round(VF, 2) #Arredonda as casas decimais
    parcelas = VF/12 #Realiza o calculo das parcelas
    parcelas_r=round(parcelas, 2)  #Arredonda as casas decimais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Voce selecionou a opção {}3 - Em 12 vezes{}".format(verde,reset)) #Informa a opção escolhida
    print("\t Essa opção tem {}6% de juros.{}".format(vermelha,reset)) #Informa o desconto
    print("\t O Valor final do seu veículo é de {}R${}{}".format(verde,VF_R,reset)) #Informa o valor final do veiculo
    print("\t As parcelas serão de: {}R${}{}".format(verde,parcelas_r,reset)) #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa

elif escolha == 4: #Cria uma Condição - Se escolheu a opçao 4
    desconto = valor *0.09 #Realiza o calculo do juros
    VF=valor+desconto #Aplica o juros no valor final do veiculo
    VF_R=round(VF, 2) #Arredonda as casas decimais
    parcelas = VF/18 #Realiza o calculo das parcelas
    parcelas_r=round(parcelas, 2)  #Arredonda as casas decimais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Voce selecionou a opção {}4 - Em 18 vezes{}".format(verde,reset)) #Informa a opção escolhida
    print("\t Essa opção tem {}9% de juros.{}".format(vermelha,reset)) #Informa o desconto
    print("\t O Valor final do seu veículo é de {}R${}{}".format(verde,VF_R,reset)) #Informa o valor final do veiculo
    print("\t As parcelas serão de: {}R${}{}".format(verde,parcelas_r,reset)) #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa

elif escolha == 5: #Cria uma Condição - Se escolheu a opçao 5
    desconto = valor *0.12 #Realiza o calculo do juros
    VF=valor+desconto #Aplica o juros no valor final do veiculo
    VF_R=round(VF, 2) #Arredonda as casas decimais
    parcelas = VF/24 #Realiza o calculo das parcelas
    parcelas_r=round(parcelas, 2)  #Arredonda as casas decimais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Voce selecionou a opção {}5 - Em 24 vezes{}".format(verde,reset)) #Informa a opção escolhida
    print("\t Essa opção tem {}12% de juros.{}".format(vermelha,reset)) #Informa o desconto
    print("\t O Valor final do seu veículo é de {}R${}{}".format(verde,VF_R,reset)) #Informa o valor final do veiculo
    print("\t As parcelas serão de: {}R${}{}".format(verde,parcelas_r,reset)) #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa

elif escolha == 6: #Cria uma Condição - Se escolheu a opçao 6
    desconto = valor *0.15 #Realiza o calculo do juros
    VF=valor+desconto #Aplica o juros no valor final do veiculo
    VF_R=round(VF, 2) #Arredonda as casas decimais
    parcelas = VF/30 #Realiza o calculo das parcelas
    parcelas_r=round(parcelas, 2)  #Arredonda as casas decimais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Voce selecionou a opção {}6 - Em 30 vezes{}".format(verde,reset)) #Informa a opção escolhida
    print("\t Essa opção tem {}15% de juros.{}".format(vermelha,reset)) #Informa o desconto
    print("\t O Valor final do seu veículo é de {}R${}{}".format(verde,VF_R,reset)) #Informa o valor final do veiculo
    print("\t As parcelas serão de: {}R${}{}".format(verde,parcelas_r,reset)) #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa

elif escolha == 7: #Cria uma Condição - Se escolheu a opçao 7
    desconto = valor *0.18 #Realiza o calculo do juros
    VF=valor+desconto #Aplica o juros no valor final do veiculo
    VF_R=round(VF, 2) #Arredonda as casas decimais
    parcelas = VF/36 #Realiza o calculo das parcelas
    parcelas_r=round(parcelas, 2)  #Arredonda as casas decimais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Voce selecionou a opção {}7 - Em 36 vezes{}".format(verde,reset)) #Informa a opção escolhida
    print("\t Essa opção tem {}18% de juros.{}".format(vermelha,reset)) #Informa o desconto
    print("\t O Valor final do seu veículo é de {}R${}{}".format(verde,VF_R,reset)) #Informa o valor final do veiculo
    print("\t As parcelas serão de: {}R${}{}".format(verde,parcelas_r,reset)) #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa

elif escolha == 8: #Cria uma Condição - Se escolheu a opçao 8
    desconto = valor *0.21 #Realiza o calculo do juros
    VF=valor+desconto #Aplica o juros no valor final do veiculo
    VF_R=round(VF, 2) #Arredonda as casas decimais
    parcelas = VF/42 #Realiza o calculo das parcelas
    parcelas_r=round(parcelas, 2)  #Arredonda as casas decimais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Voce selecionou a opção {}8 - Em 42 vezes{}".format(verde,reset)) #Informa a opção escolhida
    print("\t Essa opção tem {}21% de juros.{}".format(vermelha,reset)) #Informa o desconto
    print("\t O Valor final do seu veículo é de {}R${}{}".format(verde,VF_R,reset)) #Informa o valor final do veiculo
    print("\t As parcelas serão de: {}R${}{}".format(verde,parcelas_r,reset)) #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa

elif escolha == 9: #Cria uma Condição - Se escolheu a opçao 9
    desconto = valor *0.24 #Realiza o calculo do juros
    VF=valor+desconto #Aplica o juros no valor final do veiculo
    VF_R=round(VF, 2) #Arredonda as casas decimais
    parcelas = VF/48 #Realiza o calculo das parcelas
    parcelas_r=round(parcelas, 2)  #Arredonda as casas decimais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Voce selecionou a opção {}9 - Em 48 vezes{}".format(verde,reset)) #Informa a opção escolhida
    print("\t Essa opção tem {}24% de juros.{}".format(vermelha,reset)) #Informa o desconto
    print("\t O Valor final do seu veículo é de {}R${}{}".format(verde,VF_R,reset)) #Informa o valor final do veiculo
    print("\t As parcelas serão de: {}R${}{}".format(verde,parcelas_r,reset)) #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa

elif escolha == 10: #Cria uma Condição - Se escolheu a opçao 10
    desconto = valor *0.27 #Realiza o calculo do juros
    VF=valor+desconto #Aplica o juros no valor final do veiculo
    VF_R=round(VF, 2) #Arredonda as casas decimais
    parcelas = VF/54 #Realiza o calculo das parcelas
    parcelas_r=round(parcelas, 2)  #Arredonda as casas decimais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Voce selecionou a opção {}10 - Em 54 vezes{}".format(verde,reset)) #Informa a opção escolhida
    print("\t Essa opção tem {}27% de juros.{}".format(vermelha,reset)) #Informa o desconto
    print("\t O Valor final do seu veículo é de {}R${}{}".format(verde,VF_R,reset)) #Informa o valor final do veiculo
    print("\t As parcelas serão de: {}R${}{}".format(verde,parcelas_r,reset)) #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa

elif escolha == 11: #Cria uma Condição - Se escolheu a opçao 11
    desconto = valor *0.30 #Realiza o calculo do juros
    VF=valor+desconto #Aplica o juros no valor final do veiculo
    VF_R=round(VF, 2) #Arredonda as casas decimais
    parcelas = VF/60 #Realiza o calculo das parcelas
    parcelas_r=round(parcelas, 2)  #Arredonda as casas decimais
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Voce selecionou a opção {}11 - Em 60 vezes{}".format(verde,reset)) #Informa a opção escolhida
    print("\t Essa opção tem {}30% de juros.{}".format(vermelha,reset)) #Informa o desconto
    print("\t O Valor final do seu veículo é de {}R${}{}".format(verde,VF_R,reset)) #Informa o valor final do veiculo
    print("\t As parcelas serão de: {}R${}{}".format(verde,parcelas_r,reset)) #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("\t Obrigado por utilizar nossos serviços... \n\t Volte Sempre") #Informa o valor das parcelas
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa


else:
    print("-"*90)  #Cria uma barra de separação
    print(" ") #Pula uma linha
    print("Você escolheu uma opção inválida. Tente Novamente") #Informa que a opção escolhida é uma opção inválida
    print(" ") #Pula uma linha
    print("-"*90)  #Cria uma barra de finalização
