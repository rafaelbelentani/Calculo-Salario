import qrcode  #Importa a Biblioteca de QRCODE
from datetime import * #Importa a Biblioteca de Data e Hora

atual = datetime.now() #Cria a variavel da data e hora atual
formato = "%d%m%Y%H%M.png" #Define o formato da data e da hora + .png no final
dataformatada = atual.strftime(formato) #armazena a data formatada na variavel

print("Envie o Link do seu QrCode") #Pede que o usuario envio o link a ser criado
img = str(input(" ")) #Armazena o link na Variavel
imagem = qrcode.make(img) #Converte a imagem no qrcode
imagem.save(dataformatada) #Salva a imagem com data e hora atual
print("\t Seu QrCode foi Criado com sucesso") #Informa ao usuario que foi concluido