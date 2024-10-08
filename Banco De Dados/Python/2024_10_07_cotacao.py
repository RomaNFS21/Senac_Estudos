from tkinter import *
import tkinter as tk
import requests

def pegar_cotacoes():
    try:
        # Aqui você deve usar uma API que fornece a cotação do dólar.
        # Exemplo de uma API (verifique a documentação para obter a URL correta):
        url = 'https://api.exchangerate-api.com/v4/latest/USD'  # API de exemplo
        resposta = requests.get(url)
        dados = resposta.json()

        # Acessando o valor do dólar em relação ao real
        cotacao_dolar = dados['rates']['BRL']

        texto_resposta.config(text=f"Cotação do Dólar: R$ {cotacao_dolar:.2f}")
    except Exception as e:
        texto_resposta.config(text="Erro ao buscar cotações")

janela = Tk()
janela.title("Cotação Atual de Moedas")
texto = Label(janela, text="Clique no botão para ver as cotações de moeda")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
