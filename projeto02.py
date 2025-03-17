import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Pojeto 02",
     page_icon="📊",
     layout="wide", 
     initial_sidebar_state="expanded"

)

st.write('# Análise exploratória da previsão de renda')

renda = pd.read_csv('./input/previsao_de_renda.csv')
renda['data_ref'] = pd.to_datetime(renda['data_ref'])

with st.sidebar:
    st.title("Menu")
    pagina = st.radio(
        "Selecione uma página:",
        ["Pagina inicial", "Graficos ao longo do tempo", "Analise bivariada", "Modelo e resultados", "Conclusão"]
    )
    
if pagina == "Pagina inicial":
    st.title("Pagina inicial")

    st.subheader("Resumo dos Dados")
    st.dataframe(renda.describe(include='all'), use_container_width=True)

elif pagina == "Graficos ao longo do tempo":
    st.subheader("Graficos ao longo do tempo")
    fig, ax = plt.subplots(figsize=(10, 6))
    viz_type = st.selectbox(
        "Escolha um gráfico para visualizar:",
        ["posse_de_imovel e renda", "posse_de_veiculo e renda", "qtd_filhos e renda", "tipo_renda e renda", "educacao e renda", "estado_civil e renda", "tipo_residencia e renda"]
    )
    
    if viz_type == "posse_de_imovel e renda":
        st.subheader("posse_de_imovel e renda no tempo")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x='data_ref', y='renda', hue='posse_de_imovel', data=renda, ax=ax)
        plt.tight_layout()
        st.pyplot(fig)
        
    elif viz_type == "posse_de_veiculo e renda":
        st.subheader("posse_de_veiculo e renda no tempo")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x='data_ref', y='renda', hue='posse_de_veiculo', data=renda, ax=ax)  
        plt.tight_layout()
        st.pyplot(fig)
        
    elif viz_type == "qtd_filhos e renda":
        st.subheader("qtd_filhos e renda no tempo")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x='data_ref', y='renda', hue='qtd_filhos', data=renda, ax=ax)
        plt.tight_layout()
        st.pyplot(fig)
        
    elif viz_type == "tipo_renda e renda":
        st.subheader("tipo_renda e renda no tempo")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x='data_ref', y='renda', hue='tipo_renda', data=renda, ax=ax)
        plt.tight_layout()
        st.pyplot(fig)
                
    elif viz_type == "educacao e renda":
        st.subheader("educacao e renda no tempo")

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x='data_ref', y='renda', hue='educacao', data=renda, ax=ax)
        plt.tight_layout()
        st.pyplot(fig)

    elif viz_type == "estado_civil e renda":
        st.subheader("estado_civil e renda no tempo")

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x='data_ref', y='renda', hue='estado_civil', data=renda, ax=ax)
        plt.tight_layout()
        st.pyplot(fig)
    
    elif viz_type == "tipo_residencia e renda":
        st.subheader("tipo_residencia e renda no tempo")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x='data_ref', y='renda', hue='tipo_residencia', data=renda, ax=ax)
        plt.tight_layout()
        st.pyplot(fig)


elif pagina == "Analise bivariada":
    st.subheader("Analise bivariada")

    viz_type = st.selectbox(
        "Escolha uma das opções de analises bivariadas",
        ["Variaveis qualitativas", "Variaveis numericas"]
    )
    
    if viz_type == "Variaveis qualitativas":
        st.subheader("Variaveis qualitativas - graficos de bivariadas")
        
        vars_categoricas = ["sexo", "posse_de_veiculo", "posse_de_imovel", "tipo_renda", "educacao", "estado_civil", "tipo_residencia"]
        
        for var in vars_categoricas:
            fig, axes = plt.subplots(1, 2, figsize=(14, 5))
            
            sns.boxplot(x=var, y='renda', data=renda, ax=axes[0])
            
            axes[0].set_title(f"Boxplot: Renda x {var}")
            axes[0].tick_params(axis='x', rotation=45)
            
            sns.barplot(x=var, y='renda', data=renda, estimator=np.mean, ax=axes[1])
            
            axes[1].set_title(f"Média de Renda por {var}")
            axes[1].tick_params(axis='x', rotation=45)
            
            plt.tight_layout()
            st.pyplot(fig)  

          
    elif viz_type == "Variaveis numericas":
        st.subheader("Variaveis numericas - graficos de bivariadas")
        
        num_vars = ["idade", "tempo_emprego", "qt_pessoas_residencia"]
        for var in num_vars:
            
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
            
            ax1.scatter(renda[var], renda['renda'], alpha=0.5)
            ax1.set_xlabel(var)
            ax1.set_ylabel("Renda")
            ax1.set_title(f"Scatter Plot: Renda vs {var}")
            
            renda['bins'] = pd.cut(renda[var], bins=10)
            
            biv = renda.groupby('bins', observed=False)['renda'].mean()
            
            ax2.plot(biv.index.astype(str), biv.values, marker='o')
            ax2.set_xlabel(var)
            ax2.set_ylabel("Média da Renda")
            ax2.set_title(f"Gráfico de Linha: Média da Renda por {var}")
            plt.xticks(rotation=45)
            
            plt.tight_layout()
            st.pyplot(fig)


elif pagina == "Modelo e resultados":
    st.subheader("escolha o modelo")
    st.write(' como visto nas analises bivariadas, muitas das relações entre as variavel e renda sao não lineares, sendo assim, o melhor modelo dentro dos modelos ja aprendidos é o de arvore de decisão.')
    
    st.write('Apos o treinamento do modelo, foram obtidos os seguintes resultados:')
    st.write('mse treino: 35031681.33833955')
    st.write('r2 treino: 0.4884241462336273')
    st.write('Erro Quadrático Médio teste: 34803648.74889145')
    st.write('Coeficiente de Determinação teste: 0.48641610431283133')

    st.image("./output/arvore_regressao.png", caption='Visualização arvore de regressão',  use_container_width=True)

elif pagina == "Conclusão":
     st.subheader("Conclusão")
     
     st.write("A modelagem foi realizada utilizando algoritmos de aprendizado de máquina, sendo avaliada com métricas como Mean Squared Error (MSE) e R². O desempenho do modelo foi satisfatório, conseguindo capturar padrões importantes nos dados. No entanto, algumas limitações foram observadas, como a presença de outliers e possíveis variáveis latentes não disponíveis no conjunto de dados, que poderiam melhorar a previsibilidade do modelo.")
     st.write('Possíveis melhorias incluem o uso de técnicas mais avançadas e a inclusão de mais variáveis que possam impactar a renda, a previsão de renda é uma tarefa complexa, influenciada por múltiplas variaveis. Conseguindo prever cerca de 50% o modelo desenvolvido pode ser útil para segmentação de clientes, oferta de produtos financeiros e otimização de concessão de crédito, contribuindo para melhores decisões estratégicas no setor bancário.')

     st.write('Alem das possiveis melhorias do modelo a aplicação do mesmo poderia ser realizada em um ambiente de produção, onde os dados seriam atualizados periodicamente e o modelo seria re-treinado com novos dados, garantindo que a previsão de renda seja sempre atualizada e precisa.')
     st.write('Outro exemplo de aplicação seria ate mesmo no streamlit onde por meio de um upload de arqvuivo csv com novos dados, o modelo poderia ser re-treinado e a previsão de renda poderia ser realizada para novos clientes.')
     st.write('Por fim, a aplicação do modelo de previsão de renda pode ser utilizada para auxiliar na tomada de decisões estratégicas, como a definição de políticas de crédito, segmentação de clientes e otimização de produtos financeiros, contribuindo para a melhoria dos resultados do negócio.')

