from tkinter import *
import datetime
from tkinter import messagebox, simpledialog
from datetime import timedelta
import sqlite3




data=datetime.datetime.now()
formatoData = "%d/%m/%y"
dataf = data.strftime(formatoData)
formatodia="%d"
dia = data.strftime(formatodia)
formatoHora = "%H:%M"
horaf = data.strftime(formatoHora)


janela = Tk()



class Func():

    def conecta_bd(self):
        self.conn = sqlite3.connect("banco.bd")
        self.cursor = self.conn.cursor(); print("Conectando ao Banco de Dados")

    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao Banco de Dados")

    def montaTabelas(self):
        self.conecta_bd()
        ### Criar Tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS banco (
                cod INTEGER PRIMARY KEY,
                nome CHAR(40) NOT NULL,
                usuario INTEGER(20) UNIQUE NOT NULL,
                telefone CHAR(40) NOT NULL,
                email CHAR(50) UNIQUE NOT NULL,
                senha CHAR(10) NOT NULL,
                saldo REAL DEFAULT 0.0
            );
        """)
        self.conn.commit(); print("Banco de Dados Criado")
        self.desconecta_bd()

    def limpa_tela(self):
        self.entrada_nome.delete(0, END) #Deleta os caracteres digitados no campo código
        self.entrada_usuario.delete(0, END) #Deleta os caracteres digitados no campo código
        self.entrada_telefone.delete(0, END) #Deleta os caracteres digitados no campo código
        self.entrada_email.delete(0, END) #Deleta os caracteres digitados no campo código
        self.entrada_senha.delete(0, END) #Deleta os caracteres digitados no campo código

    def limpa_tela_login(self):
        self.entrada_usuariologin.delete(0,END)
        self.entrada_senhalogin.delete(0,END)

    def esconder_senha(self):
        self.esconder_senha = StringVar()

    def cadastrar_usuario(self):
        nome = self.entrada_nome.get()
        usuario = self.entrada_usuario.get()
        telefone = self.entrada_telefone.get()
        email = self.entrada_email.get()
        senha = self.entrada_senha.get()
        
        self.conn = sqlite3.connect('banco.bd')
        self.cursor = self.conn.cursor()

        try:
            # Inserir os dados do usuário na tabela de usuários
            self.cursor.execute('INSERT INTO banco (nome, usuario, telefone, email, senha) VALUES (?, ?, ?, ?, ?)', (nome, usuario, telefone, email, senha))
            # Confirmar as alterações no banco de dados
            self.conn.commit(); print("Cadastro realizado")
            self.limpa_tela()
            # Exibir mensagem de sucesso
            messagebox.showinfo('Cadastro', 'Cadastro realizado com sucesso!')
        except sqlite3.IntegrityError:
            # Se o e-mail já estiver cadastrado, exibir mensagem de erro
            messagebox.showerror('Erro', 'E-mail/Usuário já cadastrado!')

        # Fechar a conexão com o banco de dados
        self.desconecta_bd()

    def login(self):
        self.usuariologin = self.entrada_usuariologin.get()
        self.senhalogin = self.entrada_senhalogin.get()
        self.conn = sqlite3.connect('banco.bd')
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT * FROM banco WHERE usuario=? AND senha=?', (self.usuariologin, self.senhalogin))
        self.usuarioBanco = self.cursor.fetchone()
        self.desconecta_bd()
        

        if self.usuarioBanco:
            if self.usuarioBanco[6] != 0.0:
                self.paginaPrincipal()

            else:
                self.entrada_usuariologin.delete(0, END)
                self.entrada_senhalogin.delete(0, END)
                self.saldoentry= float(simpledialog.askstring('Saldo', 'Informe o saldo da sua conta:'))
                self.conn = sqlite3.connect('banco.bd')
                self.cursor = self.conn.cursor()
                self.cursor.execute('UPDATE banco SET saldo=? WHERE cod=?', (self.saldoentry, self.usuarioBanco[0]))
                self.conn.commit(); print("SALDO CADASTRADO LOGIN")
                self.paginaPrincipal()
                

        else:
            self.limpa_tela_login()
            messagebox.showerror('Erro', 'Usuário/Senha Inválidas.')

    def compra(self):
        self.saldo=Toplevel()
        self.saldo.title("Compra")
        self.saldo.geometry("400x250") #Define o tamanho da janela
        self.saldo.resizable(False, False) #Define se eu posso ou não aumentar ou diminuir a janela Horizontal e Vertical
        self.textsaldo = Label(self.saldo, text="Informe o valor gasto no dia {}".format(dia), font= ('arial',12, 'bold'))
        self.textsaldo.place(relx=0.25, rely=0.2)
        self.botaook = Button(self.saldo, text="OK", bd=3, fg="black", font= ('sansserif',10,), command=self.extrato)
        self.botaook.place(relx=0.38, rely=0.6, relwidth=0.2, relheight=0.15) #Define a posição do botão
        self.entrada_compra = Entry(self.saldo)
        self.entrada_compra.place(relx=0.25, rely=0.4, relwidth=0.5, relheight=0.12)
        
    def paginaPrincipal(self):
        saldo = self.usuarioBanco[6]
        self.limpa_tela_login()
        self.limite = saldo * 0.5
        self.pagina_principal=Toplevel()
        self.pagina_principal.title('Página Principal') #Cria o nome na aba do programa
        self.pagina_principal.geometry("500x900") #Define o tamanho da janela
        self.pagina_principal.resizable(False, False) #Define se eu posso ou não aumentar ou diminuir a janela Horizontal e Vertical
        self.bloco1 = Frame(self.pagina_principal, bg="red3")
        self.bloco1.place(relx=0.00, rely=0.00, relwidth=1, relheight=0.2) #Define a posição da região retangular
        self.senai = Label(self.pagina_principal, text="SENAI", bg="red3", fg="white", font= ('arial',50, 'bold')) #Cria o texto de CÓDIGO
        self.senai.place(relx=0.3, rely=0.06) #Define a posição do texto
        self.banco = Label(self.pagina_principal, text="Banco", bg="red3", fg="white", font= ('arial',16, 'bold')) #Cria o texto de CÓDIGO
        self.banco.place(relx=0.45, rely=0.04) #Define a posição do texto
        self.botaocadastrar = Button(self.pagina_principal, text="Sair", bd=3, fg="black", font= ('sansserif',10,), command=self.pagina_principal.destroy) #Cria um botão (Texto do botão, background)
        self.botaocadastrar.place(relx=0.52, rely=0.86, relwidth=0.2, relheight=0.05) #Define a posição do botão
        self.botaocomprar = Button(self.pagina_principal, text="Comprar", bd=3, fg="black", font= ('sansserif',10,), command=self.compra) #Cria um botão (Texto do botão, background)
        self.botaocomprar.place(relx=0.28, rely=0.86, relwidth=0.2, relheight=0.05) #Define a posição do botão
        self.blocoData = Frame(self.pagina_principal, bg="gray71", highlightbackground="black", highlightthickness=3 )
        self.blocoData.place(relx=0.04, rely=0.25, relheight=0.13, relwidth=0.25, )
        self.text = Label(self.pagina_principal, text="Data", bg="gray71", fg="black", font= ('arial',10, 'bold'))
        self.text.place(relx=0.12, rely=0.257, relwidth=0.1, relheight=0.02)
        self.data = Label(self.pagina_principal, text=dataf, bg="gray71", fg="white", font= ('arial',16, 'bold'))
        self.data.place(relx=0.06, rely=0.285, relwidth=0.2, relheight=0.03)
        self.hora = Label(self.pagina_principal, text=horaf, bg="gray71", fg="white", font= ('arial',16, 'bold'))
        self.hora.place(relx=0.06, rely=0.325, relwidth=0.2, relheight=0.03)
        self.blocoSaldo = Frame(self.pagina_principal, bg="gray71", highlightbackground="black", highlightthickness=3, )
        self.blocoSaldo.place(relx=0.37, rely=0.25, relheight=0.13, relwidth=0.25, )
        self.textSaldo = Label(self.pagina_principal, text="Saldo", bg="gray71", fg="black", font= ('arial',10, 'bold'))
        self.textSaldo.place(relx=0.45, rely=0.257, relwidth=0.1, relheight=0.02)
        self.textsaldoRs = Label(self.pagina_principal, text="R$", bg="gray71", fg="white", font= ('arial',16, 'bold'))
        self.textsaldoRs.place(relx=0.38, rely=0.3, relwidth=0.05, relheight=0.03)
        self.textvarsaldo = Label(self.pagina_principal, text=self.usuarioBanco[6], bg="gray71", fg="white", font= ('arial',16, 'bold'))
        self.textvarsaldo.place(relx=0.43, rely=0.3, relwidth=0.18, relheight=0.03)
        self.blocoLimite = Frame(self.pagina_principal, bg="gray71", highlightbackground="black", highlightthickness=3)
        self.blocoLimite.place(relx=0.7, rely=0.25, relheight=0.13, relwidth=0.25, )
        self.textLimite = Label(self.pagina_principal, text="Limite", bg="gray71", fg="black", font= ('arial',10, 'bold'))
        self.textLimite.place(relx=0.78, rely=0.257, relwidth=0.1, relheight=0.02)
        self.textlimiteRs = Label(self.pagina_principal, text="R$", bg="gray71", fg="white", font= ('arial',16, 'bold'))
        self.textlimiteRs.place(relx=0.71, rely=0.3, relwidth=0.05, relheight=0.03)
        self.textvarlimit = Label(self.pagina_principal, text=self.limite, bg="gray71", fg="white", font= ('arial',16, 'bold'))
        self.textvarlimit.place(relx=0.76, rely=0.3, relwidth=0.18, relheight=0.03)
        self.blocoextrato = Frame(self.pagina_principal, bg="white", highlightthickness=3, highlightbackground="black")
        self.blocoextrato.place(relx=0.05, rely=0.43, relwidth=0.9, relheight=0.38) #Define a posição da região retangular
        self.textextrato = Label(self.pagina_principal, text="Extrato", font= ('arial', '10', 'bold'), bg="white")
        self.textextrato.place(relx=0.07, rely=0.44)
        self.scroolLista = Scrollbar(self.pagina_principal ,orient="vertical") #Cria a rolagem da lista
        self.scroolLista.place(relx= 0.91, rely=0.435, relheight=0.37, relwidth=0.03) #Define a posição da Rolagem

        
class Application(Func):

    def __init__(self):
        self.janela()
        self.blocos()
        self.botao()
        self.entradas_bloco1()
        self.entradas_bloco2()
        self.entradas_bloco3()
        self.montaTabelas()
        janela.mainloop()   

    def janela(self):
        self.janela = janela
        self.janela.title('Pagina Login') #Cria o nome na aba do programa
        self.janela.geometry("500x900") #Define o tamanho da janela
        self.janela.resizable(False, False) #Define se eu posso ou não aumentar ou diminuir a janela Horizontal e Vertical

    def blocos(self):
        self.bloco1 = Frame(janela, bg="red3")
        self.bloco1.place(relx=0.00, rely=0.00, relwidth=1, relheight=0.2) #Define a posição da região retangular
        self.bloco2 = Frame(janela, bg="red3")
        self.bloco2.place(relx=0.1, rely=0.22, relwidth=0.8, relheight=0.31) #Define a posição da região retangular
        self.bloco3 = Frame(janela, bg="red3")
        self.bloco3.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.42) #Define a posição da região retangular
        
    def entradas_bloco1(self):
        self.senai = Label(text="SENAI", bg="red3", fg="white", font= ('arial',50, 'bold')) #Cria o texto de CÓDIGO
        self.senai.place(relx=0.3, rely=0.06) #Define a posição do texto
        self.banco = Label(text="Banco", bg="red3", fg="white", font= ('arial',16, 'bold')) #Cria o texto de CÓDIGO
        self.banco.place(relx=0.45, rely=0.04) #Define a posição do texto

    def entradas_bloco2(self):
        self.login = Label(text="Faça seu Login", bg="red3", fg="white", font= ('arial',12, 'bold')) #Cria o texto de CÓDIGO
        self.login.place(relx=0.38, rely=0.24) #Define a posição do texto
        self.usuariologin = Label(text="Usuário", bg="red3", fg="white", font= ('arial',12, 'bold')) #Cria o texto de CÓDIGO
        self.usuariologin.place(relx=0.15, rely=0.29) #Define a posição do texto
        self.entrada_usuariologin = Entry() #Cria o input de código
        self.entrada_usuariologin.place(relx= 0.3, rely=0.29, relheight=0.03, relwidth=0.4) #Define a posição do input
        self.senhalogin = Label(text="Senha", bg="red3", fg="white", font= ('arial',12, 'bold')) #Cria o texto de CÓDIGO
        self.senhalogin.place(relx=0.15, rely=0.35) #Define a posição do texto
        self.entrada_senhalogin = Entry(textvariable=self.esconder_senha, show="*") #Cria o input de código
        self.entrada_senhalogin.place(relx= 0.3, rely=0.35, relheight=0.03, relwidth=0.4) #Define a posição do input
        self.msglogin = Label(text="", bg="red3", fg="yellow", font= ('arial',12, 'bold')) #Cria o texto de CÓDIGO
        self.msglogin.place(relx=0.28, rely=0.48, relwidth=0.5, relheight=0.05) #Define a posição do texto

    def entradas_bloco3(self):
        self.cadastro = Label(text="Faça seu Cadastro", bg="red3", fg="white", font= ('arial',12, 'bold')) #Cria o texto de CÓDIGO
        self.cadastro.place(relx=0.38, rely=0.57) #Define a posição do texto
        self.nome = Label(text="Nome", bg="red3", fg="white", font= ('arial',12, 'bold')) #Cria o texto de CÓDIGO
        self.nome.place(relx=0.15, rely=0.61) #Define a posição do texto
        self.entrada_nome = Entry() #Cria o input de código
        self.entrada_nome.place(relx= 0.3, rely=0.61, relheight=0.03, relwidth=0.4) #Define a posição do input
        self.usuario = Label(text="Usuario", bg="red3", fg="white", font= ('arial',12, 'bold')) #Cria o texto de CÓDIGO
        self.usuario.place(relx=0.15, rely=0.66) #Define a posição do texto
        self.entrada_usuario = Entry() #Cria o input de código
        self.entrada_usuario.place(relx= 0.3, rely=0.66, relheight=0.03, relwidth=0.4) #Define a posição do input
        self.telefone = Label(text="Telefone", bg="red3", fg="white", font= ('arial',12, 'bold')) #Cria o texto de CÓDIGO
        self.telefone.place(relx=0.15, rely=0.71) #Define a posição do texto
        self.entrada_telefone = Entry() #Cria o input de código
        self.entrada_telefone.place(relx= 0.3, rely=0.71, relheight=0.03, relwidth=0.4) #Define a posição do input
        self.email = Label(text="E-mail", bg="red3", fg="white", font= ('arial',12, 'bold')) #Cria o texto de CÓDIGO
        self.email.place(relx=0.15, rely=0.76) #Define a posição do texto
        self.entrada_email = Entry() #Cria o input de código
        self.entrada_email.place(relx= 0.3, rely=0.76, relheight=0.03, relwidth=0.4) #Define a posição do input
        self.senha = Label(text="Senha", bg="red3", fg="white", font= ('arial',12, 'bold')) #Cria o texto de CÓDIGO
        self.senha.place(relx=0.15, rely=0.81) #Define a posição do texto
        self.entrada_senha = Entry(textvariable=self.esconder_senha, show="*") #Cria o input de código
        self.entrada_senha.place(relx= 0.3, rely=0.81, relheight=0.03, relwidth=0.4) #Define a posição do input
        self.msg = Label(text="", bg="red3", fg="yellow", font= ('arial',12, 'bold')) #Cria o texto de CÓDIGO
        self.msg.place(relx=0.26, rely=0.92, relwidth=0.52, relheight=0.05) #Define a posição do texto

    def botao(self):
        self.botaologar = Button(text="Login", bd=3, fg="black", font= ('sansserif',10,), command=self.login) #Cria um botão (Texto do botão, background)
        self.botaologar.place(relx=0.4, rely=0.42, relwidth=0.2, relheight=0.05) #Define a posição do botão
        self.botaocadastrar = Button(text="Cadastrar", bd=3, fg="black", font= ('sansserif',10,), command=self.cadastrar_usuario) #Cria um botão (Texto do botão, background)
        self.botaocadastrar.place(relx=0.4, rely=0.86, relwidth=0.2, relheight=0.05) #Define a posição do botão

Application()