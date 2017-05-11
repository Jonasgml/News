# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:45:45 2017

@author: jonas.oliveira2
"""

import re
from bs4 import BeautifulSoup #essa biblioteca tem esse jeito de importar
import requests 

# palavras pra procurar
keywords = ['petrobras',
            'temer']
# sites onde procurar
url = ['http://g1.globo.com/', 
       'https://www.portosenavios.com.br/']
links = []
# ******************************** fazer def
# loop nos sites
for site in url:
# ******************************** verificar data
    # pega o código fonte da página 
    page = requests.get(site)
    # organiza o código com o parse escolhido
    soup = BeautifulSoup(page.content,'html5lib')
    # loop para as palavras a serem procuradas
    for key in keywords:
        # loop na estrutura do código fonte para pegar todos tag "a" 
        for anchor in soup.find_all("a"):
            # verifica se a palavra existe dentro desse tag
            if bool(re.search(r'\b{}\b'.format(key.lower()), anchor.text.lower())):
            # caso existir armazena o link associado
                if site == 'https://www.portosenavios.com.br/':
                    links.append(site[:-1] + anchor.get('href'))
                else:
                    links.append(anchor.get('href'))   
# ******************************** procurar palavras no texto completo
# ******************************** procurar palavras em sub-páginas
# ******************************** retirar links repetidos
# ******************************** salvar arquivo com links