import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('1507e1607.csv',decimal=',')
dff = pd.read_csv('dadosDia2107.csv',decimal=',')

fechamento = df['FECHAMENTO']
features = df[['ABERTURA','MÁXIMO','MÍNIMO']]

dff
treino = features

#x_teste e y_teste sao as classes

X_treino,X_teste,y_treino,y_teste=train_test_split(treino,fechamento,
                                                   random_state=42)

equacao=LinearRegression()


equacao.fit(X_treino,y_treino)



previsao = equacao.predict(dff)
