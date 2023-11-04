print("-"*90) #Cria uma barra de inicialização do programa
print(" ") #Pula uma linha

print("Olá, seja Bem-Vindo a Calculadora de Salário") #Boas Vindas
print(" ") #Pula uma linha


salarioMinimo = 1320.00 #Seta o valor do salario minimo

print("Informe o salário?") #Pede ao usuario que informe o valor do salario
salario=float(input(" ")) #Salva o valor na variavel

if salario > salarioMinimo: #Cria uma condição - se o salario informado for maior que o salario minimo
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("O seu salario é maior do que um salario minimo") #Informa ao usuario que o salario informado é maior que um salario minimo
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa
    
else: #Cria uma condição - Se o salario nao for mair
    print("-"*90) #Cria uma barra de inicialização do programa
    print(" ") #Pula uma linha
    print("O seu salario é menor do que um salario minimo") #Informa que o salario é menor
    print(" ") #Pula uma linha
    print("-"*90) #Cria uma barra de inicialização do programa