from tkinter import messagebox, Tk, Label, Entry, PhotoImage, Button #Importa a bibliote do TKINTER
import emoji #Importa a Biblioteca de EMOJIS
from datetime import * #Importa a Biblioteca de Data e Hora
from qrcode import make #Importa a Biblioteca de QRCODE


def qrcode(): #Cria a função QRCODE
    link = entrada.get()  #Armazena o link que o usuario envia
    imagem = make(link) #Converte a imagem no qrcode
    type(imagem) #Define o tipo da imagem
    imagem.save(dataformatada) #Salva a imagem com data e hora atual    
    messagebox.askokcancel("Aviso", message=emoji.emojize(" :OK_hand: Concluído")) #Mensagem de Sucesso

atual = datetime.now() #Cria a variavel da data e hora atual
formato = "%d%m%Y%H%M.png" #Define o formato da data e da hora + .png no final
dataformatada = atual.strftime(formato) #armazena a data formatada na variavel


fundo = Tk() 
fundo.title(emoji.emojize(":desktop_computer: TESTE"))
background = PhotoImage(file="18 - 11\Aula 18 - 11\imagem.png")
janela = Label(fundo, image=background).pack()

texto = Label(janela, text="Insira o Link para gerar seu QRCODE ") # Cria um rótulo (Label) na janela para exibir um texto

imagem_label = Label(fundo, image=background)
imagem_label.place(relwidth=1, relheight=1)

entrada = Entry(width=50)
entrada.place(relx=0.5, rely=0.5, anchor="center")

entrada.focus()

texto = Label(janela, text="Insira o Link para gerar seu QRCODE ") # Cria um rótulo (Label) na janela para exibir um texto
texto.place(relx=0.5, rely=0.3, anchor="center")

botao = Button(fundo, text=" Gerar Link ", command=qrcode)
botao.place(relx=0.5, rely=0.7, anchor="center")

fundo.mainloop()