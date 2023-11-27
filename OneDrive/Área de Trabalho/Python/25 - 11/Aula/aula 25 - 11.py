from tkinter import * #Importa a bibliote do TKINTER

def calculo(): #Cria a função do calculo quando o botao CALCULAR for acionado
    nome = entrada_nome.get() #Armazena na variavel o nome digitado
    temp = float(entrada_temp.get()) #Armazena na variavel a temperatura digitado
    calculo = 5 * (temp-32)/9 #Faz a Conversão para Celsius
    calculo_r = round(calculo, 2) #Limita para 2 casas decimais
    var = "Olá",nome #Informa ao usuario o nome
    var2 = 'Sua Temperatura é:',calculo_r,"ºC" #Informa ao usuario a temperatura convertida
    resultado.config(text=var) #Altera o texto da variavel com a resposta
    resultado2.config(text=var2)  #Altera o texto da variavel com a resposta
    entrada_nome.delete(0, END) #Limpa o input apos o uso
    entrada_temp.delete(0, END) #Limpa o input apos o uso

def limpa_tela(): #Cria a função de limpar a tela quando o botao LIMPAR for acionado
    entrada_temp.delete(0, END) #Limpa o Input da temperatura
    entrada_nome.delete(0, END) #Limpa o Input do nome


janela = Tk() #Cria uma variavel para janela

janela.title('Conversor de Temperatura') #Cria o nome na aba do programa
janela.geometry("900x600") #Define o tamanho da janela
janela.resizable(True, True) #Define se eu posso ou não aumentar ou diminuir a janela Horizontal e Vertical
janela.maxsize(width=1200, height=1000) #Define o tamanho maximo da janela
janela.minsize(width=700, height=400) #Define o tamanho minimo da janela

bloco1 = Frame(janela, bg="gainsboro", highlightbackground="black", highlightthickness=3) #Cria uma região retangular na janela - (background, cor da linha, largura da linha)  da região
bloco1.place(relx=0.02, rely=0.04, relwidth=0.96, relheight=0.92) #Define a posição da região retangular

saudacao = Label(text="Bem - Vindo à Conversão de Temperatura", bg="gainsboro", font= ('arial',11, 'bold')) #Cria o texto de SAUDAÇÃO
saudacao.place(relx=0.3, rely=0.12) #Define a posição do texto

inicializacao = Label(text="Nós vamos converter a temperatura de Fahrenheit para ºC", bg="gainsboro", font= ('sansserif',11, 'bold')) #Cria o texto de INICIALIZAÇÂO
inicializacao.place(relx=0.25, rely=0.2, ) #Define a posição do texto

nome = Label(text="Qual o seu Nome?", bg="gainsboro", font= ('arial',9, 'bold')) #Cria o texto de NOME
nome.place(relx=0.06, rely=0.33) #Define a posição do texto
entrada_nome = Entry() #Cria o input de nome
entrada_nome.place(relx= 0.06, rely=0.38, relheight=0.05, relwidth=0.78) #Define a posição do input

temp = Label(text="Qual a temperatura em Fahrenheit?", bg="gainsboro", font= ('arial',9, 'bold')) #Cria o texto de TEMPERATURA
temp.place(relx=0.06, rely=0.48) #Define a posição do texto
entrada_temp = Entry() #Cria o input de TEMPERATURA
entrada_temp.place(relx= 0.06, rely=0.53, relheight=0.05, relwidth=0.30) #Define a posição do input

botaoCalcular = Button(text="Calcular", bd=3, fg="black", font= ('arial',11, 'bold'), command=calculo) #Cria um botão de CALCULAR
botaoCalcular.place(relx=0.35, rely=0.63, relwidth=0.12, relheight=0.1) #Define a posição do botão

botaoLimpar = Button(text="Limpar", bd=3, fg="black", font= ('arial',11, 'bold'), command=limpa_tela) #Cria um botão de LIMPAR
botaoLimpar.place(relx=0.5, rely=0.63, relwidth=0.12, relheight=0.1) #Define a posição do botão

resultado = Label(text="", bg="gainsboro", font= ('arial',11, 'bold')) #Cria um espaço para a resposta ao usuario
resultado.place(relx=0.43, rely=0.8) #Define a posição da resposta

resultado2 = Label(text="", bg="gainsboro", font=('arial',11, 'bold')) #Cria um espaço para a resposta ao usuario
resultado2.place(relx=0.33, rely=0.85) #Define a posição da resposta

janela.mainloop() #Cria um loop da janela