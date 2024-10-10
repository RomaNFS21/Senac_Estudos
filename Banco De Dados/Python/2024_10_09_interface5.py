from importlib import reload
from tkinter import *
from tkinter import ttk
root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(bg="#132623")
        self.root.geometry("700x500")
        self.root.resizable(True,True)
        self.root.maxsize(width=900,height=700)
        self.root.minsize(width=400, height=300)

    def frames_da_tela(self):
        #Frame 1 em cima da pagina
        self.frame_1=Frame(self.root, bd=4 , bg="#173b5f", highlightbackground ="white", highlightthickness= 3)
        self.frame_1.place(relx=0.02, rely=0.02,relwidth = 0.96, relheight= 0.46)

        #Frame 2 em baixo da pagina
        self.frame_2 = Frame(self.root, bd=4, bg="#fb3329", highlightbackground="white", highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.46)

    def criando_botoes(self):

        #Botão de LIMPAR
        self.bt_limpar = Button(self.frame_1,text = "Limpar")
        self.bt_limpar.place(relx = 0.2 , rely = 0.2, relheight = 0.15)

        # Botão de BUSCAR
        self.bt_buscar = Button(self.frame_1, text = "Buscar")
        self.bt_buscar.place(relx = 0.3 , rely = 0.2, relheight = 0.15)

        # Botão de NOVO
        self.bt_novo = Button(self.frame_1, text="Novo")
        self.bt_novo.place(relx=0.6, rely=0.2, relheight=0.15)

        # Botão de ALTERAR
        self.bt_alterar = Button(self.frame_1, text="Alterar")
        self.bt_alterar.place(relx=0.7, rely=0.2, relheight=0.15)

        # Botão de APAGAR
        self.bt_apagar = Button(self.frame_1, text="Apagar")
        self.bt_apagar.place(relx=0.8, rely=0.2, relheight=0.15)

        # CRIAÇÃO LABEL
        self.lb_codigo = Label(self.frame_1, text="Código")
        self.lb_codigo.place(relx=0.5, rely=0.05)

        self.codigo_Entry= Entry(self.frame_1)
        self.codigo_Entry.place(relx=0.05 ,rely=0.15, relwidth=0.08)

        self.lb_nome= Label(self.frame_1, text="Nome")
        self.lb_nome.place(relx= 0.05, rely= 0.35)

        self.nome_entry= Entry(self.frame_1)
        self.nome_entry.place(relx= 0.05, rely=0.15, relwidth=0.085)

Application()