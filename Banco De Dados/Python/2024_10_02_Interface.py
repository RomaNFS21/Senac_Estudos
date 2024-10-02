import tkinter as tk
from tkinter import *

janela = Tk() #Criando a janela
janela.title("Eventos nos botões") # Título da janela
janela.geometry("400x400+540+150")

def mostrarTexto():
    mensagem['text'] = "Parabéns! realizou a primeira ação no botão" #Mensagem

botao=tk.Button(janela,text='Clique aqui', font=('Arial,12,"bold'), command=mostrarTexto)
botao.place(x=150,y=100)

mensagem = Label(janela, font=('Arial',12,"bold"))
mensagem.place(x=30,y=150)
janela.mainloop()
