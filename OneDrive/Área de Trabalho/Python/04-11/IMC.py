abaixo = 18.5
ideal = 24.9
acima = 29.9
obesidade1 = 34.9
obesidade2 = 39.9
obesidade3 = 40

tabela = print("Confira a Tabela")

print("\t Bem-Vindo a Calculadora de IMC...")
print(" ")


print("\t Qual o seu peso?")
peso = float(input(" "))

print("\t Qual a sua altura?")
altura = float(input(" "))

imc = peso/altura**2
imc_r = round(imc, 2)

if imc <= abaixo:
    print("\t Seu imc é {} e voce está abaixo do peso".format(imc_r))

elif imc > abaixo and imc <= ideal:
    print("\t Seu imc é {} e voce está no seu peso ideal".format(imc_r))
    
elif imc > ideal and imc <= acima:
    print("\t Seu imc é {} e voce está acima do peso ideal".format(imc_r))
    
elif imc > acima and imc <= obesidade1:
    print("\t Seu imc é {} e voce está na Obesidade grau I".format(imc_r))

elif imc > obesidade1 and imc <= obesidade2:
    print("\t Seu imc é {} e voce está na Obesidade grau II".format(imc_r))
    
else:
    print("\t Seu imc é {} e voce está na Obesidade grau III \n Ta GORDÃO ".format(imc_r))