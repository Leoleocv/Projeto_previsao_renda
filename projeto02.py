import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="???????",
     page_icon=":?:",
     layout="wide",
)

st.write('# Análise exploratória da previsão de renda')

renda = pd.read_csv('./input/previsao_de_renda.csv')

#plots
fig, ax = plt.subplots(8,1,figsize=(10,70))
renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
st.write('## Gráficos ao longo do tempo')

sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel',data=renda, ax=ax[1])
ax[1].tick_params(axis='x', rotation=45)

sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',data=renda, ax=ax[2])
ax[2].tick_params(axis='x', rotation=45)

sns.lineplot(x='data_ref',y='renda', hue='qtd_filhos',data=renda, ax=ax[3])
ax[3].tick_params(axis='x', rotation=45)

sns.lineplot(x='data_ref',y='renda', hue='tipo_renda',data=renda, ax=ax[4])
ax[4].tick_params(axis='x', rotation=45)

sns.lineplot(x='data_ref',y='renda', hue='educacao',data=renda, ax=ax[5])
ax[5].tick_params(axis='x', rotation=45)

sns.lineplot(x='data_ref',y='renda', hue='estado_civil',data=renda, ax=ax[6])
ax[6].tick_params(axis='x', rotation=45)

sns.lineplot(x='data_ref',y='renda', hue='tipo_residencia',data=renda, ax=ax[7])
ax[7].tick_params(axis='x', rotation=45)

sns.despine()
st.pyplot(plt)

st.write('## Gráficos bivariada')
fig, ax = plt.subplots(7,1,figsize=(10,50))

sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0])

sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])

sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])

sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])

sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])

sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])

sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])

sns.despine()

st.pyplot(plt)

st.write('## Model Evaluation Metrics')
st.write(f'MSE (train): 35031681.34')
st.write(f'R2 (train): 0.4884')
st.write(f'MSE: 34803648.75')
st.write(f'R2: 0.4864')

st.write('## Conclusion')
st.write('A modelagem foi realizada utilizando algoritmos de aprendizado de máquina, sendo avaliada com métricas como Mean Squared Error (MSE) e R². O desempenho do modelo foi satisfatório, conseguindo capturar padrões importantes nos dados. No entanto, algumas limitações foram observadas, como a presença de outliers e possíveis variáveis latentes não disponíveis no conjunto de dados, que poderiam melhorar a previsibilidade do modelo.')
st.write('Possíveis melhorias incluem o uso de técnicas mais avançadas e a inclusão de mais variáveis que possam impactar a renda, a previsão de renda é uma tarefa complexa, influenciada por múltiplas variaveis. Conseguindo prever cerca de 50% d O modelo desenvolvido pode ser útil para segmentação de clientes, oferta de produtos financeiros e otimização de concessão de crédito, contribuindo para melhores decisões estratégicas no setor bancário.')

st.write('## Distribution of Renda')
fig_hist, ax_hist = plt.subplots()
sns.histplot(renda["renda"], bins=50, kde=True, ax=ax_hist)
ax_hist.set_title("Distribution of Renda")
ax_hist.set_xlabel("Renda")
ax_hist.set_ylabel("Frequência")
st.pyplot(fig_hist)
