from datetime import datetime

import pandas as pd
import spacy
import streamlit as st
from spacy.util import is_package

global local_arquivos_analise



local_arquivos_analise = './documents/base dados/'

@st.cache_data()
def criando_dataframe():

    # df_diarioFreq -- Lendo os arquivos CSV --


    df_diarioFreq = pd.read_csv(local_arquivos_analise + "TbDiario/Originais anonimizados/TbDiarioFrequencia.csv")

    # Selecionando as colunas e aplicando a lógica condicional
    df_diarioFreq = df_diarioFreq[['IdDiarioAula', 'IdAluno', 'StPresencaFalta']].rename(
        columns={
            'IdDiarioAula': 'id_diario_aula',
            'IdAluno': 'id_aluno'
        }
    )

    # Aplicando a lógica para a coluna de presença
    df_diarioFreq['presente'] = df_diarioFreq['StPresencaFalta'].apply(lambda x: 1 if x == 'P' else 0)


    # df_diarioAula -- Lendo os arquivos CSV --


    df_diarioAula = pd.read_csv(local_arquivos_analise + "TbDiario/Originais anonimizados/TbDiarioAula.csv")

    # Selecionando e renomeando colunas
    df_diarioAula = df_diarioAula[['IdDiarioAula', 'IdDiario', 'DataAula', 'NumeroAula', 'ConteudoMinistrado', 'IdProfessor']].rename(
        columns={
            'IdDiarioAula': 'id_diario_aula',
            'IdDiario': 'id_diario',
            'DataAula': 'data_aula',
            'NumeroAula': 'num_aula',
            'ConteudoMinistrado': 'conteudo_ministrado',
            'IdProfessor': 'id_professor'
        }
    )

    # Convertendo a coluna de data para datetime e extraindo o dia da semana
    df_diarioAula['data_aula'] = pd.to_datetime(df_diarioAula['data_aula'], format="%Y-%m-%d %H:%M:%S")
    df_diarioAula['dia_semana'] = df_diarioAula['data_aula'].dt.weekday

    # Criando variáveis dummy para o dia da semana
    df_diarioAula = pd.get_dummies(df_diarioAula, columns=['dia_semana'])

    # Ordenando pelo campo 'data_aula' e 'num_aula'
    df_diarioAula = df_diarioAula.sort_values(by=['data_aula', 'num_aula'])
    
    
    # df_diario -- Lendo os arquivos CSV --


    df_diario = pd.read_csv(local_arquivos_analise + "TbDiario/Originais anonimizados/TbDiario.csv")

    # Selecionando e renomeando as colunas
    df_diario = df_diario[['IdDiario', 'IdTurma', 'IdDisciplina']].rename(
        columns={
            'IdDiario': 'id_diario',
            'IdTurma': 'id_turma',
            'IdDisciplina': 'id_disciplina'
        }
    )


    # df_turma -- Lendo os arquivos CSV --


    df_turma = pd.read_csv(local_arquivos_analise + "TbTurma/Originais anonimizados/TbTurma.csv")

    # Selecionando e renomeando as colunas
    df_turma = df_turma[['IdTurma', 'IdSerie', 'IdPeriodo', 'TurnoPrincipal']].rename(
        columns={
            'IdTurma': 'id_turma',
            'IdSerie': 'id_serie',
            'IdPeriodo': 'id_periodo'
        }
    )

    # Aplicando a lógica condicional para a coluna 'TurnoPrincipal'
    df_turma['turno_turma'] = df_turma['TurnoPrincipal'].apply(lambda x: 
        0 if x == "M" else 
        1 if x == "T" else 
        2 if x == "N" else 
        3 if x == "Z" else 4
    )

    
    # df_aluno -- Lendo os arquivos CSV --


    df_aluno = pd.read_csv(local_arquivos_analise + "TbAluno/Originais anonimizados/TbAluno.csv")

    # Selecionando e renomeando as colunas
    df_aluno = df_aluno[['IdAluno', 'DataNascimento', 'Sexo', 'IdPai', 'IdMae', 'CorRaca']].rename(
        columns={
            'IdAluno': 'id_aluno',
            'DataNascimento': 'data_nascimento_aluno'
        }
    )

    # Convertendo a coluna de data de nascimento para datetime
    df_aluno['data_nascimento_aluno'] = pd.to_datetime(df_aluno['data_nascimento_aluno'], format="%Y-%m-%d %H:%M:%S", errors='coerce')

    # Calculando a idade do aluno
    df_aluno['idade_aluno'] = datetime.now().year - df_aluno['data_nascimento_aluno'].dt.year

    # Aplicando a lógica condicional para a coluna 'Sexo'
    df_aluno['sexo_aluno'] = df_aluno['Sexo'].apply(lambda x: 0 if x == "M" else 1)

    # Verificando se o campo 'IdPai' e 'IdMae' são nulos
    df_aluno['tem_pai'] = df_aluno['IdPai'].apply(lambda x: 0 if pd.isnull(x) else 1)
    df_aluno['tem_mae'] = df_aluno['IdMae'].apply(lambda x: 0 if pd.isnull(x) else 1)

    # Substituindo valores nulos na coluna 'CorRaca' por "None"
    df_aluno['raca_aluno'] = df_aluno['CorRaca'].fillna("None")

    # Criando variáveis dummy para a coluna 'raca_aluno'
    df_aluno = pd.get_dummies(df_aluno, columns=['raca_aluno'])


    # df_professor -- Lendo os arquivos CSV --


    df_professor = pd.read_csv(local_arquivos_analise + "TbProfessor/Originais anonimizados/TbProfessor.csv")

    # Selecionando e renomeando as colunas
    df_professor = df_professor[['IdProfessor', 'DataNascimento', 'Sexo', 'CorRaca', 'Cargo']].rename(
        columns={
            'IdProfessor': 'id_professor',
            'DataNascimento': 'data_nascimento_professor',
            'CorRaca': 'raca_professor',
            'Cargo': 'cargo_professor'
        }
    )

    # Convertendo a coluna de data de nascimento para datetime
    df_professor['data_nascimento_professor'] = pd.to_datetime(df_professor['data_nascimento_professor'], format="%Y-%m-%d %H:%M:%S", errors='coerce')

    # Calculando a idade do professor
    df_professor['idade_professor'] = datetime.now().year - df_professor['data_nascimento_professor'].dt.year

    # Aplicando a lógica condicional para a coluna 'Sexo'
    df_professor['sexo_professor'] = df_professor['Sexo'].apply(lambda x: 0 if x == "M" else 1)

    # Preenchendo valores nulos na coluna 'Cargo'
    df_professor['cargo_professor'] = df_professor['cargo_professor'].fillna("Nenhum")

    # Criando variáveis dummy para as colunas 'raca_professor' e 'cargo_professor'
    df_professor = pd.get_dummies(df_professor, columns=['raca_professor', 'cargo_professor'])

    # Convertendo as colunas 'id_professor' para o tipo (string)
    df_professor['id_professor'] = df_professor['id_professor'].astype(str)


    # Merge de todos os dataframes

    # Realizando os merges (junção) usando pandas
    df_raw = pd.merge(df_diarioFreq, df_aluno, on="id_aluno", how="left")
    df_raw = pd.merge(df_raw, df_diarioAula, on="id_diario_aula", how="left")
    df_raw = pd.merge(df_raw, df_professor, on="id_professor", how="left")
    df_raw = pd.merge(df_raw, df_diario, on="id_diario", how="left")
    df_raw = pd.merge(df_raw, df_turma, on="id_turma", how="left")

    # Ordenar o DataFrame pelas colunas 'id_aluno' e 'data_aula'
    df_seq = df_raw.sort_values(by=["id_aluno", "data_aula"]).copy()

    # Criar a coluna 'seq_presenca' com a sequência ordinal por aluno
    df_seq['seq_presenca'] = df_seq.groupby('id_aluno').cumcount() + 1


    return df_seq


@st.cache_data()
def pegar_alunos():

    df_aluno = pd.read_csv(local_arquivos_analise + "TbAluno/Originais anonimizados/TbAluno.csv")

        # Selecionar e renomear colunas
    df_aluno = df_aluno.rename(columns={
        "IdAluno": "id_aluno",
        "NomeAluno": "nome_aluno",
        "DataNascimento": "data_nascimento_aluno"
    })

    # Converter a coluna 'DataNascimento' para o formato de data
    df_aluno['data_nascimento_aluno'] = pd.to_datetime(df_aluno['data_nascimento_aluno'], format="%Y-%m-%d %H:%M:%S", errors='coerce')

    # Converter a coluna 'Sexo' para 0 e 1 (0 para 'M', 1 para 'F')
    df_aluno['sexo_aluno'] = df_aluno['Sexo'].map({'M': 0, 'F': 1})

    # Criar a coluna 'nome_id_aluno' concatenando 'nome_aluno' e 'id_aluno'
    df_aluno['nome_id_aluno'] = df_aluno['nome_aluno'] + " - ID: " + df_aluno['id_aluno'].astype(str)
    
    return df_aluno

@st.cache_data()
def base_disciplina_aluno():
    df_disciplina = pd.read_csv(local_arquivos_analise + "TbDisciplina/Originais anonimizados/TbDisciplina.csv")

    df_disciplina = df_disciplina[['IdDisciplina', 'NomeDisciplina']]

    df_disciplina.columns = ['id_disciplina', 'NomeDisciplina']

    return df_disciplina



def prepare_datos_predict(df: pd.DataFrame, id_aluno):

    df = df.sort_values(['id_aluno', 'data_aula']).copy()

    # Criando a coluna 'seq_presenca' com a sequência ordinal de presença para cada aluno
    df['seq_presenca'] = df.groupby('id_aluno').cumcount() + 1

    # Filtrando o dataframe para o id_aluno específico
    df_aluno = df[df["id_aluno"] == id_aluno]

    # Calculando as janelas de presença
    inicio_janela = df_aluno["seq_presenca"].max() - 10
    fim_janela = df_aluno["seq_presenca"].max()


    def load_spacy_model():
        # Verifica se o modelo já está instalado
        if not is_package("pt_core_news_sm"):
            # Faz o download do modelo caso não esteja instalado
            from spacy.cli import download
            download("pt_core_news_sm")
        # Carrega o modelo de linguagem
        return spacy.load("pt_core_news_sm")

    # Carregando o modelo de NLP
    nlp = load_spacy_model()

    # Função para criar embeddings
    def criar_embedding(texto):
        doc = nlp(texto)
        return doc.vector.tolist()

    # Filtrando o dataframe nas janelas de presença
    df_janela = df_aluno[(df_aluno["seq_presenca"] >= inicio_janela) & (df_aluno["seq_presenca"] <= fim_janela)]

    # Agrupando os dados e criando as agregações necessárias
    df_agg = df_janela.groupby("id_aluno").agg({
        "data_aula": ["first", "last"],
        "dia_semana_0": "sum",
        "dia_semana_1": "sum",
        "dia_semana_2": "sum",
        "dia_semana_3": "sum",
        "dia_semana_4": "sum",
        "dia_semana_5": "sum",
        "dia_semana_6": "sum",
        "conteudo_ministrado": lambda x: " ".join(x),  # Concatenando o conteúdo
        "sexo_aluno": "first",
        "tem_pai": "first",
        "tem_mae": "first",
        "raca_aluno_A": "first",
        "raca_aluno_B": "first",
        "raca_aluno_I": "first",
        "raca_aluno_N": "first",
        "raca_aluno_None": "first",
        "raca_aluno_P": "first",
        "raca_aluno_R": "first",
        "idade_aluno": "mean",
        "sexo_professor": "sum",
        "raca_professor_A": "sum",
        "raca_professor_B": "sum",
        "raca_professor_N": "sum",
        "raca_professor_P": "sum",
        "raca_professor_R": "sum",
        "cargo_professor_Nenhum": "sum",
        "cargo_professor_Neuropsicóloga": "sum",
        "cargo_professor_Professor": "sum",
        "cargo_professor_Professor Inglês": "sum",
        "cargo_professor_Professor de Inglês": "sum",
        "cargo_professor_Professor de Matemática": "sum",
        "cargo_professor_Professora": "sum",
        "cargo_professor_Professora de Inglês": "sum",
        "cargo_professor_Professora de Matemática": "sum",
        "cargo_professor_Professora/Coordenadora": "sum",
        "cargo_professor_Psicóloga": "sum",
        "cargo_professor_Psicólogo": "sum",
        "idade_professor": "mean",
        "id_professor": pd.Series.nunique,  # Número de professores diferentes
        "id_disciplina": pd.Series.nunique,  # Número de disciplinas diferentes
        "id_serie": pd.Series.nunique,  # Número de séries diferentes
        "id_turma": pd.Series.nunique,  # Número de turmas diferentes
        "presente": ["sum", "count"],  # Soma e contagem de presenças
        "seq_presenca": lambda x: x[df_janela["presente"] == 1].max()  # Última presença
    })

    # Ajustando os nomes das colunas agregadas
    df_agg.columns = ["_".join(col).strip() if isinstance(col, tuple) else col for col in df_agg.columns]

    # Renomeando as colunas geradas pelo `groupby` para seguir o padrão desejado
    df_agg.rename(columns={
        'conteudo_ministrado_<lambda>': 'conteudo_ministrado_concat',
        'seq_presenca_<lambda>': 'ultima_presenca',
        'dia_semana_0_sum': 'sum_dia_semana_1',
        'dia_semana_1_sum': 'sum_dia_semana_2',
        'dia_semana_2_sum': 'sum_dia_semana_3',
        'dia_semana_3_sum': 'sum_dia_semana_4',
        'dia_semana_4_sum': 'sum_dia_semana_5',
        'dia_semana_5_sum': 'sum_dia_semana_6',
        'dia_semana_6_sum': 'sum_dia_semana_7',
        'sexo_aluno_first': 'sexo_aluno',
        'tem_pai_first': 'tem_pai',
        'tem_mae_first': 'tem_mae',
        'raca_aluno_A_first': 'raca_aluno_A',
        'raca_aluno_B_first': 'raca_aluno_B',
        'raca_aluno_I_first': 'raca_aluno_I',
        'raca_aluno_N_first': 'raca_aluno_N',
        'raca_aluno_None_first': 'raca_aluno_None',
        'raca_aluno_P_first': 'raca_aluno_P',
        'raca_aluno_R_first': 'raca_aluno_R',
        'idade_aluno_mean': 'idade_aluno_media',
        'cargo_professor_Professor Inglês_sum': 'cargo_professor_Professor_Inglês_sum',
        'cargo_professor_Professor de Inglês_sum': 'cargo_professor_Professor_de_Inglês_sum',
        'cargo_professor_Professor de Matemática_sum': 'cargo_professor_Professor_de_Matemática_sum',
        'cargo_professor_Professora de Inglês_sum': 'cargo_professor_Professora_de_Inglês_sum',
        'cargo_professor_Professora de Matemática_sum': 'cargo_professor_Professora_de_Matemática_sum',
        'cargo_professor_Professora/Coordenadora_sum': 'cargo_professor_Professora_Coordenadora_sum',
        'idade_professor_mean': 'idade_professor_media',
        'id_professor_nunique': 'num_professores',
        'id_disciplina_nunique': 'num_disciplinas',
        'id_serie_nunique': 'num_series',
        'id_turma_nunique': 'num_turmas',
        'presente_sum': 'num_presencas',
        'presente_count': 'num_aulas'
    }, inplace=True)

    # Adicionando a coluna 'last_seq'
    df_agg["last_seq"] = fim_janela

    # Criando os embeddings para o conteúdo ministrado
    df_agg["conteudo_embedding"] = df_agg["conteudo_ministrado_concat"].apply(criar_embedding)

    # Remove a coluna 'conteudo_embedding' antiga e expande os embeddings
    abt_filtered = df_agg.drop(columns=['conteudo_embedding', 'conteudo_ministrado_concat'])

    # Expande a lista de embeddings (conteúdo_embedding) em múltiplas colunas
    conteudo_embedding_expanded = pd.DataFrame(df_agg['conteudo_embedding'].tolist(), index=df_agg.index)

    # Converte as colunas numéricas de embeddings para strings representando números
    conteudo_embedding_expanded.columns = [str(i) for i in range(conteudo_embedding_expanded.shape[1])]

    # Concatena o DataFrame original com as novas colunas de embedding
    abt_final = pd.concat([abt_filtered, conteudo_embedding_expanded], axis=1)

    # Preenchendo os valores NaN da coluna 'ultima_presenca' com a média de 'num_presenca'
    media_presenca = abt_final['num_presencas'].mean()
    abt_final['ultima_presenca'].fillna(media_presenca, inplace=True)

    # Retornando o dataframe final
    return abt_final.reset_index()


def carregar_dados():
    return criando_dataframe()
