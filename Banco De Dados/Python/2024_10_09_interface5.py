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
        self.lista_frame2()
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
        self.bt_limpar = Button(self.frame_1,text = "Limpar", bg="#3c84ff", fg="#ffffff", font=("verdana", 8,"bold"))
        self.bt_limpar.place(relx = 0.9 , rely = 0.3, relheight = 0.15)

        # Botão de BUSCAR
        self.bt_buscar = Button(self.frame_1, text = "Buscar", bg="#3c84ff", fg="#ffffff", font=("verdana", 8,"bold"))
        self.bt_buscar.place(relx = 0.9 , rely = 0.05, relheight = 0.15)

        # Botão de NOVO
        self.bt_novo = Button(self.frame_1, text="Novo", bg="#038317", fg="#ffffff", font=("verdana", 8,"bold"))
        self.bt_novo.place(relx=0.62, rely=0.05, relheight=0.15)

        # Botão de ALTERAR
        self.bt_alterar = Button(self.frame_1, text="Alterar", bg="#3c84ff", fg="#ffffff", font=("verdana", 8,"bold"))
        self.bt_alterar.place(relx=0.69, rely=0.05, relheight=0.15)

        # Botão de APAGAR
        self.bt_apagar = Button(self.frame_1, text="Apagar", bg="#fa2e25", fg="#ffffff", font=("verdana", 8,"bold"))
        self.bt_apagar.place(relx=0.78, rely=0.05, relheight=0.15)

        self.codigo_Entry= Entry(self.frame_1)
        self.codigo_Entry.place(relx=0.05 ,rely=0.15, relwidth=0.08)

        # CRIAÇÃO LABEL
        self.lb_codigo = Label(self.frame_1, text="Código", bg="#dfe3ee", fg="#107db2")
        self.lb_codigo.place(relx=0.05, rely=0.05)

        # Criação da label entrade de nome
        self.lb_nome= Label(self.frame_1, text="Nome", bg="#dfe3ee", fg="#107db2")
        self.lb_nome.place(relx= 0.05, rely= 0.4, relwidth=0.085)

        self.nome_entry= Entry(self.frame_1)
        self.nome_entry.place(relx= 0.05, rely=0.5, relwidth=0.4)

        # Criação da lebel entrada de telefone
        self.lb_nome = Label(self.frame_1, text="Telefone", bg="#dfe3ee", fg="#107db2")
        self.lb_nome.place(relx=0.05, rely=0.6)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.7,relwidth = 0.4)

        # Criação da label entrada de cidade
        self.lb_cidade = Label(self.frame_1, text="Cidade", bg="#dfe3ee", fg="#107db2")
        self.lb_cidade.place(relx= 0.5, rely= 0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx =0.5, rely=0.7, relwidth= 0.4)

        #lista Frame_2

    def lista_frame2(self):
        self.lista_cliente = ttk.Treeview(self.frame_2,height=3,columns=("coll1","coll2","coll3","coll4"))
        #NOME DE CADA COLUNA
        self.lista_cliente.heading("#0",text="")
        self.lista_cliente.heading("#1", text="Código")
        self.lista_cliente.heading("#2", text="Nome")
        self.lista_cliente.heading("#3", text="Telefone")
        self.lista_cliente.heading("#4", text="Cidade")
        #TAMANHO DE CADA COLUNA
        self.lista_cliente.column("#0",width=1)
        self.lista_cliente.column("#1", width=50)
        self.lista_cliente.column("#2", width=200)
        self.lista_cliente.column("#3", width=125)
        self.lista_cliente.column("#4", width=125)
        # POSIÇÃO
        self.lista_cliente.place(relx=0.01,rely=0.01, relwidth=0.95, relheight=0.98)

        # BARRA DE ROLAGEM
        self.scrollista = Scrollbar(self.frame_2,orient="vertical")
        self.lista_cliente.configure(yscroll=self.scrollista.set)
        self.scrollista.place(relx=0.97,rely=0.02,relwidth=0.03,relheight=0.955)


Application()