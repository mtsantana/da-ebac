import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data = df, x = 'dia', y = 'venda')
  grafico.set(title = 'Preço da gasolina ao longo dos dias', \
            xlabel = 'Dia', ylabel = "Preço")

plt.savefig('gasolina.png')