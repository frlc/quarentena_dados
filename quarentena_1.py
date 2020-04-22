import pandas as pd

#filmes == Dataframe do pandas

#filmes dataset
#filmes = pd.read_csv('/home/cr4zyd0g/Documentos/quarentena_dados/ml-latest-small/movies.csv')
#print(filmes.head())

#avaliações dataset
avaliacoes = pd.read_csv('/home/cr4zyd0g/Documentos/quarentena_dados/ml-latest-small/ratings.csv')
print(avaliacoes.head())
print(avaliacoes.shape)
print(len(avaliacoes))
print(avaliacoes.columns)
avaliacoes.columns = ['usuarioId', 'filmeId', 'nota', 'momento']
print(avaliacoes.columns)
print(avaliacoes.head())
print(avaliacoes.query('usuarioId == 1'))
print(avaliacoes.describe())
print(avaliacoes['nota'])
print(avaliacoes.query('usuarioId == 1').describe())
print(avaliacoes.query('usuarioId == 1').mean())
print(avaliacoes.query('usuarioId == 1')['nota'].mean())