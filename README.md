# fiap_datathon

# PÓS TECH - Datathon: Passos Mágicos 🎓

## 💻 Sobre o Datathon

O objetivo principal deste Datathon é promover a criação de uma proposta que ajude a ONG “Passos Mágicos” a entender e aprimorar seu impacto na comunidade. Esta ONG usa a educação como ferramenta para transformar as condições de vida de crianças e jovens em situação de vulnerabilidade social.

### Propostas:

1. **🎯 Proposta Analítica**:

   - Demonstrar o impacto da ONG na performance dos estudantes.
   - Criar um **dashboard** e **storytelling** para contar a história dos dados, gerando insights para tomada de decisão.
   - Foco na análise de indicadores de desempenho e no perfil dos alunos.

2. **🔮 Proposta Preditiva**:
   - Criar um **modelo preditivo** para prever o comportamento dos estudantes.
   - Utilizar algoritmos de aprendizado supervisionado ou não supervisionado, como **machine learning**, **deep learning** ou **NLP**.
   - Usar a criatividade para propor soluções que ajudem a identificar o desenvolvimento dos alunos.

### Base de Dados 🎲

Os dados fornecidos incluem informações **educacionais** e **socioeconômicas** dos estudantes da ONG nos anos de 2020, 2021 e 2023, com dois datasets distintos e um **dicionário de dados**. Além disso, relatórios de pesquisa realizados pela ONG serão disponibilizados para melhor compreensão do contexto.

---

## 🎯 Projeto de Previsão de Presença de Alunos

Este projeto tem como foco a previsão de ausência ou presença de alunos nas aulas, utilizando dados históricos de frequência e outras informações relevantes sobre os alunos e as aulas.

### Etapas:

1. **Balanceamento de Dados**:
   - Uso do **RandomUnderSampler** para equilibrar a distribuição de presença/ausência.
2. **Modelo RandomForest com Hiperparâmetros Otimizados**:
   - Uso de **RandomForestClassifier** com otimização de hiperparâmetros via **RandomizedSearchCV** para maximizar a precisão das previsões.

---

## Acessos e Repositórios

- **Link do Dashboard (Streamlit)**: [Link Dashboard Passos Mágicos ](https://fiapdatathongrupo38.streamlit.app/)
- **Repositório do Streamlit**: [GIT Streamlit](https://github.com/Leandro-Braga/fiap_datathon)
- **Notebook do Projeto**: [GIT Notebook](https://github.com/Leandro-Braga/fiap_datathon/tree/14e5a62762964dc8a3e45b327ca9a6104a739d9b/notebook)

### Passos para Acessar o Projeto:

1. Clone o repositório:
   ```bash
   git clone https://github.com/Leandro-Braga/fiap_datathon.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd fiap_datathon
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o aplicativo Streamlit:
   ```bash
   streamlit run app.py
   ```
