from selenium import webdriver
import requests
import pandas as pd
navegador = webdriver.Chrome()

#                           BAIXANDO DADOS DA INTERNET 
navegador.get('https://www.infomoney.com.br/cotacoes/petrobras-petr4/historico/')
elemento = navegador.find_element_by_class_name('dt-button ').click()

#-----------------------------------------------------------------------------
#                               MANIPULANDO

df = pd.read_csv('1407.csv')
abertura1 = df['ABERTURA']
abertura = abertura1[0]

fechamento1 = df['FECHAMENTO']
fechamento = fechamento1[0]

minimo1 = df['MÍNIMO']
minimo = minimo1[0]

maximo1 = df['MÁXIMO']
maximo = maximo1[0]

#-----------------------------------------------------------------------------
#                           LISTA DOS DADDOS MANIPULADOS

listaDados = []
listaDados.append([abertura,fechamento,minimo,maximo]) 

#----------------------------------------------------------------------------
#                           DATA FRAME DADOS TRATADOS

NovaDf = pd.DataFrame(listaDados,columns = ['Abertura','Fechamento','Minimo','Maximo'])
NovaDf.to_csv('Tratado1407.csv')


#ALTERAR PLANILHA CONFORME O DIA, PARA ADICIONAR OS DADOS NO NOVO DF
df2 = pd.read_csv('Tratado1407.csv')


abertura2 = df2['Abertura']
novaabertura = abertura2[0]


fechamento2 = df2['Fechamento']
novaminimo = fechamento2[0]


minimo2 = df2['Minimo']
novaminimo = minimo2[0]


maximo2 = df2['Maximo']
novamaximo = maximo2[0]

# RODAR ESSA APENAS 1 VEZ A LISTA 
lista2 = []

lista2.append([novaabertura,novaminimo,novaminimo,novamaximo])

NovaDf2 = pd.DataFrame(lista2,columns = ['Abertura','Fechamento','Minimo','Maximo'])

NovaDf2


