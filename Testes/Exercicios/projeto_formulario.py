import tkinter as tk

def submeter_formulario():
    nome = entry_nome.get()
    email = entry_email.get()
    idade = entry_idade.get()

    # Exibe as informações no console
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Idade: {idade}")

# Criar a janela principal
janela = tk.Tk()
janela.title("Formulário de Cadastro")

# Criar e posicionar os widgets na janela
label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_email = tk.Label(janela, text="E-mail:")
label_email.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

entry_email = tk.Entry(janela)
entry_email.grid(row=1, column=1, padx=10, pady=5)

label_idade = tk.Label(janela, text="Idade:")
label_idade.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)

entry_idade = tk.Entry(janela)
entry_idade.grid(row=2, column=1, padx=10, pady=5)

botao_submeter = tk.Button(janela, text="Submeter", command=submeter_formulario)
botao_submeter.grid(row=3, columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()

