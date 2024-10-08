from tkinter import *
import tkinter as tk

janela=Tk()
janela.title('Projeto')
janela['bg']=('lightblue')
janela.geometry('300x200+550+150')
janela.resizable(width=False, height=False)
'''
label = tk.Label(janela, text = 'DIGITE AQUI' , font=('Arial',9,'bold'), bg = 'lightblue')
label.place(x=10,y=10)

entrada = tk.Entry(janela, width=30)
entrada.place(x=90,y=10)

botao=tk.Button(janela,text='Botão', font=('Arial',9,'bold'),width=30)
botao.place(x=50,y=40)
'''
##########################
'''
bt1 = Button(janela, text='Botão 1', bg="#2689f1")
bt1.pack(side=LEFT)
bt2 = Button(janela, text='Botão 2', bg="#fb352b")
bt2.pack(side=TOP)
bt3 = Button(janela, text='Botão 3', bg="#d8d416")
bt3.pack(side=RIGHT)
bt4= Button(janela, text='Botão 4', bg="#22b65b")
bt4.pack(side=BOTTOM)
bt5= Button(janela, text='Botão 5', bg="#ffffff")
bt5.pack(anchor=CENTER)
'''
#########################
'''
bt1 = Button(janela, text='ESQUERDA', bg="#2689f1")
bt1.pack(anchor=E)
bt2 = Button(janela, text='CIMA', bg="#fb352b")
bt2.pack(anchor=N)
bt3 = Button(janela, text='DIREITA', bg="#d8d416")
bt3.pack(anchor=E)
bt4= Button(janela, text='BAIXO', bg="#22b65b")
bt4.pack(anchor=S)
bt5= Button(janela, text='CENTRO', bg="#ffffff")
bt5.pack(anchor=CENTER)
'''
########################
'''
bt1 = Button(janela, text='BOTÃO 1', bg="#2689f1")
bt1.pack(side= TOP , fill=BOTH)
bt2 = Button(janela, text='BOTÃO 2', bg="#fb352b")
bt2.pack(side= BOTTOM, fill=BOTH)
bt3 = Button(janela, text='BOTÃO 3', bg="#d8d416")
bt3.pack(side=RIGHT, fill=BOTH)
bt4= Button(janela, text='BOTÃO 4', bg="#22b65b")
bt4.pack(side=LEFT, fill=BOTH)
'''
#######################

bt1 = Button(janela, text='BOTÃO 1', bg="#2689f1")
bt1.pack(fill=BOTH, expand=True)
bt2 = Button(janela, text='BOTÃO 2', bg="#fb352b")
bt2.pack(fill=BOTH, expand=False)
bt3 = Button(janela, text='BOTÃO 3', bg="#d8d416")
bt3.pack(fill=BOTH, expand=1)
bt4= Button(janela, text='BOTÃO 4', bg="#22b65b")
bt4.pack(fill=BOTH, expand=0)

janela.mainloop()