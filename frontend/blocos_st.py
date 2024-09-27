
import streamlit as st
from PIL import Image
from streamlit_extras.metric_cards import style_metric_cards

from backend.predict_passos import predict
from backend.processo_dados import (base_disciplina_aluno, carregar_dados,
                                    pegar_alunos, prepare_datos_predict)
from frontend import blocos_st, controlador

from . import graficos as graf

global data
global df_aluno
global df_disciplina


def setup():

    # -- imagens e logos -- #
    img = './documents/img/onibus-escolar2.png'
    img = Image.open(img)

    # --- Configurações da página 'Geral' --- #
    st.set_page_config(
        page_title='Análise de Presença Escolar',
        page_icon=img,
        layout='wide',
        initial_sidebar_state='expanded',
        # initial_sidebar_state='collapsed',
        menu_items={
            'Get Help': 'https://www.google.com.br/',
            'Report a bug': "https://www.google.com.br/",
            'About': "Esse app foi desenvolvido pela Grupo 38 FIAP."
        }
    )


def style_card_metrica_ajustes():

    # Ajustes dos Cards e layout

    style_metric_cards(background_color='#232D3F', 
                       box_shadow=True, 
                       border_left_color='#EEEEEE', 
                       border_radius_px=10)


def prev(df_aluno, data):
    
    # Ordenar a lista de alunos
    lista_aluno = list(df_aluno.sort_values("nome_id_aluno")["nome_id_aluno"])

    with st.form("my_form"):
        aluno = st.selectbox("Selecione o Aluno", lista_aluno)

        if st.form_submit_button("Prever"):
            # Filtrar pelo aluno selecionado
            df_aluno_filtered = df_aluno[df_aluno["nome_id_aluno"] == aluno]
            id_aluno = df_aluno_filtered["id_aluno"].iloc[0]

            c1, c2 = st.columns([2, 1])

            # Preparar os dados e fazer a previsão
            resp = prepare_datos_predict(data, id_aluno)


            # st.dataframe(resp)


            proba = predict(resp)

            # Exibir as informações do aluno
            with c1:
                st.markdown("##### Aluno Selecionado")
                st.markdown(
                    f"""
                    <p style=''>ID: {df_aluno_filtered['id_aluno'].iloc[0]}</p>
                    <p style='margin-top: -15px'>Nome: {df_aluno_filtered['nome_aluno'].iloc[0]}</p>
                    <p style='margin-top: -15px'>Data Nascimento: {df_aluno_filtered['data_nascimento_aluno'].iloc[0]}</p>
                    <p style='margin-top: -15px'>Sexo: {('Masculino' if df_aluno_filtered['sexo_aluno'].iloc[0] == 1 else 'Feminino')}</p>
                    """,
                    unsafe_allow_html=True,
                )

            # Exibir a probabilidade de comparecimento
            with c2:
                st.markdown(
                    "<div style='margin-bottom: 40px'></div>", unsafe_allow_html=True
                )
                st.metric(
                    label="Probabilidade de comparecer", value=f"{proba[1]*100:.1f}%"
                )
                style_card_metrica_ajustes() # <-- Chama os ajustes do card
            
            # Exibir o gráfico de faltas do aluno
            graf.graph_faltas_aluno(data[data["id_aluno"] == id_aluno])


def init_session_state():

    # # Defina as páginas
    pages = {
        "Introdução": "introducao",
        "Análise Exploratória": "analise_exploratoria",
        "Modelos de Previsão": "modelos_previsao",
    }

    # Adicione a navegação na sidebar
    st.sidebar.title("Navegação")
    selection = st.sidebar.radio("Ir para", list(pages.keys()))

    cor_titulo = '#00ABB3' 
    cor_texto = '#C7C8CC'
    tamanho_texto = '16px'


    data = carregar_dados()
    df_aluno = pegar_alunos()
    df_disciplina = base_disciplina_aluno()

    img_page = './documents/img/Passos-magicos-icon-cor.png'
    img_page = Image.open(img_page)

    if selection == "Introdução":

        st.markdown(f'<h1 style="text-align: left; color: {cor_titulo}; font-size: 40px;">{selection} | DATATHON</h1>', unsafe_allow_html=True)

        st.subheader("", divider="gray")
        # blue, green, orange, red, violet, gray, grey, rainbow.
        
        st.markdown(f'<h1 style="text-align: left; color: {cor_titulo}; font-size: 40px;">Objetivo</h1>', unsafe_allow_html=True)

        st.markdown(f"""<h1 style="text-align: left; color: {cor_texto}; font-size: {tamanho_texto};">
        Este projeto tem como objetivo desenvolver uma análise da presença de alunos em aulas e gerar insight para ação da ONG Passos Mágicos. A análise é baseada no histórico de frequência registrado no diário de classe, além de outras informações relevantes sobre as aulas e os estudantes.<br><br>
        Para garantir uma visão abrangente e robusta, foram utilizados dados de bases distintas, incluindo informações sobre o cadastro de alunos, professores, turmas e disciplinas. 
        """, unsafe_allow_html=True)
    
        st.subheader("", divider="gray")
        
        st.markdown(f'<h1 style="text-align: left; color: {cor_titulo}; font-size: 40px;">ONG (Passos Mágicos)</h1>', unsafe_allow_html=True)
        
        col01, col02 = st.columns(2)

        with col01:
            st.image(img_page, width=250)
        
        with col02:
            st.markdown(""" 
                A Associação Passos Mágicos tem uma trajetória de 30 anos de atuação, trabalhando na transformação da vida de crianças e jovens de baixa renda os levando a melhores oportunidades de vida.
                
                A associação busca instrumentalizar o uso da educação como ferramenta para a mudança das condições de vida das crianças e jovens em vulnerabilidade social. 
                        """)
        st.markdown(""" 
            ### Base de dados

            As bases de dados contém informações educacionais e socioeconômicas dos estudantes da Passos Mágicos.
            Além da base de dados, alguns relatórios de pesquisa realizada pela Passos Mágicos também foram disponibilizados para auxiliar no conhecimento do negócio.

            Para mais detalhes, acessar o site oficial da Passos Mágicos: [Passos Mágicos Quem Somos](https://passosmagicos.org.br/quem-somos/) | [Passos Mágicos home](https://passosmagicos.org.br)
                    """)


    elif selection == "Análise Exploratória":

        st.markdown(f'<h1 style="text-align: left; color: {cor_titulo}; font-size: 40px;">{selection}</h1>', unsafe_allow_html=True)
        
        st.subheader("", divider="gray")

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['📒 Análise de Presença', 
                                                '🌍 Análise Demográfica dos Alunos', 
                                                '🚻 Distribuição por Gênero',
                                                '🌓 Distribuição por Raça/Cor',
                                                '👨‍👨‍👦 Correlação entre Pais e Presença',
                                                '📚 Disciplina e Presença']
                                                )
 
        with tab1:
            col1, col2 = st.columns(2)

            with col1:
                controlador.texto_tab1_col1()

            with col2:
                graf.graph_presenca_aluno(data)
                    
            st.subheader("", divider="gray")

            texto_titulo_base = 'Gráfico da taxa de presença por dia da semana'

            st.markdown(f'<h1 style="text-align: left; color: {cor_texto}; font-size: 18px;">{texto_titulo_base}:</h1>', unsafe_allow_html=True)


            var_presente = st.radio("**Selecione:**", 
                    options=['Presença', 'Faltas'], 
                    key='presente')

            graf.graph_frequencia_aluno_semanal(data, var_presente)

            if var_presente == 'Presença':
                controlador.texto_tab1_presente()

            elif var_presente == 'Faltas':
                controlador.texto_tab1_falta()
               

        with tab2:

            st.markdown("""
            ### Distribuição de Idade dos Alunos

            - Qual a faixa etária predominante dos alunos? 
            - Existe uma correlação entre idade e presença nas aulas?""")

            df_alunos = data.drop_duplicates(subset=['id_aluno'], keep='first')

            st.write(df_alunos[['idade_aluno']].describe().T)

            graf.graph_distribuicao(data)

            controlador.texto_analise_distribuicao_idade()

            var_presente = st.radio("**Selecione:**", 
            options=['Presença', 'Faltas'], 
            key='presente_2')

            graf.graph_frequencia_aluno_idade(data, var_presente)

            controlador.texto_analise_correlacao_idade()


        with tab3:

            col3, col4 = st.columns(2)
            with col3:
                controlador.texto_distribuicao_sexo()

            with col4:
                graf.graph_distribuicao_sexo(data)

            graf.graph_porcentagem_presenca_genero(data)

            controlador.texto_analise_genero()


        with tab4:
            
            controlador.texto_distribuicao_raca_cor()
            
            graf.graph_presenca_raca_cor(data)

            controlador.texto_analise_raca_cor()

            graf.graph_porcento_presenca_raca_cor(data)

            controlador.texto_analise_raca_presenca()


        with tab5:
            
            controlador.texto_correlacao_pais_presenca()

            graf.graph_presenca_pais(data)

            controlador.texto_analise_pais_presenca()

            st.divider()

            controlador.texto_cabecalho_analise_pais_presenca()

            graf.graph_presenca_pais_mae(data)

            controlador.texto_analise_pais_presenca_mae()


        with tab6:
            
            controlador.texto_titulo_disciplina_presenca()

            graf.graph_disciplina_presenca(data, df_disciplina)

            controlador.texto_analise_disciplina_presenca()


    elif selection == "Modelos de Previsão":

        st.markdown(f'<h1 style="text-align: left; color: {cor_titulo}; font-size: 40px;">{selection}</h1>', unsafe_allow_html=True)

        st.subheader("", divider="gray")
           
        controlador.texto_modelo_avaliacao()

        st.latex(r"\text{Prediction} = \frac{1}{n_{\text{trees}}} \sum_{i=1}^{n_{\text{trees}}} \text{Tree}_i(\text{input})")


        blocos_st.prev(df_aluno, data)
            
    st.markdown("""
    <style>
        [data-testid=stSidebar] {background-color: #304463;}
    </style> """, unsafe_allow_html=True)

    with st.sidebar:
        
        st.divider()

        st.subheader("Alunos do Grupo 38:")
        st.write("**Leandro Braga Alves** <br> RM :orange[353057] | 3DTAT", unsafe_allow_html=True)
        st.write("**Rodrigo Mitsuo Yoshida** <br> RM :orange[35274] | 3DTAT", unsafe_allow_html=True)
        st.write("**Roberto Yukio Ihara** <br> RM :orange[35274] | 3DTAT", unsafe_allow_html=True)


        st.divider()



