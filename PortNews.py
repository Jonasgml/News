# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:45:45 2017

@author: jonas.oliveira2
"""

import re
from bs4 import BeautifulSoup #essa biblioteca tem esse jeito de importar
import requests 
import pandas as pd

# palavras pra procurar
keywords = ['petrobras']
# sites onde procurar
url = ['http://g1.globo.com/', 
       'https://www.portosenavios.com.br/',
       'http://portal.antaq.gov.br/index.php/category/noticias/',
       'http://www.jornalportuario.com.br/resumo-economico/transacoes-economicas-do-mes-de-maio#.WRX0zfkrK00',
       'http://www.jornalportuario.com.br/ultimas-noticias#.WRX04fkrK00',
       'http://www.portalnaval.com.br/',
       'http://www.portalnaval.com.br/entrevista/',
       'http://portosprivados.ibsweb.com.br/#',
       'http://www.folha.uol.com.br/',
       'http://www.estadao.com.br/',
       'https://www.terra.com.br/',
       'http://www.valor.com.br/',
       'http://www.atribuna.com.br/porto-mar/',
       'http://jcrs.uol.com.br/']

links = []
aux = []
aux_google = []
xls_file = pd.ExcelFile('links_PRUMO.xlsx')
news = xls_file.parse(xls_file.sheet_names)
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
            #loop de buscas no google
            google = requests.get("https://news.google.com/news/section?q=" + key)
            # organiza o código com o parse escolhido
            googlesoup = BeautifulSoup(google.content,'html5lib')
            for anchorgoogle in googlesoup.find_all("a"):
                if bool(re.search(r'\b{}\b'.format(key.lower()), anchorgoogle.text.lower())):
                    aux_google.append(anchorgoogle.get('href'))
            # loop na estrutura do código fonte para pegar todos tag "a" 
            for anchor in soup.find_all("a"):
            # verifica se a palavra existe dentro desse tag
                if bool(re.search(r'\b{}\b'.format(key.lower()), anchor.text.lower())):
            # caso existir armazena o link associado
                    aux.append(site)
                    if site == 'https://www.portosenavios.com.br/':
                        links.append(site[:-1] + anchor.get('href'))
                    elif site == 'http://www.valor.com.br/':
                        links.append(site[:-1] + anchor.get('href'))
                    elif site == 'http://jcrs.uol.com.br/':
                        links.append(site[:-1] + anchor.get('href'))
                    else:
                        links.append(anchor.get('href'))   
# ******************************** procurar palavras no texto completo
# ******************************** procurar palavras em sub-páginas
links = links + aux_google
# retira links repetidos
news = list(set(links))
news.sort()
# salvar arquivo com links
# Create a Pandas dataframe from the data.
df = pd.DataFrame(news)
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('links_PRUMO.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='news')
# Close the Pandas Excel writer and output the Excel file.
writer.save()