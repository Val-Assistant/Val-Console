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
        audio.cria_audio(f"{item.title.text}\n")
# Previsão do tempo
def previsao_do_tempo():
    site = get('http://api.openweathermap.org/data/2.5/weather?lat=-29.6842&lon=-53.8069&appid=90215b527139cc03551eff4bb45ea00f&units=metric&lang=pt')
    clima = site.json()
    temperatura = clima['main']['temp']
    fell = clima['main']['feels_like']
    descricao = clima['weather'][0]['description']
    return (f"Temperatura atual: {temperatura} graus, sensação térmica de {fell} graus, situação atual do céu {descricao}")
# Chatbot
while True:
    try:
        cmd: str = input('Você: ').strip().lower()
        response = wiki(cmd)
        if response == None:
            if cmd == 'bom dia':
                response = 'Bom dia, tudo bem?'
            elif cmd == 'estou bem' or cmd == 'tudo bem comigo':
                response = 'que bom que você esta bem!'
            elif cmd == 'boa tarde':
                response = 'Boa tarde!'
            elif cmd == 'boa noite':
                response = 'Boa noite pra você tambem!'
            else:
                response = 'Não tenho resposta para isso!'
        print(f'Assistente: {response}')
        speaker(phrase=response)
    except KeyboardInterrupt:
        break
    except:
        print('IA: Desculpe-me, ocorreu um erro!')
