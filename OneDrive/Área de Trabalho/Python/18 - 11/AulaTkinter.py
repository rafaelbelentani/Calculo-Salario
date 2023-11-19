from tkinter import messagebox, Tk, Label, Entry, PhotoImage, Button
import emoji
from datetime import * #Importa a Biblioteca de Data e Hora
from qrcode import make


def qrcode():
    link = entrada.get()
    imagem = make(link) #Converte a imagem no qrcode
    type(imagem)
    imagem.save(dataformatada) #Salva a imagem com data e hora atual    
    messagebox.askokcancel("Aviso", message=emoji.emojize(" :OK_hand: Concluído"))

atual = datetime.now() #Cria a variavel da data e hora atual
formato = "%d%m%Y%H%M.png" #Define o formato da data e da hora + .png no final
dataformatada = atual.strftime(formato) #armazena a data formatada na variavel


fundo = Tk()
fundo.title(emoji.emojize(":desktop_computer: TESTE"))
background = PhotoImage(file="imagem.png")
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