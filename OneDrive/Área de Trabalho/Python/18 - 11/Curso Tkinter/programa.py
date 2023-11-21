from tkinter import * #Importa a Biblioteca Tkinter
from tkinter import ttk

janela = Tk() #Cria uma variavel para janela

class Func():
    def limpa_tela(self):
        self.entrada_codigo.delete(0, END)
        self.entrada_nome.delete(0, END)
        self.entrada_telefone.delete(0, END)
        self.entrada_cidade.delete(0, END)


class Application(Func):
    def __init__(self):
        self.janela()
        self.blocos()
        self.botao()
        self.entradas()
        self.lista()
        janela.mainloop() #Cria um loop da janela

    def blocos(self): #Cria uma função para os blocos dentro da janela
        self.bloco1 = Frame(janela, bg="gainsboro", highlightbackground="black", highlightthickness=3) #Cria uma região retangular na janela - (background, cor da linha, largura da linha)  da região
        self.bloco1.place(relx=0.02, rely=0.04, relwidth=0.96, relheight=0.46) #Define a posição da região retangular
        self.bloco2 = Frame(janela, bg="gainsboro", highlightbackground="black", highlightthickness=3) #Cria uma região retangular na janela - (background, cor da linha, largura da linha)  da região
        self.bloco2.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46) #Define a posição da região retangular

    def botao(self): #Cria a função para os botões
        self.botaoLimpar = Button(text="Limpar", background="deepskyblue", bd=3, fg="black", font= ('sansserif',9, 'bold'), command=self.limpa_tela) #Cria um botão (Texto do botão, background)
        self.botaoLimpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.07) #Define a posição do botão
        self.botaoBuscar = Button(text="Buscar", background="deepskyblue", bd=3, fg="black", font= ('sansserif',9, 'bold')) #Cria um botão (Texto do botão, background)
        self.botaoBuscar.place(relx=0.31, rely=0.1, relwidth=0.1, relheight=0.07) #Define a posição do botão
        self.botaoNovo = Button(text="Novo", background="deepskyblue", bd=3, fg="black", font= ('sansserif',9, 'bold')) #Cria um botão (Texto do botão, background)
        self.botaoNovo.place(relx=0.52, rely=0.1, relwidth=0.1, relheight=0.07) #Define a posição do botão
        self.botaoAltertar = Button(text="Alterar", background="deepskyblue", bd=3, fg="black", font= ('sansserif',9, 'bold')) #Cria um botão (Texto do botão, background)
        self.botaoAltertar.place(relx=0.63, rely=0.1, relwidth=0.1, relheight=0.07) #Define a posição do botão
        self.botaoApagar = Button(text="Apagar", background="deepskyblue", bd=3, fg="black", font= ('sansserif',9, 'bold')) #Cria um botão (Texto do botão, background)
        self.botaoApagar.place(relx=0.74, rely=0.1, relwidth=0.1, relheight=0.07) #Define a posição do botão

    def entradas(self): #Cria a função para os INPUT
        self.codigo = Label(text="Código", bg="gainsboro", font= ('sansserif',9, 'bold')) #Cria o texto de CÓDIGO
        self.codigo.place(relx=0.09, rely=0.06) #Define a posição do texto
        self.entrada_codigo = Entry() #Cria o input de código
        self.entrada_codigo.place(relx= 0.06, rely=0.115, relheight=0.05, relwidth=0.12) #Define a posição do input
        self.nome = Label(text="Nome", bg="gainsboro", font= ('sansserif',9, 'bold')) #Cria o texto de NOME
        self.nome.place(relx=0.09, rely=0.2) #Define a posição do texto
        self.entrada_nome = Entry() #Cria o input de nome
        self.entrada_nome.place(relx= 0.06, rely=0.25, relheight=0.05, relwidth=0.78) #Define a posição do input
        self.telefone = Label(text="Telefone", bg="gainsboro", font= ('sansserif',9, 'bold')) #Cria o texto de TELEFONE
        self.telefone.place(relx=0.09, rely=0.32) #Define a posição do texto
        self.entrada_telefone = Entry() #Cria o input de Telefone
        self.entrada_telefone.place(relx= 0.06, rely=0.37, relheight=0.05, relwidth=0.30) #Define a posição do input
        self.cidade = Label(text="Cidade", bg="gainsboro", font= ('sansserif',9, 'bold')) #Cria o texto de CIDADE
        self.cidade.place(relx=0.43, rely=0.32) #Define a posição do texto
        self.entrada_cidade = Entry() #Cria o input da cidade
        self.entrada_cidade.place(relx= 0.40, rely=0.37, relheight=0.05, relwidth=0.44) #Define a posição do input
 
    def lista(self): #Cria a função para a LISTA
        self.listaclientes = ttk.Treeview(height=3, columns=("col1", "col2", "col3", "col4", )) #Cria uma lista com 4 colunas
        self.listaclientes.heading("#0", text="") #Define os textos da coluna 0
        self.listaclientes.heading("#1", text="Código") #Define os textos da coluna 1
        self.listaclientes.heading("#2", text="Nome") #Define os textos da coluna 2
        self.listaclientes.heading("#3", text="Telefone") #Define os textos da coluna 3
        self.listaclientes.heading("#4", text="Cidade") #Define os textos da coluna 4
        self.listaclientes.column("#0", width=1) #Define o tamanho da coluna 0
        self.listaclientes.column("#1", width=50) #Define o tamanho da coluna 1
        self.listaclientes.column("#2", width=200) #Define o tamanho da coluna 2
        self.listaclientes.column("#3", width=100) #Define o tamanho da coluna 3
        self.listaclientes.column("#4", width=200) #Define o tamanho da coluna 4
        self.listaclientes.place(relx= 0.04, rely=0.55, relheight=0.40, relwidth=0.9) #Define a posição da lista na janela
        self.scroolLista = Scrollbar(orient="vertical") #Cria a rolagem da lista
        self.scroolLista.place(relx= 0.94, rely=0.55, relheight=0.40, relwidth=0.03) #Define a posição da Rolagem

    def janela(self):
        self.janela=janela
        self.janela.title('Cadastro de Clientes') #Cria o nome na aba do programa
        self.janela.configure(background="darkslategray") #Define a cor de fundo da janela do programa
        self.janela.geometry("700x400") #Define o tamanho da janela
        self.janela.resizable(True, True) #Define se eu posso ou não aumentar ou diminuir a janela Horizontal e Vertical
        self.janela.maxsize(width=900, height=700) #Define o tamanho maximo da janela
        self.janela.minsize(width=600, height=300) #Define o tamanho minimo da janela


Application()
