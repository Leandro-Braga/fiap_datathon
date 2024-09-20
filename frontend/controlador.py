import streamlit as st

cor_titulo = '#00ABB3' 
cor_texto = '#C7C8CC'
tamanho_texto = '16px'

def texto_tab1_col1():

    st.markdown(f'<h1 style="text-align: left; color: {cor_texto}; font-size: 18px;">Gráfico de Presença:</h1>', unsafe_allow_html=True)

    st.markdown("""
    No gráfico ao lado, podemos observar que a porcentagem de alunos presentes é de **:green[78,7%]**, enquanto as faltas correspondem a **:red[21,3%]**. Esse gráfico de pizza nos dá uma visão clara da distribuição de presenças e faltas em todas as aulas registradas.
    """)


def texto_tab1_presente():

    st.markdown(""" 
    Podemos verificar outras métricas, como a taxa de presença por dia da semana ou a correlação entre o número de aulas e a taxa de presença. Essas análises podem fornecer insights mais profundos sobre os padrões de frequência e ajudar na identificação de dias com maior ou menor comparecimento.

    Por exemplo, poderíamos verificar se há uma diferença significativa na presença dos alunos em determinados dias da semana, o que poderia ajudar a otimizar a distribuição de aulas ou focar em intervenções específicas para reduzir as faltas.


    A análise de presença por dia da semana mostra uma variação interessante. A maior taxa de presença ocorre no **:orange[domingo]**, com **:green[85,7%]**, enquanto o **:orange[sábado]** tem a menor taxa de presença, com apenas **:green[50,6%]**. Durante os dias úteis, as taxas de presença variam de **:green[75,3%]** (sexta-feira) a **:green[81,5%]** (terça-feira). Isso sugere que, durante o final de semana, os alunos são menos assíduos, especialmente no sábado, o que pode indicar uma oportunidade de ajustar o planejamento de aulas ou atividades nesse dia para tentar aumentar o engajamento.

    """, unsafe_allow_html=True)


def texto_tab1_falta():
    st.markdown(""" 
        Assim como na presença, podemos observar que o **:orange[sábado]** tem a maior taxa de faltas, com **:red[49,4%]** de alunos ausentes. Isso contrasta fortemente com o **:orange[domingo]**, que tem a menor taxa de faltas, com **:red[14,3%]**. Durante a semana, as faltas variam entre **:red[18,5%]** na :orange[terça-feira] e **:red[24,7%]** na :orange[sexta-feira], o que pode sugerir que, no final da semana, a presença diminui consistentemente.
        """, unsafe_allow_html=True)


def texto_analise_distribuicao_idade():

    st.markdown("""
                ### Análise do Gráfico de Distribuição de Idade dos Alunos:
                            
                O gráfico mostra a **distribuição etária** dos alunos, concentrando a maioria das idades entre **10 e 19 anos**:

                1. **Faixa Etária Predominante**: O pico mais alto ocorre entre **10 e 14 anos**, com aproximadamente **1 mil alunos** nessa faixa. Essa é a faixa etária mais representada na amostra.

                2. **Queda na Frequência com a Idade**: A partir dos **15 anos**, a quantidade de alunos começa a diminuir, especialmente depois dos **20 anos**, sugerindo que a instituição ou programa pode ter um foco maior em adolescentes.

                3. **Alunos mais Velhos**: Embora haja poucos alunos acima dos **20 anos**, ainda existem alunos com até **24 anos**, com uma presença marginal até essa faixa etária.

                4. **Possível Foco da ONG**: Dado que a maior parte dos alunos está na faixa de 10 a 19 anos, isso indica que o público atendido pela ONG ou escola provavelmente está em estágios de educação básica e ensino médio.

                Esse gráfico sugere que a maior parte do impacto das atividades da ONG será sobre alunos adolescentes. Se há algum esforço para expandir o atendimento a grupos etários mais velhos, uma estratégia específica pode ser necessária para aumentar o engajamento de alunos acima dos 20 anos.
                """)


def texto_analise_correlacao_idade():

    st.markdown("""
        ### Análise de Correlação entre Idade e Presença/Faltas:

        A análise das porcentagens de presença e faltas por faixa etária revela padrões importantes no comportamento dos alunos em relação à frequência nas aulas:

        1. **Faixa Etária 0-10 anos**:
            - **Presença**: **94%**
            - **Faltas**: **6%**
            - **Interpretação**: Os alunos mais novos (0-10 anos) têm a maior taxa de presença. Isso pode indicar que, nessa faixa etária, há um maior controle dos responsáveis e uma maior adesão à rotina escolar.

        2. **Faixa Etária 11-15 anos**:
            - **Presença**: **89%**
            - **Faltas**: **11%**
            - **Interpretação**: A presença ainda é alta, embora um pouco menor do que a faixa anterior. Nessa idade, os alunos podem estar começando a ter mais autonomia, o que pode explicar o leve aumento nas faltas. O engajamento permanece elevado, mas já há sinais de diminuição.

        3. **Faixa Etária 16-20 anos**:
            - **Presença**: **86%**
            - **Faltas**: **14%**
            - **Interpretação**: A partir dessa faixa etária, a taxa de presença começa a cair de forma mais significativa. Esse grupo, geralmente no final do ensino médio, pode ter mais responsabilidades externas, como estágios ou preparação para vestibulares, o que pode impactar a frequência escolar. O aumento nas faltas pode também ser atribuído ao início de um comportamento mais independente.

        4. **Faixa Etária 21-25 anos**:
            - **Presença**: **76%**
            - **Faltas**: **24%**
            - **Interpretação**: A queda mais drástica na presença é observada nessa faixa etária. Alunos entre 21 e 25 anos costumam estar na transição para o mercado de trabalho ou cursando estudos superiores. Muitas vezes, conciliam estudos e trabalho, o que pode explicar o aumento significativo nas faltas. 

        5. **Faixa Etária 26-30 anos**:
            - **Presença**: **63%**
            - **Faltas**: **37%**
            - **Interpretação**: A taxa de presença volta a subir para 73,3%, o que pode indicar que os alunos dessa faixa etária que permanecem no sistema de ensino têm mais motivação e comprometimento, talvez buscando aperfeiçoamento profissional ou concluindo etapas educacionais que foram adiadas.

        6. **Faixa Etária 30+ anos**:
            - **Presença**: **00%**
            - **Faltas**: **100%**
            - **Interpretação**: A taxa de presença volta a cair nessa faixa etária, mas ainda se mantém relativamente alta. Alunos com mais de 30 anos provavelmente estão buscando educação continuada ou completando estudos interrompidos anteriormente. A taxa de faltas pode ser influenciada por obrigações pessoais e profissionais mais estabelecidas, como trabalho e família.

        **Considerações Gerais:**

        - **Tendência Geral**: A taxa de presença tende a diminuir à medida que a idade dos alunos aumenta, com a maior queda ocorrendo entre os alunos de **21 a 25 anos**. Isso pode refletir mudanças nas prioridades à medida que os alunos entram na vida adulta, com responsabilidades profissionais e pessoais competindo com a educação formal.
        
        - **Exceção dos 26-30 anos**: A presença na faixa de **26-30 anos** se recupera em comparação com a faixa de 21-25 anos. Essa recuperação pode indicar que alunos nessa faixa estão mais focados em completar sua formação ou em busca de desenvolvimento profissional.

        - **Implicações para Intervenção**: Programas que incentivem a retenção e o engajamento de alunos entre **16 e 25 anos** podem ser úteis para melhorar as taxas de presença. O apoio extra pode ser necessário para essa faixa, especialmente para alunos que estão entrando no mercado de trabalho ou lidando com múltiplas responsabilidades.

        Esta análise demonstra uma clara correlação entre o aumento da idade e a diminuição da presença nas aulas, com algumas nuances importantes em faixas específicas que podem ser alvos de intervenção para melhorar o engajamento.
    """)


def texto_distribuicao_sexo():
    st.markdown("""
            ### Distribuição por Gênero:

            - Existem diferenças na frequência de meninos e meninas nas aulas?

                """)


def texto_analise_genero():
    st.markdown("""

        ### Análise de Presença e Faltas por Gênero:

        **Presença:** 

        - **Masculino (0)**: **86,97%**
        - **Feminino (1)**: **88,25%**

        A taxa de presença entre alunos do gênero masculino e feminino é bastante próxima, com uma diferença mínima de aproximadamente **0,45 pontos percentuais**. Os alunos masculinos têm uma ligeiramente maior taxa de presença, porém, a diferença é pequena o suficiente para ser considerada insignificante em termos práticos.

        **Faltas:**

        - **Masculino (0)**: **13,03%**
        - **Feminino (1)**: **11,75%**

        Da mesma forma, as porcentagens de faltas são praticamente equivalentes. Os alunos do gênero feminino apresentam uma taxa de faltas ligeiramente maior (**13,03%** comparado a **11,75%** para os alunos masculinos), mas, assim como na presença, essa diferença é muito pequena para indicar um comportamento significativamente diferente entre os gêneros.

        **Conclusão:**

        As taxas de presença e faltas são muito similares entre os gêneros, indicando que **não há uma diferença relevante** no comportamento de presença e faltas entre alunos masculinos e femininos. Isso sugere que, no contexto dessa análise, o gênero dos alunos não é um fator determinante para variações na frequência escolar. Estratégias de engajamento ou intervenção não precisam ser diferenciadas com base no gênero, já que ambos apresentam padrões muito semelhantes.
        """)


def texto_distribuicao_raca_cor():
    st.markdown("""

        ### Distribuição por Raça e Cor:

        - Existe uma predominância de uma raça/cor específica?
        """)


def texto_analise_raca_cor():
    st.markdown("""
    ### Análise da Distribuição por Raça/Cor:

    A distribuição de alunos por raça/cor mostra algumas categorias com uma predominância clara e outras com presença muito pequena:

    1. **Branco (1007 alunos)**: É a categoria mais representada, sugerindo que a maioria dos alunos se identifica com essa classificação.
    
    2. **Pardo (858 alunos)**: A segunda categoria mais representada, com uma quantidade significativa de alunos.

    3. **Preto (249 alunos)**: Essa categoria que é a soma da "P" e "N" tem uma representação menor que as duas maiores categorias.

    5. **Outras Categorias (Amarelo, Indígina)**:
        - **Amarelo (16 alunos)** representa uma quantidade muito pequena de alunos.
        - **Indígina (1 aluno)** tem a menor representação possível, indicando apenas um aluno nessa categoria.

    **Considerações:**

    - **Concentração**: As categorias "Branco" e "Pardo" dominam a distribuição, representando a maioria dos alunos.
    - **Diversidade**: A presença de categorias menores como "Amarelo", "Indígina" e "Preto" indica uma diversidade na classificação racial, mas com uma concentração evidente em poucas categorias.
    """)


def texto_analise_raca_presenca():
    st.markdown("""

        ### Análise Breve da Correlação entre Raça/Cor e Presença/Faltas:

        A análise da **presença e faltas por raça/cor** revela algumas diferenças interessantes entre os grupos:

        1. **Amarelo (Presença: 100%, Faltas: 0%)**:
            - Este grupo tem uma das maiores taxas de presença, indicando um engajamento forte nas aulas.
            - A baixa taxa de faltas sugere que os alunos dessa categoria estão bastante comprometidos com suas atividades.

        2. **Branco (Presença: 88,38%, Faltas: 11,61%)**:
            - A categoria mais populosa tem uma taxa de presença moderadamente alta, mas as faltas, com **11,61%**, indicam que cerca de um quinto dos alunos dessa categoria estão ausentes regularmente.

        3. **Indígina (Presença: 100%, Faltas: 0%)**:
            - Embora haja apenas um aluno nessa categoria, esse aluno tem **100% de presença** e nenhuma falta, o que é um comportamento notável, mas deve ser interpretado com cautela devido ao tamanho da amostra (apenas um aluno).

        4. **Preto (Presença: 87,78%, Faltas: 12,22%)**:
            - A taxa de presença e faltas nesse grupo é quase idêntica à da categoria "B", o que sugere um comportamento semelhante de engajamento e absenteísmo.

        7. **Pardo (Presença: 86,24%, Faltas: 13,76%)**:
            - A presença nesse grupo é similar à das categorias "B" e "P", com uma taxa de faltas de **13%**. O comportamento de presença está dentro da média observada para os outros grupos.

        **Considerações Finais:**

        - **Grupo Indígina/Amarelo**: Apesar de ser uma amostra muito pequena, esses grupos se destacam por ter **100% de presença**. Isso pode ser um outlier devido ao tamanho reduzido da amostra.
        - **Grupo Branco**: Com a maior taxa de presença (**88%**), os alunos dessa categoria parecem ser os mais assíduos.
        - **Outros Grupos (Preto e Pardo)**: A maioria dos grupos tem taxas de presença na faixa de **87% a 86%** e faltas entre **13% e 12%**, o que indica um comportamento relativamente consistente entre esses alunos.
        """)


def texto_correlacao_pais_presenca():
    st.markdown("""
    ### Correlação entre Pais e Presença
    
    - Alunos que têm ambos os pais cadastrados faltam menos?
    - Isso pode revelar fatores sociais que impactam a presença.
    """)


def texto_analise_pais_presenca():
    st.markdown("""
        ### Análise da Correlação entre Presença de Pais e Presença/Faltas:

        1. **Alunos com Ambos os Pais**:
            - **Presença**: **73,85%**
            - **Faltas**: **26,15%**
            - **Interpretação**: Curiosamente, alunos que têm ambos os pais registrados apresentam a **menor taxa de presença** e a maior taxa de faltas (**26,15%**). Isso pode indicar que a presença de ambos os pais não necessariamente garante maior assiduidade nas aulas.

        2. **Alunos com Apenas Pai ou Mãe**:
            - **Presença**: **77,02%**
            - **Faltas**: **22,98%**
            - **Interpretação**: Alunos que têm apenas pai ou mãe registrados apresentam uma taxa de presença maior (**77,02%**), e a taxa de faltas diminui para cerca de **23%**. Essa categoria parece estar em uma situação intermediária entre alunos com ambos os pais e sem pais.

        3. **Alunos Sem Pais**:
            - **Presença**: **78,74%**
            - **Faltas**: **21,26%**
            - **Interpretação**: De maneira contraintuitiva, alunos sem pai nem mãe registrados têm a **maior taxa de presença** (**78,74%**) e a menor taxa de faltas. Isso sugere que, para esses alunos, a falta de pais registrados não resulta em uma menor presença escolar, e pode haver outros fatores sociais ou institucionais que motivam esses alunos a comparecerem mais frequentemente.

        **Conclusão:**

        - **Alunos com ambos os pais** têm a maior taxa de faltas, o que é um resultado inesperado. Intervenções para engajar mais esses alunos podem ser úteis.
        - **Alunos sem pais** se destacam por ter a maior taxa de presença, sugerindo que esses alunos podem receber suporte adicional ou possuem uma motivação interna maior para comparecer às aulas.
        - **Alunos com apenas um dos pais** estão em uma situação intermediária, com uma boa taxa de presença, indicando que a presença de pelo menos um dos pais pode ajudar no engajamento escolar.

        Esses resultados indicam que a presença de pais, por si só, não é o único fator determinante para a assiduidade, e outras variáveis podem estar influenciando o comportamento dos alunos.
        """)


def texto_cabecalho_analise_pais_presenca():
    st.markdown("""
    ### Análise da Correlação entre Presença de Pais/Mães e Presença/Faltas:
    """)


def texto_analise_pais_presenca_mae():

    st.markdown("""
        1. **Alunos com Pai**:
            - **Presença**: **85,76%**
            - **Faltas**: **14,24%**
            - **Interpretação**: Alunos que têm pai registrado apresentam uma alta taxa de presença (**85,76%**), sugerindo um maior comprometimento com as aulas em comparação com os alunos sem pai registrado.

        2. **Alunos sem Pai**:
            - **Presença**: **76,60%**
            - **Faltas**: **23,40%**
            - **Interpretação**: A ausência de pai registrado está associada a uma redução significativa na presença, com quase **23,4% de faltas**, indicando um possível fator de vulnerabilidade.

        3. **Alunos com Mãe**:
            - **Presença**: **76,57%**
            - **Faltas**: **23,43%**
            - **Interpretação**: A presença de mãe registrada não parece influenciar tanto quanto a de pai. Alunos com mãe têm uma taxa de presença ligeiramente inferior, similar à dos alunos sem pai.

        4. **Alunos sem Mãe**:
            - **Presença**: **84,84%**
            - **Faltas**: **15,16%**
            - **Interpretação**: Curiosamente, alunos sem mãe registrada apresentam uma presença mais alta (**84,84%**) do que aqueles com mãe registrada. Esse comportamento pode ser influenciado por outros fatores que exigem uma investigação mais profunda.

        **Conclusão:**

        - **Presença de Pai**: A presença de um pai registrado está associada a uma maior taxa de presença. A falta de pai registrado parece impactar negativamente a presença dos alunos, aumentando significativamente as faltas.
        - **Presença de Mãe**: A diferença entre ter ou não mãe registrada é menos clara, com alunos sem mãe apresentando uma taxa de presença até superior àqueles com mãe registrada.

        Esses dados sugerem que a **ausência de pai** tem um impacto mais significativo na frequência escolar.
                """)


def texto_titulo_disciplina_presenca():
    st.markdown("""
        ### Correlação entre a Disciplina e Presença
                
        - Quais disciplinas precisam de ajustes para melhorar a participação dos alunos e quais estão funcionando bem?        
        """)


def texto_analise_disciplina_presenca():
    st.markdown("""
        #### Análise da Presença e Faltas por Disciplina:

        1. **JORNADA DAS EMOÇÕES**:
            - **Presença**: **87,95%**
            - **Faltas**: **12,05%**
            - **Interpretação**: A disciplina com a maior taxa de presença, indicando um alto nível de engajamento dos alunos. Com uma taxa de faltas bem baixa, é uma das disciplinas com o melhor desempenho em termos de frequência.

        2. **GUARDIÕES DO SABER**:
            - **Presença**: **86,30%**
            - **Faltas**: **13,70%**
            - **Interpretação**: Também apresenta uma taxa de presença elevada, com uma baixa taxa de faltas, mostrando bom engajamento.

        3. **SUPERAÇÃO**:
            - **Presença**: **100%**
            - **Faltas**: **0%**
            - **Interpretação**: Notavelmente, todos os alunos registrados assistiram a essa disciplina, resultando em **100% de presença**. Isso pode indicar uma disciplina de curta duração ou um tema altamente motivacional.

        4. **MATEMÁTICA** e **PORTUGUÊS**:
            - **Presença**: **82,61%** e **82,89%**, respectivamente.
            - **Faltas**: **17,39%** e **17,11%**.
            - **Interpretação**: Essas disciplinas apresentam um desempenho sólido em termos de presença, com taxas de faltas moderadas, típicas para disciplinas centrais no currículo.

        5. **INGLÊS**:
            - **Presença**: **75,46%**
            - **Faltas**: **24,54%**
            - **Interpretação**: Uma das disciplinas com menor taxa de presença, sugerindo que os alunos podem ter mais dificuldades ou menos interesse em comparecer às aulas de inglês.

        6. **POLIVALENTE**:
            - **Presença**: **49,16%**
            - **Faltas**: **50,84%**
            - **Interpretação**: Essa disciplina tem uma das piores taxas de presença, com mais da metade dos alunos faltando. A alta taxa de faltas pode indicar falta de engajamento ou dificuldades associadas ao conteúdo.

        7. **TRILHANDO MEU CAMINHO**:
            - **Presença**: **27,74%**
            - **Faltas**: **72,26%**
            - **Interpretação**: Esta é a disciplina com a **pior taxa de presença**. Mais de 70% dos alunos estão ausentes, o que indica que há uma necessidade urgente de reavaliar a forma como essa disciplina está sendo conduzida ou as condições que estão afetando o comparecimento.

        8. **DISCIPLINAS MOTIVACIONAIS** (e.g., "EU NO COMANDO / SACODE A POEIRA / SUPERAÇÃO"):
            - **Presença**: **80,26%** a **100%**
            - **Interpretação**: As disciplinas com temas motivacionais têm uma presença geralmente alta, sugerindo que o conteúdo inspira os alunos a participar mais.

        **Conclusão:**

        - **Disciplinas de Engajamento Alto**: "Jornada das Emoções", "Guardião dos Saberes" e "Superação" estão no topo da lista, com taxas de presença acima de 85%, indicando que essas disciplinas são populares e bem recebidas pelos alunos.
        - **Áreas de Preocupação**: Disciplinas como "Polivalente" e "Trilhando Meu Caminho" têm taxas de faltas extremamente altas, exigindo uma revisão do conteúdo ou estratégias para aumentar a participação dos alunos.
        - **Disciplinas Centrais (Matemática, Português)**: Essas disciplinas têm boas taxas de presença, mas ainda podem se beneficiar de estratégias que reduzam as faltas e aumentem o engajamento.
                """)


def texto_modelo_avaliacao():
    st.markdown(""" 
        #### 🤖 Modelo Modelo RandomForestClassifier

        🔍 **:orange[RandomForestClassifier]:** <br><br>
            Este modelo tem como objetivo prever a ausência ou presença de alunos com base em um conjunto de dados histórico. <br><br>
            **Etapas do processo:** <br><br>
            1. **:orange[Balanceamento dos Dados]**: Utilizamos o **`RandomUnderSampler`** para equilibrar as classes no conjunto de treino (presença vs. ausência). Isso evita que o modelo favoreça a classe majoritária (presença), criando novos conjuntos de dados balanceados.<br><br>
            2. **:orange[RandomForest com Hiperparâmetros Otimizados]**: Um modelo de **`RandomForestClassifier`** foi utilizado para fazer as previsões. Os hiperparâmetros, que controlam aspectos como a profundidade das árvores e o número mínimo de amostras por folha, foram otimizados por meio de **`RandomizedSearchCV`**, que testa combinações aleatórias de parâmetros para encontrar a melhor configuração. <br><br>
            Essa abordagem combina técnicas de balanceamento e otimização de hiperparâmetros para melhorar a precisão das previsões de presença e ausência de alunos.
            """, unsafe_allow_html=True)