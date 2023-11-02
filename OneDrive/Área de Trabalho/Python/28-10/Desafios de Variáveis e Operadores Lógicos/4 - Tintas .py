import math #importa módulos matematicos para python - Arredonda para cima a divisão de tinta
verde = "\033[92m"    #Seta a Cor Verde
reset= "\033[0m"     #Seta a Cor Original
vermelha = "\033[1;91m" #Seta a Cor Vermelha
precoLata = 50.00 #Seta o preço da lata de tinta
Lata = 5 #Seta a quantidade de uma lata de tinta
cobertura = 3 #Seta a area de cobertura de 1 litro de tinta
pi = 3.14 #seta o valor de pi para usar nos calculos

print("") #Pula uma linha
print("") #Pula uma linha
print("-"*90) #Cria uma linha de inicilização
print("") #Pula uma linha
print("") #Pula uma linha
print("\t Olá, seja Bem-Vindo à Calculadora de Tinta.") #Inicialização do programa - pergunta o nome do usuario

print("\t Digite o raio do cilindro em metros.") #Pergunta ao usuario o raio do cilindro
Raio = float(input("")) #Salva a area na variavel
print("\t Digite a altura do cilindro em metros.")  #Pergunta ao usuario a altura do cilindro
Altura = float(input("")) #Salva a altura na variavel

areaCilidro = 2*pi*Raio**2+2*pi*Raio*Altura #Realiza o Calculo da area do cilindro
areaCilidro_r=round(areaCilidro, 2) #Arredonda para 2 casas decimais
print("{}-{}".format(vermelha,reset)*90) #Cria uma linha de inicilização
print("") #Pula uma linha
print("\t A área do cilindro é {}{}{} m²".format(verde,areaCilidro_r,reset)) #Informa a area do cilindro

litrosTinta = areaCilidro / cobertura #Realiza o calculo de quantos litros de tinta será necessária
litrosTinta_r=round(litrosTinta, 2) #Arredonda para 2 casas decimais
print("\t Voce precisará de {}{}{} litros de tinta".format(verde,litrosTinta_r,reset)) #Informa quantos litros de tinta será necessároo

quantidadeLatas = math.ceil(litrosTinta / Lata) #Realiza o calculo de quantas latas de tinta será necessário - arredondando para cima
print("\t Voce precisará de {}{}{} latas de tinta".format(verde,quantidadeLatas,reset)) #Informa quantas latas de tinta será necessároa

sobra = ((quantidadeLatas*Lata) - litrosTinta) #Realiza o calculo da sobra de tinta
sobra_r=round(sobra, 2)  #Arredonda para 2 casas decimais
if sobra_r !=0: #Cria uma decisão - se houver sobra
    print("\t Sobrará {}{}{} litros".format(verde,sobra_r,reset)) #Informar quantos litros sobrará
else: #Cria uma decisão - se não houver sobra
    print("\t {}Não Sobrará tinta{}".format(vermelha,reset)) #Informar que não sobrará tinta

custo = quantidadeLatas  * precoLata #Realiza o calculo final
print("\t O valor total é de {}R${}{}".format(verde,custo,reset)) #Informa o custo total de tinta

print("") #Pula uma linha
print("\t Muito Obrigado por utilziar nosso programa... \n \t Volte Sempre") #Finalização do programa

print("") #Pula uma linha
print("{}-{}".format(vermelha,reset)*90) #Cria uma linha de inicilização