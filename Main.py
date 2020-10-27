"""

MIT License

Copyright (c) 2020 Val

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
# -*- coding utf-8 -*-
__version__ = '0.0.01'
# Importando modulos
import pyttsx3
import wikipedia
from requests import get
from bs4 import BeautifulSoup
# Definições
wikipedia.set_lang('pt')
keywords = ['quem foi', 'quem e', 'o que é',
            'quem é', 'o que é', 'definicao de', 'definição de',
            'definicao da palavra', 'definição da palavra'] # Palavras chaves para pesquisar no Wikipedia
voice = pyttsx3.init() # Configurações da voz
# Sinteze de Voz
def speaker(phrase):
    voice.say(phrase)
    voice.runAndWait()
# Busca no wikipedia
def wiki(phrase):
    result = None
    results = None
    for key in keywords:
        if phrase.startswith(key):
            result = phrase.replace(key, '')
    if result is not None:
        results = wikipedia.summary(wikipedia.search(result)[0], sentences=2)
    return results
# Noticias
def scrapping():
    site = get("https://news.google.com/rss?need=pt_br&gl=BR&hl=pt-BR&ceid=BR:pt-419")
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:5]:
        return f"{item.title.text}\n"
# Previsão do tempo
def previsao_do_tempo():
    site = get('http://api.openweathermap.org/data/2.5/weather?lat=-29.6842&lon=-53.8069&appid=90215b527139cc03551eff4bb45ea00f&units=metric&lang=pt')
    clima = site.json()
    temperatura = clima['main']['temp']
    fell = clima['main']['feels_like']
    descricao = clima['weather'][0]['description']
    return f"Temperatura atual: {temperatura} graus, sensação térmica de {fell} graus, situação atual do céu {descricao}"
# Chatbot
while True:
    try:
        cmd: str = input('Você: ').strip().lower()
        response = wiki(cmd)
        if response == None:
            if cmd == 'bom dia':
                response = 'Bom dia, tudo bem?'
                continue
            elif cmd == 'oi':
                response = 'Olá'
                continue
            elif cmd == 'estou bem' or cmd == 'tudo bem comigo':
                response = 'que bom que você esta bem!'
                continue
            elif cmd == 'boa tarde':
                response = 'Boa tarde!'
                continue
            elif cmd == 'previsao do tempo' or cmd == 'previsão do tempo' or cmd == 'como esta o tempo' or 'como esta o tempo hoje':
                response = previsao_do_tempo()
                continue
            elif cmd == 'noticias' or cmd == 'noticias diarias' or cmd == 'noticias de hoje':
                response = scrapping()
                continue
            elif cmd == 'boa noite':
                response = 'Boa noite pra você tambem!'
                continue
            elif cmd == 'tchau' or cmd == 'adeus':
                print('Val Assistent: Tchau!!!')
                break
            else:
                response = 'Não tenho resposta para isso!'
                continue
        print(f'Val Assistente: {response}')
        speaker(phrase=response)
    except Exception as e:
        print('Val Assistente: Desculpe-me, ocorreu um erro!')
        continue
