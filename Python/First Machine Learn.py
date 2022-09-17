
import pandas as pd
arquivo = pd.read_csv('C:/Users/Marcelo/Desktop/Pythongg/wine_dataset.csv')
arquivo.head()

arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)

#Separando as variaveis entre preditoras e variavel alvo
y = arquivo['style']
x = arquivo.drop('style', axis = 1)

from sklearn.model_selection import train_test_split

#criando os conjuntos de dados de treino e de teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size = 0.3)

from sklearn.ensemble import ExtraTreesClassifier
#Criação do modelo:
modelo = ExtraTreesClassifier()
modelo.fit(x_treino,y_treino)

#imprimindo resultados:
resultado = modelo.score(x_teste, y_teste)
print("Acurácia:", resultado)
