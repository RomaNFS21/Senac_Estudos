from tkinter import *
import tkinter as tk

janela=Tk()
janela.title("App System")

# Forma de definir cor do background 1
#janela['bg']='lightgreen'

# Forma de definir cor do background 2
janela.configure(bg="#22b65b")

# Forma de definir tamanho da janela 1
#janela.minsize(width=400,height=400)
#janela.maxsize(width=800,height=600)

# Forma de definir o tamanho da janela 2
janela.geometry('800x600+150+100')
'''
nome=tilte=tk.Label(janela, text='Bem vindo ao programa',
font=('Verdana', 25, "bold"),
bg='lightblue',height=2,width=35,relief='groove',fg="black")

botao=tk.Button(janela,text="Entrar", font=('Arial',25), bg="red")
botao.place(x=450,y=200)
botao1=tk.Button(janela,text="Enviar", font=('Arial',25), bg="purple")
botao1.place(x=750,y=200)

nome.place(x=250,y=20)'''

#################################### ESTILO DE BORDAS #################################
# relief flat, raised , sunken, groove , ridge
'''
nome1=tk.Label(janela,text='Borda Groove',relief="groove")
nome1.place(x=100,y=500)
nome2=tk.Label(janela,text='Borda Flat',relief="flat")
nome2.place(x=200,y=500)
nome3=tk.Label(janela,text='Borda Raised',relief="raised")
nome3.place(x=300,y=500)
nome4=tk.Label(janela,text='Borda Sunken',relief="sunken")
nome4.place(x=400,y=500)
nome5=tk.Label(janela,text='Borda Ridge',relief="ridge")
nome5.place(x=500,y=500)
'''
#################################### CAIXA DE TEXTO #####################################
'''
entrada1 = tk.Entry(janela)  # aplica um campo de largura padrao
entrada1.pack()
entrada1.place(x=400,y=150)
entrada2 = tk.Entry(janela,width=30) # aplica um campo com largura de tamanho 30
entrada2.pack()
entrada2.place(x=400,y=300)
'''

email = tk.Label(janela,text= "EMAIL", relief= "flat")
email.place(x=300,y=100)
entrada_email = tk.Entry(janela, width= 100)
entrada_email.pack()
entrada_email.place(x=350,y=100)

senha = tk.Label(janela,text= "SENHA", relief= "flat")
senha.place(x=300,y=200)
entrada_senha = tk.Entry(janela, width= 100)
entrada_senha.pack()
entrada_senha.place(x=350,y=200)

botao=tk.Button(janela,text="Entrar", font=('Arial',25), bg="white")
botao.place(x=600,y=300)

mainloop()