#  -------------------- impotacões --------------------
from tkinter import Tk, ttk
from tkinter import *
#  -------------------- impotacões secundarias--------------------
from PIL import ImageTk, Image
import requests
# -------------------- cores usadas no projeto --------------------
branco = "#fcfcfc"  # Branco
preto = "#030000"  # Preto
amarelo = "#fccf03"  # Amarelo

# -------------------- configurando a janela --------------------

janela = Tk()
janela.title('Conversor de moedas')
janela.geometry('300x320')
janela.config(background=branco)

style = ttk.Style(janela)
style.theme_use('clam')

# -------------------- divisão da tela(frame) --------------------

frame_logo = Frame(janela, width=300, height=60, padx=0, pady=0, bg=preto, relief="flat")
frame_logo.grid(row=0, column=0, columnspan=2)

frame_conversor = Frame(janela, width=300, height=260, padx=5, pady=0, bg=branco, relief="flat")
frame_conversor.grid(row=1, column=0, sticky=NSEW)


# -------------------- funcao para calcular a conversao e sonsumir a API --------------------
def conversao():
    moeda1 = escolhasMoeda.get()
    if moeda1 == 'USD':
        moeda1 = 'USDBRL'
        simbolo = ' US$'
    elif moeda1 == 'EUR':
        moeda1 = 'EURBRL'
        simbolo = '€'
    valorReal = valor.get()

    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacoes_dic = cotacoes.json()

    valorFinal = float(valorReal) / float(cotacoes_dic[moeda1]['bid'])
    valorFinal = f'{valorFinal:.2f}'

    resultado.configure(text=simbolo+valorFinal)


# -------------------- adicionar logo/criar img para exibir no tlinter --------------------

img = Image.open("images/conversor.png")
img_tk = ImageTk.PhotoImage(img)
logo = Label(frame_logo, image=img_tk)
logo.grid()

# -------------------- configurando o conversor --------------------
moedas = ['USD', 'EUR']

resultado = Label(frame_conversor, text='', width=16, height=2, pady=7, relief="solid", anchor=CENTER, font='Ivy 15 bold', bg=branco, fg=preto)
resultado.place(x=50, y=10)

deQual = Label(frame_conversor, text='De: ', width=8, height=1, pady=7, relief="flat", anchor=NW, font='Ivy 10 bold', bg=branco, fg=preto)
deQual.place(x=48, y=90)
escolhas1 = Label(frame_conversor, text='Real R$', width=8, justify=CENTER, font='Ivy 12 bold')
escolhas1.place(x=50, y=115)

paraQual = Label(frame_conversor, text='Para', width=8, height=1, pady=7, relief="flat", anchor=NW, font='Ivy 10 bold', bg=branco, fg=preto)
paraQual.place(x=158, y=90)
escolhasMoeda = ttk.Combobox(frame_conversor, width=8, justify=CENTER, font='Ivy 12 bold')
escolhasMoeda['values'] = moedas
escolhasMoeda.place(x=160, y=115)

msg = Label(frame_conversor, text='valor R$', width=8, height=1, pady=7, relief="flat", anchor=NW, font='Ivy 10 bold', bg=branco, fg=preto)
msg.place(x=45, y=149)
valor = Entry(frame_conversor, width=16, font='Ivy 12 bold', relief=SOLID)
valor.place(x=104, y=155)

botao = Button(frame_conversor, text="Converter", command=conversao, width=19, padx=5, height=1, bg=amarelo, fg=branco, font='Ivy 12 bold', relief=RAISED, overrelief=RIDGE)
botao.place(x=50, y=210)

janela.mainloop()
