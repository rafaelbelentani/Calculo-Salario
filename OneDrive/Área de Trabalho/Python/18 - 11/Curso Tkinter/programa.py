from tkinter import * #Importa a Biblioteca Tkinter
from tkinter import ttk
import pandas as pd
import sqlite3
from tkinter import messagebox

janela = Tk() #Cria uma variavel para janela


class Func():

    def limpa_tela(self): #Cria a Função de Limpar os campos da tela
        self.entrada_codigo.delete(0, END) #Deleta os caracteres digitados no campo código
        self.entrada_nome.delete(0, END) #Deleta os caracteres digitados no campo nome
        self.entrada_telefone.delete(0, END) #Deleta os caracteres digitados no campo telefone
        self.entrada_cidade.delete(0, END) #Deleta os caracteres digitados no campo cidade

    def conecta_bd(self):  #Cria a Função de conectar ao banco de dados
        self.conn = sqlite3.connect("clientes.bd") #Conecta o banco de dados com a tabela clientes
        self.cursor = self.conn.cursor(); print("Conectando ao Banco de Dados") #Conecta o banco de dados com a tabela clientes e imprime na tela

    def desconecta_bd(self): #Cria a Função de desconectar ao banco de dados
        self.conn.close(); print("Desconectando ao Banco de Dados") #Desconecta do banco de dados e imprime na tela

    def montaTabelas(self): #Cria a Função de criar a tabela do banco de dados
        self.conecta_bd() #Conecta ao banco de dados
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """) #Cria a tabela de clientes, caso ela não exista e insere uma chave primaria ao codigo do cliente
        self.conn.commit(); print("Banco de Dados Criado") #Cria a tabela e imprime na tela
        self.desconecta_bd() #Desconecta do banco de dados

    def variaveis(self): #Cria a função das variaveis de entrada
        self.codigo = self.entrada_codigo.get() #Armazena na variavel a entrada do codigo
        self.nome = self.entrada_nome.get() #Armazena na variavel a entrada do nome
        self.telefone = self.entrada_telefone.get() #Armazena na variavel a entrada do telefone
        self.cidade = self.entrada_cidade.get() #Armazena na variavel a entrada da cidade

    def select_list(self):  #Cria a função de atuzalizar a lista de clientes
        self.listaclientes.delete(*self.listaclientes.get_children()) 
        self.conecta_bd() #Conecta ao banco de dados
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """) #Seleciona as colunas em ordem crescente da tabela clientes
        for i in lista: #Cria uma estrutura de repetição
            self.listaclientes.insert("", END, values=i) 
        self.desconecta_bd() #Desconecta do banco de dados


    def cadastrar_cliente(self):  #Cria a Função de cadastrar clientes na tabela do banco de dados
        self.variaveis() #Chama as variaveis da função
        self.conecta_bd() #Conecta ao banco de dados
        
        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES(?, ?, ?)""", (self.nome, self.telefone, self.cidade)) #executa a função de inserir na tabela clientes os valores de cada coluna
        self.conn.commit() #Valida as informações no banco de dados
        self.desconecta_bd() #Desconecta do banco de dados
        self.select_list() #executa a função de atualizar a lista de clientes
        self.limpa_tela() #executa a função de limpar os dados da tela
        messagebox.showinfo("Cliente Cadastrado", "Cliente Cadastrado com Sucesso!") #cria uma caixa de mensagem de informação

    def DuploClick(self, event): #Cria uma função para utilizar o duplo clique
        self.limpa_tela() #Executa a função de limpar a tela
        self.listaclientes.selection() #seleciona as informações da lista
        
        for n in self.listaclientes.selection(): #Cria uma estrutura de repetição para extrair os dados da lista
            col1, col2, col3, col4 = self.listaclientes.item(n, 'values') #Numera as colunas da tabela
            self.entrada_codigo.insert(END, col1) #puxa as informações do codigo para o input
            self.entrada_nome.insert(END, col2) #puxa as informações do nome para o input
            self.entrada_telefone.insert(END, col3) #puxa as informações do telefone para o input
            self.entrada_cidade.insert(END, col4) #puxa as informações da cidade para o input

    def deleta_cliente(self): #Cria a função para deletar o cliente
        self.variaveis() #executa a função de chamar as variaveis
        self.conecta_bd() #Conecta ao banco de dados
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo)) #Executa a função de deletar o cliente selecionado da tabela clientes
        self.conn.commit() #Valida no banco de dados
        self.desconecta_bd() #Desconecta ao banco de dados
        self.limpa_tela() #limpa a tela
        self.select_list() #Atualiza a lista
        messagebox.showinfo("Cliente Deletado", "Cliente Deletado com Sucesso!") #Cria uma caixa de informação para o usuario


class Application(Func):
    def __init__(self):
        self.janela()
        self.blocos()
        self.botao()
        self.entradas()
        self.lista()
        self.montaTabelas()
        self.select_list()
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
        self.botaoNovo = Button(text="Novo", background="deepskyblue", bd=3, fg="black", font= ('sansserif',9, 'bold'), command=self.cadastrar_cliente) #Cria um botão (Texto do botão, background)
        self.botaoNovo.place(relx=0.52, rely=0.1, relwidth=0.1, relheight=0.07) #Define a posição do botão
        self.botaoAltertar = Button(text="Alterar", background="deepskyblue", bd=3, fg="black", font= ('sansserif',9, 'bold')) #Cria um botão (Texto do botão, background)
        self.botaoAltertar.place(relx=0.63, rely=0.1, relwidth=0.1, relheight=0.07) #Define a posição do botão
        self.botaoApagar = Button(text="Apagar", background="deepskyblue", bd=3, fg="black", font= ('sansserif',9, 'bold'), command=self.deleta_cliente) #Cria um botão (Texto do botão, background)
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
        self.listaclientes.bind("<Double-1>", self.DuploClick) #

    def janela(self): #Cria a função de criar uma janela
        self.janela=janela #Cria a janela
        self.janela.title('Cadastro de Clientes') #Cria o nome na aba do programa
        self.janela.configure(background="darkslategray") #Define a cor de fundo da janela do programa
        self.janela.geometry("700x400") #Define o tamanho da janela
        self.janela.resizable(True, True) #Define se eu posso ou não aumentar ou diminuir a janela Horizontal e Vertical
        self.janela.maxsize(width=900, height=700) #Define o tamanho maximo da janela
        self.janela.minsize(width=600, height=300) #Define o tamanho minimo da janela


Application()
