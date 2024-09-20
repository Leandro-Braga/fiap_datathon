import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def graph_faltas_aluno(df_aluno):

    cor_clara = '#DCF2F1'

    # Criar uma nova coluna formatada para 'data'
    df_aluno['data'] = pd.to_datetime(df_aluno['data_aula']).dt.strftime("%Y/%m")

    # Agrupar os dados por 'data' e calcular as presenças e faltas
    df_aux = df_aluno.groupby("data").agg(
        faltou=('presente', lambda x: (x == 0).sum()),
        compareceu=('presente', lambda x: (x == 1).sum())
    ).reset_index()

    # Calcular a média de faltas
    media_faltas = df_aux["faltou"].mean()

    # Criar o gráfico com Plotly
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df_aux["data"],
            y=df_aux["faltou"],
            mode="lines+markers",
            name="Faltas",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df_aux["data"],
            y=[media_faltas] * len(df_aux),
            mode="lines",
            name="Média de Faltas",
            line=dict(color="gray", width=2, dash="dash"),
        )
    )

    # Personalizando o layout do gráfico
    fig.update_layout(
        title="Quantidade de Faltas ao Longo do Tempo",
        xaxis_title="Data",
        yaxis_title="Número de Faltas",
        template="plotly_white",
        width=1100,
        height=500,
    
        # Configurar cor e tamanho da fonte dos rótulos dos eixos
        xaxis=dict( # xaxis=dict(gridcolor='red'),  
            title=dict(text='DATA', font=dict(size=16, color=cor_clara)),  
            tickfont=dict(size=14, color=cor_clara),
        ),

        yaxis=dict(gridcolor=cor_clara,
            title=dict(text='Número de Faltas', font=dict(size=16, color=cor_clara)),  
            tickfont=dict(size=14, color=cor_clara),
            tickprefix=' ', 
        ),
    
    
    )

    # Configurar o tamanho da linha
    fig.update_traces(
        line=dict(width=4),  
        marker=dict(size=9),  
        # Configurar a cor e a fonte do hover_data
        hoverlabel=dict( 
            bgcolor='#0C2D57',  
            font=dict(family='Arial', size=16, color='white'), 
            namelength=-1  # Mostra o nome completo mesmo que seja longo  
        ),
        
    )

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)


def graph_presenca_aluno(df):
    
    # Calculando a porcentagem de presença
    total_presencas = df['presente'].sum()
    total_registros = df['presente'].count()
    porcentagem_presenca = (total_presencas / total_registros) * 100
    porcentagem_falta = 100 - porcentagem_presenca

    # Criando um DataFrame para o gráfico
    df_porcentagem = pd.DataFrame({
        'Status': ['Presente', 'Faltou'],
        'Porcentagem': [porcentagem_presenca, porcentagem_falta]
    })

    # Criando o gráfico de pizza 
    fig = px.pie(
        df_porcentagem, 
        values='Porcentagem', 
        names='Status', 
        title='Porcentagem de Presença',
        color='Status',  # Especifica personalizar as cores por Status
        color_discrete_map={'Presente': '#229799', 'Faltou': '#A04747'}  # Mapeia as cores
    )

    # Ajustando o layout do gráfico
    fig.update_layout(
        title_font=dict(size=20),
        plot_bgcolor='rgba(0, 0, 0, 0)', 
        paper_bgcolor='rgba(0, 0, 0, 0)', 
        font_color='white',
        width=600,
        height=500, 
        )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig)


def graph_frequencia_aluno_semanal(df, var_presente):

    cor_clara = '#DCF2F1'

    df_completo = df

    # Extraindo o dia da semana e convertendo para nomes dos dias
    df_completo['dia_semana'] = df_completo['data_aula'].dt.weekday
    dias_semana = {0: 'Segunda', 1: 'Terça', 2: 'Quarta', 3: 'Quinta', 4: 'Sexta', 5: 'Sábado', 6: 'Domingo'}
    df_completo['dia_semana'] = df_completo['dia_semana'].map(dias_semana)

    # Calculando a taxa de presença por dia da semana
    presenca_por_dia = df_completo.groupby('dia_semana')['presente'].mean() * 100

    # Ordenando os dias da semana para exibição
    presenca_por_dia = presenca_por_dia.reindex(['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'])

    # Calculando a taxa de faltas por dia da semana
    faltas_por_dia = 100 - presenca_por_dia

    if var_presente == 'Presença':
        texto_y = 'Porcentagem de Presença'
        # Gráfico da taxa de presença por dia da semana
        fig_dia_semana = px.bar(
            presenca_por_dia, 
            title='Taxa de Presença por Dia da Semana', 
            labels={'value': 'Porcentagem de Presença', 'index': 'Dia da Semana'},
            color_discrete_sequence=px.colors.sequential.Blues_r,
            text_auto='.2s'
        )

    elif var_presente == 'Faltas':
        texto_y = 'Porcentagem de Faltas'
         # Gráfico da taxa de presença por dia da semana
        fig_dia_semana = px.bar(
            faltas_por_dia, 
            title='Taxa de Faltas por Dia da Semana', 
            labels={'value': 'Porcentagem de Faltas', 'index': 'Dia da Semana'},
            color_discrete_sequence=px.colors.qualitative.Bold,
            text_auto='.2s'
        )

    # Ajustando o layout do gráfico
    fig_dia_semana.update_layout(
        title_font=dict(size=20),
        plot_bgcolor='rgba(0, 0, 0, 0)', 
        paper_bgcolor='rgba(0, 0, 0, 0)', 
        font_color='white',
        bargap=0.2,  # Ajuste para a largura das barras
        width=1200,
        height=500,
        # legend=dict(font=dict(size=15)),
        showlegend=False,  # remove a legenda

    
    # Configurar cor e tamanho da fonte dos rótulos dos eixos
    xaxis=dict( # xaxis=dict(gridcolor='red'), 
        title=dict(text='', font=dict(size=15, color=cor_clara)), 
        tickfont=dict(size=15, color=cor_clara)
    ),

    yaxis=dict(gridcolor=cor_clara,
        title=dict(text=texto_y, font=dict(size=18, color=cor_clara)),  
        tickfont=dict(size=18, color=cor_clara),
        tickprefix='% ',
    ),
        )
    

    fig_dia_semana.update_traces(
        # Configurar a cor e a fonte do hover_data
        hoverlabel=dict(
            bgcolor='#0C2D57',  
            font=dict(family='Arial', size=15, color='white'), 
            namelength=-1  # Mostra o nome completo mesmo que seja longo  
        ),   

        # Aumentar o tamanho do rótulo das barras
        textfont=dict(size=15, color='white')
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_dia_semana)


def graph_distribuicao(df):

    cor_clara = '#DCF2F1'
    texto_y = 'Quantidade de Alunos'

    df = df.drop_duplicates(subset=['id_aluno'], keep='first')

    # Criando o histograma da distribuição de idade dos alunos
    fig = px.histogram(df, 
                    x='idade_aluno', 
                    title='Gráfico da Distribuição de Idade dos Alunos', 
                    labels={'idade_aluno': 'Idade dos Alunos'}, 
                    nbins=10,  # Ajuste o número de bins 
                    color_discrete_sequence=['#1f77b4'])

    # Ajustando o layout para fundo escuro
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',  
        paper_bgcolor='rgba(0, 0, 0, 0)', 
        font_color='white',
        width=1200,
        height=500,   

    # Configurar cor e tamanho da fonte dos rótulos dos eixos
    xaxis=dict( # xaxis=dict(gridcolor='red'), 
        title=dict(text='', font=dict(size=15, color=cor_clara)), 
        tickfont=dict(size=15, color=cor_clara)
    ),

    yaxis=dict(gridcolor=cor_clara,
        title=dict(text=texto_y, font=dict(size=18, color=cor_clara)),  
        tickfont=dict(size=18, color=cor_clara),
        tickprefix='UN ',
    ),             
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig)


def graph_frequencia_aluno_idade(df, var_presente):

    cor_clara = '#DCF2F1'

    # Juntando as tabelas para trazer as idades dos alunos para a tabela de frequência
    df_merged = df.drop_duplicates(subset=['id_aluno'])
    # df_merged = df.drop_duplicates(subset=['id_aluno'], keep='first')

    # Definindo as faixas etárias
    bins = [0, 10, 15, 20, 25, 30, 100]
    labels = ['0-10', '11-15', '16-20', '21-25', '26-30', '30+']
    df_merged['faixa_etaria'] = pd.cut(df_merged['idade_aluno'], bins=bins, labels=labels, right=False)

    # Calculando a porcentagem de presença e faltas por faixa etária
    presenca_por_faixa = df_merged.groupby('faixa_etaria')['presente'].mean() * 100
    faltas_por_faixa = 100 - presenca_por_faixa

    # Exibindo os resultados para análise
    # print("Porcentagem de Presença por Faixa Etária:")
    # print(presenca_por_faixa)
    # print("\nPorcentagem de Faltas por Faixa Etária:")
    # print(faltas_por_faixa)
    
    if var_presente == 'Presença':
        
        texto_y = 'Porcentagem de Presença por Faixa Etária'
        
        # Gráfico de presença por faixa etária (mantido como estava)
        fig_presenca = px.bar(presenca_por_faixa, 
                            title='Porcentagem de Presença por Faixa Etária', 
                            labels={'value': 'Porcentagem de Presença', 'faixa_etaria': 'Faixa Etária'},
                            color_discrete_sequence=px.colors.sequential.Blues_r,
                            text_auto='.2s')
              

        fig_presenca.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',  
            paper_bgcolor='rgba(0, 0, 0, 0)', 
            font_color='white',
            width=1200,
            height=500,
            showlegend=False,  # remove a legenda   

            # Configurar cor e tamanho da fonte dos rótulos dos eixos
            xaxis=dict( # xaxis=dict(gridcolor='red'), 
                title=dict(text='', font=dict(size=15, color=cor_clara)), 
                tickfont=dict(size=15, color=cor_clara)
            ),

            yaxis=dict(gridcolor=cor_clara,
                title=dict(text=texto_y, font=dict(size=18, color=cor_clara)),  
                tickfont=dict(size=18, color=cor_clara),
                tickprefix='% ',
            ),

        )

        fig_presenca.update_traces(
            # Configurar a cor e a fonte do hover_data
            hoverlabel=dict(
                bgcolor='#0C2D57',  
                font=dict(family='Arial', size=15, color='white'), 
                namelength=-1  # Mostra o nome completo mesmo que seja longo  
            ),   

            # Aumentar o tamanho do rótulo das barras
            textfont=dict(size=15, color='white')
        )

        # Exibindo o gráfico no Streamlit
        st.plotly_chart(fig_presenca)
    
    elif var_presente == 'Faltas':
        
        texto_y = 'Porcentagem de Faltas'
        
        # Gráfico de faltas por faixa etária com cor vermelha clara e rótulo correto
        fig_faltas = px.bar(faltas_por_faixa, 
                            title='Porcentagem de Faltas por Faixa Etária', 
                            labels={'value': 'Porcentagem de Faltas', 'faixa_etaria': 'Faixa Etária'},  # Corrigindo o rótulo 'value'
                            color_discrete_sequence=px.colors.qualitative.Bold,
                            text_auto='.2s'   
                            # color_discrete_sequence=['#FF7F7F'] # Vermelho claro
                            )  

        fig_faltas.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',  
            paper_bgcolor='rgba(0, 0, 0, 0)', 
            font_color='white', 
            width=1200,
            height=500, 
            showlegend=False,  # remove a legenda 

            # Configurar cor e tamanho da fonte dos rótulos dos eixos
            xaxis=dict( # xaxis=dict(gridcolor='red'), 
                title=dict(text='', font=dict(size=15, color=cor_clara)), 
                tickfont=dict(size=15, color=cor_clara)
            ),

            yaxis=dict(gridcolor=cor_clara,
                title=dict(text=texto_y, font=dict(size=18, color=cor_clara)),  
                tickfont=dict(size=18, color=cor_clara),
                tickprefix='% ',
            ),
        )

        fig_faltas.update_traces(
            # Configurar a cor e a fonte do hover_data
            hoverlabel=dict(
                bgcolor='#0C2D57',  
                font=dict(family='Arial', size=15, color='white'), 
                namelength=-1  # Mostra o nome completo mesmo que seja longo  
            ),   

            # Aumentar o tamanho do rótulo das barras
            textfont=dict(size=15, color='white')
        )


        # Exibindo o gráfico no Streamlit
        st.plotly_chart(fig_faltas)


def graph_distribuicao_sexo(df):
    
    # Contando o número de alunos por Gênero
    sexo_contagem = df['sexo_aluno'].value_counts()

    # Dicionário para os rótulos de Gênero
    sexo_labels = {0: 'Masculino', 1: 'Feminino'}

    # Gráfico de pizza para mostrar a distribuição de Gênero
    fig_sexo_pizza = px.pie(values=sexo_contagem.values, 
                            names=sexo_contagem.index.map(sexo_labels),
                            title='Distribuição de Alunos por Gênero',
                            # color_discrete_sequence=px.colors.qualitative.Bold
                            color=sexo_labels,  # Especifica personalizar as cores por Status
                            color_discrete_map={'Masculino': '#A04747', 'Feminino': '#229799'}  # Mapeia as cores
                            )


    # Ajustando o layout com fundo escuro
    fig_sexo_pizza.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',  
        paper_bgcolor='rgba(0, 0, 0, 0)', 
        font_color='white',
        width=600,
        height=500,                   
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_sexo_pizza)


def graph_porcentagem_presenca_genero(df):

    cor_clara = '#DCF2F1'
    texto_y = 'Porcentagem'

    # Juntando as tabelas de frequência e aluno para trazer o sexo dos alunos
    # df_sexo_freq = pd.merge(df_diarioFreq, df_aluno[['id_aluno', 'sexo_aluno']], on='id_aluno', how='inner')
    df_sexo_freq = df.drop_duplicates(subset=['id_aluno'], keep='first')

    # Removendo quaisquer valores nulos (se houver)
    df_sexo_freq.dropna(subset=['presente', 'sexo_aluno'], inplace=True)

    # Calculando a porcentagem de presença por sexo
    presenca_por_sexo = df_sexo_freq.groupby('sexo_aluno')['presente'].mean() * 100

    # Calculando a porcentagem de faltas por sexo
    faltas_por_sexo = 100 - presenca_por_sexo

    # Criando um DataFrame para presença e faltas
    df_presenca_faltas = pd.DataFrame({
        'Gênero': ['Masculino', 'Feminino'],
        'Presença (%)': [presenca_por_sexo[0], presenca_por_sexo[1]],
        'Faltas (%)': [faltas_por_sexo[0], faltas_por_sexo[1]]
    })

    # print("Porcentagem de Presença por Sexo:")
    # print(presenca_por_sexo)
    # print("\nPorcentagem de Faltas por Sexo:")
    # print(faltas_por_sexo)

    # Transformando o DataFrame para gráfico empilhado
    df_presenca_faltas_melt = df_presenca_faltas.melt(id_vars='Gênero', 
                                                    value_vars=['Presença (%)', 'Faltas (%)'], 
                                                    var_name='Status Gênero', 
                                                    value_name='Porcentagem')

    # Gráfico de barras empilhadas com plotly
    fig = px.bar(df_presenca_faltas_melt, 
                x='Gênero', 
                y='Porcentagem', 
                color='Status Gênero', 
                title='Porcentagem de Presença e Faltas por Gênero',
                color_discrete_sequence=['#1f77b4', '#FF7F7F'],
                text_auto='.2s')  # Azul para presença, vermelho claro para faltas

    # Ajustando o layout com fundo escuro
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',  
        paper_bgcolor='rgba(0, 0, 0, 0)', 
        font_color='white',                
        barmode='stack',
        width=1200,
        height=500,     

    # Configurar cor e tamanho da fonte dos rótulos dos eixos
    xaxis=dict( # xaxis=dict(gridcolor='red'), 
        title=dict(text='', font=dict(size=15, color=cor_clara)), 
        tickfont=dict(size=15, color=cor_clara)
    ),

    yaxis=dict(gridcolor=cor_clara,
        title=dict(text=texto_y, font=dict(size=18, color=cor_clara)),  
        tickfont=dict(size=18, color=cor_clara),
        tickprefix='% ',
    ), 

    )


    fig.update_traces(
    # Configurar a cor e a fonte do hover_data
    hoverlabel=dict(
        bgcolor='#0C2D57',  
        font=dict(family='Arial', size=15, color='white'), 
        namelength=-1  # Mostra o nome completo mesmo que seja longo  
    ),   

    # Aumentar o tamanho do rótulo das barras
    textfont=dict(size=15, color='white')
        )


    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig)


def graph_presenca_raca_cor(df):

    cor_clara = '#DCF2F1'
    texto_y = 'Número de Alunos'

    df = df.drop_duplicates(subset=['id_aluno'], keep='first')

    # Selecionando as colunas relacionadas por raça/cor
    raca_colunas = [col for col in df.columns if col.startswith('raca_aluno')]

    # Calculando a contagem de alunos para cada raça/cor
    distribuicao_raca = df[raca_colunas].sum()

    # Transformando o índice para um formato mais amigável e removendo 'None'
    distribuicao_raca.index = distribuicao_raca.index.str.replace('raca_aluno_', '')

    # Filtrando a categoria 'None'
    distribuicao_raca = distribuicao_raca[distribuicao_raca.index != 'None']

    # Mapeando as categorias para os novos rótulos
    raca_mapeamento = {
        'B': 'Branco',
        'A': 'Amarelo',
        'I': 'Indígena',
        'N': 'Preto',
        'P': 'Preto',
        'R': 'Pardo'
    }

    # Aplicando o mapeamento de categorias
    distribuicao_raca.index = distribuicao_raca.index.map(raca_mapeamento)

    # Agrupando as categorias "N" e "P" como "Preto"
    distribuicao_raca_agrupada = distribuicao_raca.groupby(distribuicao_raca.index).sum()

    # Gráfico de barras para mostrar a distribuição por raça/cor
    fig_raca = px.bar(distribuicao_raca_agrupada, 
                    x=distribuicao_raca_agrupada.index, 
                    y=distribuicao_raca_agrupada.values,
                    title='Distribuição de Alunos por Raça/Cor',
                    labels={'y': 'Número de Alunos', 'x': 'Raça/Cor'},
                    color_discrete_sequence=['#1f77b4'],
                    text_auto='.2s')

    # Ajustando o layout com fundo escuro
    fig_raca.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',  
        paper_bgcolor='rgba(0, 0, 0, 0)', 
        font_color='white',
        width=1200,
        height=500,   


    # Configurar cor e tamanho da fonte dos rótulos dos eixos
    xaxis=dict( # xaxis=dict(gridcolor='red'), 
        title=dict(text='', font=dict(size=15, color=cor_clara)), 
        tickfont=dict(size=15, color=cor_clara)
    ),

    yaxis=dict(gridcolor=cor_clara,
        title=dict(text=texto_y, font=dict(size=18, color=cor_clara)),  
        tickfont=dict(size=18, color=cor_clara),
        tickprefix='UN ',
    ), 

    )

    fig_raca.update_traces(
        # Configurar a cor e a fonte do hover_data
        hoverlabel=dict(
            bgcolor='#0C2D57',  
            font=dict(family='Arial', size=15, color='white'), 
            namelength=-1  # Mostra o nome completo mesmo que seja longo  
        ),   

        # Aumentar o tamanho do rótulo das barras
        textfont=dict(size=15, color='white')
            )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_raca)


def graph_porcento_presenca_raca_cor(df):

    cor_clara = '#DCF2F1'
    texto_y = 'Porcentagem'

    df = df.drop_duplicates(subset=['id_aluno'], keep='first')

    # Mapeando as categorias de raça/cor
    raca_mapeamento = {
        'B': 'Branco',
        'A': 'Amarelo',
        'I': 'Indígena',
        'N': 'Preto',
        'P': 'Preto',
        'R': 'Pardo'
    }

    # Filtrando as colunas de raça/cor, excluindo 'None'
    raca_colunas = [col for col in df.columns if col.startswith('raca_aluno') and col != 'raca_aluno_None']
    
    df_raca_freq = df

    # Calculando a porcentagem de presença por raça/cor
    presenca_por_raca = {}
    for raca in raca_colunas:
        media_presenca = df_raca_freq.groupby(raca)['presente'].mean()[1] * 100  # A média de presença para alunos com aquela raça
        
        # Usando o mapeamento diretamente na string do nome da raça
        raca_label = raca.replace('raca_aluno_', '')
        raca_label = raca_mapeamento.get(raca_label, raca_label)  # Aplicando o mapeamento
        presenca_por_raca[raca_label] = media_presenca

    # Criando o DataFrame para presença e faltas
    df_presenca_raca = pd.DataFrame.from_dict(presenca_por_raca, orient='index', columns=['Presença (%)'])
    df_presenca_raca['Faltas (%)'] = 100 - df_presenca_raca['Presença (%)']

    # Transformando o DataFrame para o formato adequado para o gráfico
    df_presenca_raca_melt = df_presenca_raca.reset_index().melt(id_vars='index', 
                                                                value_vars=['Presença (%)', 'Faltas (%)'], 
                                                                var_name='Status', 
                                                                value_name='Porcentagem')

    # Gráfico de barras empilhadas para presença e faltas por raça/cor
    fig_raca_freq = px.bar(df_presenca_raca_melt, 
                        x='index', 
                        y='Porcentagem', 
                        color='Status', 
                        title='Porcentagem de Presença e Faltas por Raça/Cor',
                        labels={'index': 'Raça/Cor'},
                        color_discrete_sequence=['#1f77b4', '#FF7F7F'],
                        text_auto='.2s')  # Azul para presença, vermelho claro para faltas

    # Ajustando o layout com fundo escuro
    fig_raca_freq.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',  
        paper_bgcolor='rgba(0, 0, 0, 0)', 
        font_color='white',               
        barmode='stack',                   
        width=1200,
        height=500,   

    # Configurar cor e tamanho da fonte dos rótulos dos eixos
    xaxis=dict( # xaxis=dict(gridcolor='red'), 
        title=dict(text='', font=dict(size=15, color=cor_clara)), 
        tickfont=dict(size=15, color=cor_clara)
    ),

    yaxis=dict(gridcolor=cor_clara,
        title=dict(text=texto_y, font=dict(size=18, color=cor_clara)),  
        tickfont=dict(size=18, color=cor_clara),
        tickprefix='% ',
    ), 
    
    )

    fig_raca_freq.update_traces(
        # Configurar a cor e a fonte do hover_data
        hoverlabel=dict(
            bgcolor='#0C2D57',  
            font=dict(family='Arial', size=15, color='white'), 
            namelength=-1  # Mostra o nome completo mesmo que seja longo  
        ),   

        # Aumentar o tamanho do rótulo das barras
        textfont=dict(size=15, color='white')
            )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_raca_freq)


def graph_presenca_pais(df):

    cor_clara = '#DCF2F1'
    texto_y = 'Porcentagem'

    # df = df.drop_duplicates(subset=['id_aluno'], keep='first')

    # Criando uma nova coluna para categorizar os alunos
    df['categoria_pais'] = df.apply(lambda row: 'Ambos Pais' if row['tem_pai'] == 1 and row['tem_mae'] == 1 
                                    else 'Só Pai ou Só Mãe' if row['tem_pai'] != row['tem_mae'] 
                                    else 'Sem Pais', axis=1)

    # Calculando a média de presença para cada categoria
    presenca_categoria = df.groupby('categoria_pais')['presente'].mean() * 100
    faltas_categoria = 100 - presenca_categoria

    # Criando DataFrame para visualização dos resultados
    df_categoria_pais = pd.DataFrame({
        'Categoria': ['Ambos Pais', 'Só Pai ou Só Mãe', 'Sem Pais'],
        'Presença (%)': presenca_categoria.values,
        'Faltas (%)': faltas_categoria.values
    })

    # Transformando o DataFrame para gráfico empilhado
    df_categoria_pais_melt = df_categoria_pais.melt(id_vars='Categoria', 
                                                    value_vars=['Presença (%)', 'Faltas (%)'], 
                                                    var_name='Status', 
                                                    value_name='Porcentagem')

    # Gráfico de barras empilhadas para presença e faltas por categoria
    fig_categoria_pais = px.bar(df_categoria_pais_melt, 
                                x='Categoria', 
                                y='Porcentagem', 
                                color='Status', 
                                title='Presença e Faltas por Categoria de Pais',
                                color_discrete_sequence=['#1f77b4', '#FF7F7F'],
                                text_auto='.2s')  # Azul para presença, vermelho claro para faltas

    # Ajustando o layout com fundo escuro
    fig_categoria_pais.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',  
        paper_bgcolor='rgba(0, 0, 0, 0)', 
        font_color='white',               
        barmode='stack',                   
        width=1200,
        height=500,   

    # Configurar cor e tamanho da fonte dos rótulos dos eixos
    xaxis=dict( # xaxis=dict(gridcolor='red'), 
        title=dict(text='', font=dict(size=15, color=cor_clara)), 
        tickfont=dict(size=15, color=cor_clara)
    ),

    yaxis=dict(gridcolor=cor_clara,
        title=dict(text=texto_y, font=dict(size=18, color=cor_clara)),  
        tickfont=dict(size=18, color=cor_clara),
        tickprefix='% ',
    ), 
      
    )


    fig_categoria_pais.update_traces(
        # Configurar a cor e a fonte do hover_data
        hoverlabel=dict(
            bgcolor='#0C2D57',  
            font=dict(family='Arial', size=15, color='white'), 
            namelength=-1  # Mostra o nome completo mesmo que seja longo  
        ),   

        # Aumentar o tamanho do rótulo das barras
        textfont=dict(size=15, color='white')
            )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_categoria_pais)


def graph_presenca_pais_mae(df):
    
    cor_clara = '#DCF2F1'
    texto_y = 'Porcentagem'

    # Calculando a média de presença para alunos com e sem pai
    presenca_pai = df.groupby('tem_pai')['presente'].mean() * 100
    faltas_pai = 100 - presenca_pai

    # Calculando a média de presença para alunos com e sem mãe
    presenca_mae = df.groupby('tem_mae')['presente'].mean() * 100
    faltas_mae = 100 - presenca_mae

    # Criando DataFrame para visualização dos resultados
    df_pai_mae = pd.DataFrame({
        'Grupo': ['Tem Pai', 'Não Tem Pai', 'Tem Mãe', 'Não Tem Mãe'],
        'Presença (%)': [presenca_pai[1], presenca_pai[0], presenca_mae[1], presenca_mae[0]],
        'Faltas (%)': [faltas_pai[1], faltas_pai[0], faltas_mae[1], faltas_mae[0]]
    })

    # Transformando o DataFrame para gráfico empilhado
    df_pai_mae_melt = df_pai_mae.melt(id_vars='Grupo', 
                                    value_vars=['Presença (%)', 'Faltas (%)'], 
                                    var_name='Status', 
                                    value_name='Porcentagem')

    # Gráfico de barras empilhadas para presença e faltas por grupo (pai/mãe)
    fig_pai_mae = px.bar(df_pai_mae_melt, 
                        x='Grupo', 
                        y='Porcentagem', 
                        color='Status', 
                        title='Presença e Faltas por Presença de Pai/Mãe',
                        color_discrete_sequence=['#1f77b4', '#FF7F7F'],
                        text_auto='.2s')  # Azul para presença, vermelho claro para faltas

    # Ajustando o layout com fundo escuro
    fig_pai_mae.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',  
        paper_bgcolor='rgba(0, 0, 0, 0)', 
        font_color='white',               
        barmode='stack',
        width=1200,
        height=500,   

    # Configurar cor e tamanho da fonte dos rótulos dos eixos
    xaxis=dict( # xaxis=dict(gridcolor='red'), 
        title=dict(text='', font=dict(size=15, color=cor_clara)), 
        tickfont=dict(size=15, color=cor_clara)
    ),

    yaxis=dict(gridcolor=cor_clara,
        title=dict(text=texto_y, font=dict(size=18, color=cor_clara)),  
        tickfont=dict(size=18, color=cor_clara),
        tickprefix='% ',
    ),                            
    )

    fig_pai_mae.update_traces(
        # Configurar a cor e a fonte do hover_data
        hoverlabel=dict(
            bgcolor='#0C2D57',  
            font=dict(family='Arial', size=15, color='white'), 
            namelength=-1  # Mostra o nome completo mesmo que seja longo  
        ),   

        # Aumentar o tamanho do rótulo das barras
        textfont=dict(size=15, color='white')
            )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_pai_mae)


def graph_disciplina_presenca(df, df_disciplina):

    cor_clara = '#DCF2F1'
    texto_y = 'Porcentagem'

    # Realizando o merge para trazer o nome da disciplina
    df_merged = pd.merge(df, df_disciplina, on='id_disciplina', how='left')

    # Calculando a média de presença por disciplina
    presenca_disciplina = df_merged.groupby('NomeDisciplina')['presente'].mean() * 100
    faltas_disciplina = 100 - presenca_disciplina

    # Criando DataFrame para visualização dos resultados
    df_disciplina_presenca = pd.DataFrame({
        'Disciplina': presenca_disciplina.index,
        'Presença (%)': presenca_disciplina.values,
        'Faltas (%)': faltas_disciplina.values
    })

    # Transformando o DataFrame para gráfico empilhado
    df_disciplina_presenca_melt = df_disciplina_presenca.melt(id_vars='Disciplina', 
                                                            value_vars=['Presença (%)', 'Faltas (%)'], 
                                                            var_name='Status', 
                                                            value_name='Porcentagem')

    # Gráfico de barras empilhadas para presença e faltas por disciplina
    fig_disciplina = px.bar(df_disciplina_presenca_melt, 
                            x='Disciplina', 
                            y='Porcentagem', 
                            color='Status', 
                            title='Presença e Faltas por Disciplina',
                            color_discrete_sequence=['#1f77b4', '#FF7F7F'],
                            text_auto='.2s')  # Azul para presença, vermelho claro para faltas

    # Ajustando o layout com fundo escuro
    fig_disciplina.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)', 
        paper_bgcolor='rgba(0, 0, 0, 0)', 
        font_color='white',               
        barmode='stack',
        width=1200,
        height=600,   

    # Configurar cor e tamanho da fonte dos rótulos dos eixos
    xaxis=dict( # xaxis=dict(gridcolor='red'), 
        title=dict(text='', font=dict(size=15, color=cor_clara)), 
        tickfont=dict(size=15, color=cor_clara)
    ),

    yaxis=dict(gridcolor=cor_clara,
        title=dict(text=texto_y, font=dict(size=18, color=cor_clara)),  
        tickfont=dict(size=18, color=cor_clara),
        tickprefix='% ',
    ),          

    )

    fig_disciplina.update_traces(
        # Configurar a cor e a fonte do hover_data
        hoverlabel=dict(
            bgcolor='#0C2D57',  
            font=dict(family='Arial', size=15, color='white'), 
            namelength=-1  # Mostra o nome completo mesmo que seja longo  
        ),   

        # Aumentar o tamanho do rótulo das barras
        textfont=dict(size=15, color='white')
            )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_disciplina)


