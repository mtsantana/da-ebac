import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

grafico = sns.lineplot(data = df, x = 'dia', y = 'venda', palette = 'pastel')

grafico.set(title = 'Preço da gasolina - Julho 2021',\
            xlabel = 'Dia da consulta', ylabel = 'Preço de venda (R$)')

plt.savefig('gasolina.png')