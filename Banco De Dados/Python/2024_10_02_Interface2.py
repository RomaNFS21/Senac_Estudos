import tkinter as tk
from tkinter import *
from tkinter import messagebox


janela = Tk() #Criando a janela
janela.title("Eventos nos botões") # Título da janela
janela.geometry("400x400+540+150")
'''
def resposta(event):
    messagebox.showinfo("caixa de mensagem","evento de clique")

Label=tk.Label(janela,text="Abrir caixa", relief="raised")
Label.pack(pady=20)
Label.bind("<Button-1>",resposta)

janela.mainloop()
'''

def resposta(event):
    messagebix.showinfo(title: 'caixa de mensagem')

label = Label(janela,text="Abrir caixa", relief="raised")
label.pack(pady=20)

Label.bind("<Button-1>", resposta)
Label.bind("<Button-2>", resposta)
Label.bind("<Button-3>", resposta)
Label.bind("<Button-4>", resposta)
Label.bind("<Button-5>", resposta)

janela.mainloop()