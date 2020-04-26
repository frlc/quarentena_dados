import pandas as pd
from matplotlib import pyplot as plt

#filmes == Dataframe do pandas

#filmes dataset
filmes = pd.read_csv('/home/cr4zyd0g/Documentos/quarentena_dados/ml-latest-small/movies.csv')
filmes.columns = ['filmeId', 'titulo', 'generos']
#print(filmes.head())

#avaliações dataset
avaliacoes = pd.read_csv('/home/cr4zyd0g/Documentos/quarentena_dados/ml-latest-small/ratings.csv')
# print(avaliacoes.head())
# print(avaliacoes.shape)
# print(len(avaliacoes))
# print(avaliacoes.columns)
avaliacoes.columns = ['usuarioId', 'filmeId', 'nota', 'momento']
# print(avaliacoes.columns)
# print(avaliacoes.head())
# print(avaliacoes.query('usuarioId == 1'))
# print(avaliacoes.describe())
# print(avaliacoes['nota'])
# print(avaliacoes.query('usuarioId == 1').describe())
# print(avaliacoes.query('usuarioId == 1').mean())
# print(avaliacoes.query('usuarioId == 1')['nota'].mean())
nota_media_por_filme = avaliacoes.groupby("filmeId")["nota"].mean()
# print(nota_media_por_filme.head())
filmes_com_media = filmes.join(nota_media_por_filme, on="filmeId")
filmes_com_media = filmes_com_media.rename(columns={'nota': 'media'})
#filmes_com_media.columns = ['filme', 'titulo', 'generos', 'media']
#print(filmes_com_media.sort_values("media", ascending=False).head(15))
#print(avaliacoes.query('filmeId in [1,2,102084]'))
avaliacoes.query('filmeId == 1')['nota'].plot(kind='hist')