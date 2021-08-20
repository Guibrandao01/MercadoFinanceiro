import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

v = 0
v1 = 0
c2 = 0

v3 = str(input('\n digite o valor ideal para compra '))
v3 = str(v3)

v4 = str(input('\n digite o valor ideal para venda'))
v4 = str(v4)

def job():    
    response = requests.get('https://www.infomoney.com.br/cotacoes/petrobras-petr4/historico/',headers={'User-Agent': 'Mozilla/5.0'})
    #https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/petr4-sa/
    # print(response.status_code)
    # print(response.headers)
    # print(response.content)
       
    content = response.content
    #especificando que o conteudo da pagina esta em html
    site  = BeautifulSoup(content,'html.parser')
    # print(site.prettify())
    noticias = site.find('div',attrs={'id':'results_box'})
    noticias

    abertura1 = site.find('div', attrs={'class': 'value'})
    abertura1.text
    abertura = abertura1.find('p')
    abertura.text    

    atual = abertura.text
    v1 = atual
   
  
    
    
    minimo1 = site.find('div', attrs={'class': 'minimo'})
    minimo1.text
    minimo = minimo1.find('p')
    minimo.text
    minn = minimo.text
    v = minn
    
    
    maxima1 = site.find('div',attrs={'class': 'maximo'})
    maxima1.text
    maxima = maxima1.find('p')
    maxima.text
    maxx = maxima.text
    v2 = maxx
    
    # variacao1 = site.find('td',attrs={'class': 'positive'})
    # variacao1.text
    lista = []
    
    lista.append([abertura.text ,minimo.text ,maxima.text])
    
    lista        
            
    df = pd.DataFrame(lista, columns=['Abertura','Minima','Maxima'])
    # print(df)

      #salvando df com os dados do dia
    tste = df.to_csv('dadosDia0208.csv', index=False)
    
    print('\n valor atual em ', atual)
    time.sleep(2)
    print("\n A minima chegou em",minn)
    time.sleep(2)
    print("\n A maxima chegou em",maxx)
    time.sleep(2)
        
    
    
    if atual == v3:
        print('\n valor atual chegou no valor informado para compra', atual)
        time.sleep(2)
    if atual == v4:
        print('\n valor atual chegou no falor informado para venda', atual)
        
        
        
   
        
         
job()























    


