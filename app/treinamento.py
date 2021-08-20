import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# import pickle
from request import job

import schedule
import time




def treinamentos():
    df = pd.read_csv('2017a2021.csv',decimal=',')
    dff = pd.read_csv('dadosDia0208.csv',decimal=',')
    
    fechamento = df['FECHAMENTO']
    features = df[['ABERTURA','MÍNIMO','MÁXIMO']]
    
    features
    treino = features
    
    X_treino,X_teste,y_treino,y_teste=train_test_split(treino,fechamento,
                                                       random_state=42)
    equacao=LinearRegression()

    treinamento = equacao.fit(X_treino,y_treino)
    
    previsao = equacao.predict(dff)
    
    string = str(previsao)
    
    print('\n A previsao atualizada do fechamento da ação é ',string)
    time.sleep(2)
    
                                #### SALVANDO PREVISOES ####
                                
    # with open('previsoes.txt','a') as file:
    #     file.write('\n')
    #     file.write('DIA 0308')
    #     file.write(string)
    
    
                                ##### SALVANDO MODELO #####
                                
    # with open('modelo.pkl', 'wb') as file:
    #     pickle.dump(treinamento, file)
schedule.every(5).seconds.do(job)
schedule.every(5).seconds.do(treinamentos)
       
treinamentos()


while True:
    schedule.run_pending()
    time.sleep(1)



