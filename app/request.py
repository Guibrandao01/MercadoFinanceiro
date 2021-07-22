import requests
from bs4 import BeautifulSoup
import pandas as pd
response = requests.get('https://www.infomoney.com.br/cotacoes/petrobras-petr4/historico/',headers={'User-Agent': 'Mozilla/5.0'})
#https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/petr4-sa/
print(response.status_code)
print(response.headers)
print(response.content)


content = response.content
#especificando que o conteudo da pagina esta em html
site  = BeautifulSoup(content,'html.parser')
print(site.prettify())




noticias = site.find('div',attrs={'id':'results_box'})
noticias


abertura1 = site.find('div', attrs={'class': 'value'})
abertura1.text
abertura = abertura1.find('p')
abertura.text    


minimo1 = site.find('div', attrs={'class': 'minimo'})
minimo1.text
minimo = minimo1.find('p')
minimo.text    



maxima1 = site.find('div',attrs={'class': 'maximo'})
maxima1.text
maxima = maxima1.find('p')
maxima.text

lista = []

if(noticias):
    lista.append([abertura.text ,minimo.text ,maxima.text])
else:
    lista.append(['','',''])

    
lista        
        
df = pd.DataFrame(lista, columns=['Abertura','Minima','Maxima'])


print(df)
#salvando df com os dados do dia
tste = df.to_csv('dadosDia2107.csv', index=False)


dff = pd.read_csv('dadosDia.csv')
dff2 = pd.read_csv('noticias1.csv')
    


