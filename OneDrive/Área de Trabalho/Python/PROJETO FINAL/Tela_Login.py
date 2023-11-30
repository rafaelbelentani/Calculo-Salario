from tkinter import *
import datetime

data=datetime.datetime.now()
formatoData = "%d/%m/%y"
dataf = data.strftime(formatoData)
formatoHora = "%H:%M"
horaf = data.strftime(formatoHora)



janela = Tk()

class Func():


    def esconder_senha(self):
        self.esconder_senha = StringVar()
        
    def login(self):
        
        self.usuariologin = self.entrada_usuariologin.get()
        self.senhalogin = self.entrada_senhalogin.get()
        self.usuario = "usuario"
        self.senha = "senha"
        
        if self.usuariologin==""  and self.senhalogin=="":
            self.mensagem = "Login Autorizado"
            self.msglogin.config(text=self.mensagem)
            self.entrada_usuariologin.delete(0, END)
            self.entrada_senhalogin.delete(0, END)
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
            self.botaocadastrar = Button(self.pagina_principal, text="Fechar", bd=3, fg="black", font= ('sansserif',10,), command=self.pagina_principal.destroy) #Cria um botão (Texto do botão, background)
            self.botaocadastrar.place(relx=0.4, rely=0.86, relwidth=0.2, relheight=0.05) #Define a posição do botão
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
            self.textvarsaldo = Label(self.pagina_principal, text="2.000,00", bg="gray71", fg="white", font= ('arial',16, 'bold'))
            self.textvarsaldo.place(relx=0.43, rely=0.3, relwidth=0.18, relheight=0.03)
            self.blocoLimite = Frame(self.pagina_principal, bg="gray71", highlightbackground="black", highlightthickness=3)
            self.blocoLimite.place(relx=0.7, rely=0.25, relheight=0.13, relwidth=0.25, )
            self.textLimite = Label(self.pagina_principal, text="Limite", bg="gray71", fg="black", font= ('arial',10, 'bold'))
            self.textLimite.place(relx=0.78, rely=0.257, relwidth=0.1, relheight=0.02)
            self.textlimiteRs = Label(self.pagina_principal, text="R$", bg="gray71", fg="white", font= ('arial',16, 'bold'))
            self.textlimiteRs.place(relx=0.71, rely=0.3, relwidth=0.05, relheight=0.03)
            self.textvarlimit = Label(self.pagina_principal, text="2.000,00", bg="gray71", fg="white", font= ('arial',16, 'bold'))
            self.textvarlimit.place(relx=0.76, rely=0.3, relwidth=0.18, relheight=0.03)

        else:
            self.mensagem = "ERRO! Usuário/Senha Inválido"
            self.msglogin.config(text=self.mensagem)
            self.entrada_usuariologin.delete(0, END)
            self.entrada_senhalogin.delete(0, END)

class Application(Func):

    def __init__(self):
        self.janela()
        self.blocos()
        self.botao()
        self.entradas_bloco1()
        self.entradas_bloco2()
        self.entradas_bloco3()
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
        self.entrada_senha = Entry() #Cria o input de código
        self.entrada_senha.place(relx= 0.3, rely=0.81, relheight=0.03, relwidth=0.4) #Define a posição do input
        self.msg = Label(text="", bg="red3", fg="yellow", font= ('arial',12, 'bold')) #Cria o texto de CÓDIGO
        self.msg.place(relx=0.26, rely=0.92, relwidth=0.52, relheight=0.05) #Define a posição do texto

    def botao(self):
        self.botaologar = Button(text="Login", bd=3, fg="black", font= ('sansserif',10,), command=self.login) #Cria um botão (Texto do botão, background)
        self.botaologar.place(relx=0.4, rely=0.42, relwidth=0.2, relheight=0.05) #Define a posição do botão
        self.botaocadastrar = Button(text="Cadastrar", bd=3, fg="black", font= ('sansserif',10,)) #Cria um botão (Texto do botão, background)
        self.botaocadastrar.place(relx=0.4, rely=0.86, relwidth=0.2, relheight=0.05) #Define a posição do botão


Application()