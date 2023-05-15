# conversor de moedas com API

![Captura de tela_20230502_173332](https://user-images.githubusercontent.com/127805808/235780339-246d549c-77fb-411f-9afd-a2a8f59a01b8.png)

<h4>Este é o meu primeiro projeto com API utilizando Python e Tkinter. Trata-se de um conversor de moedas, que faz uso da API AwesomeAPI para obter as cotações em tempo real das moedas USD, EUR e BTC em relação ao Real (BRL)
A API AwesomeAPI é uma fonte de dados econômicos atualizados em tempo real, com informações sobre moedas, ações e índices financeiros de diversas partes do mundo..<h4>

## Funcionalidades
<h4>O programa utiliza a API AwesomeAPI para buscar as cotações de moedas em tempo real. O usuário escolhe a moeda de origem (Real R$), a moeda de destino (USD ou EUR) e o valor a ser convertido. O programa faz a conversão automaticamente e exibe o resultado.</h4>

## Como executar
<h4>Para executar o programa, basta rodar o arquivo "conversor.py". O programa foi escrito em Python 3 e utiliza as bibliotecas tkinter e requests.</h4>
<h4>Para utilizar o projeto, é necessário ter as bibliotecas PIL, requests e tkinter instaladas. Para instalá-las, basta utilizar o gerenciador de pacotes pip. Para mais informações sobre como instalar as bibliotecas, consulte a documentação oficial do Python.</h4>

  <pre>
pip install tk
</pre>
<pre>
pip install pillow
</pre>
<pre>
pip install requests
</pre>
  
## Configuração da interface
<h4>A interface do programa é construída utilizando a biblioteca tkinter. A janela possui dimensões de 300x320 e fundo branco. As cores utilizadas no projeto são branco (#fcfcfc), preto (#030000) e amarelo (#fccf03). A janela principal é dividida em dois frames, um para exibição da imagem da logo (frame_logo) e outro para o conversor de moedas (frame_conversor).</h4>

## Consumo da API
<h4>A API utilizada é a AwesomeAPI, que retorna as cotações em formato JSON. O programa faz uma requisição GET para a API com as cotações das moedas de interesse (USD, EUR e BTC) e armazena em um dicionário (cotacoes_dic). Em seguida, é feita a conversão de moedas e o resultado é exibido na interface.</h4>

