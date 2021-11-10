import streamlit as st
import pandas as pd
from PIL import Image
from functions import leitor, indicador, desempenho_manutencao, desempenho_instalação_rh
from functions import desempenho_almoxarifado, desempenho_plan_proj, desempenho_seg_trabalho
import streamlit.components.v1 as components
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# This code is different for each deployed app.
CURRENT_THEME = "light"
IS_DARK_THEME = False
EXPANDER_TEXT = """
    This is Streamlit's default *Light* theme. It should be enabled by default 🎈
    If not, you can enable it in the app menu (☰ -> Settings -> Theme).
    """


logo_C = Image.open("./LogoC.png")
logo_Capa = Image.open("./Logo_C_capa.png")
header = Image.open("./header.png")
logo_Cinza = Image.open("./Logo_Site.png")
fluxograma = Image.open("./Fluxograma.jpg")
contigencia = open("planodecontingencia.pdf")
organograma = open("organograma.pdf")
politica_de_qualidade = open("politica_de_qualidade.pdf")
diretrizes = open("diretrizes.pdf")
fluxo_de_interacao = open("fluxo_de_interacao.pdf")


# Barra lateral
st.sidebar.image(logo_C, caption=None, width=75)
st.sidebar.title('**Constel Engenharia Elétrica**')

option = st.sidebar.selectbox('Selecione a página desejada', ["Início", "Indicadores", "Desempenho", "Documentos", "Sobre"])

if option == "Início":
    # Página inicial
    st.image(header, caption=None, width=800)
    st.header('**Bem vindo!**')
    st.markdown('Nesta plataforma você encontrará os indicadores dos processos e desempenho dos processos.')
    st.markdown('É possível visualizar também documentos relacionados a Gestão da Qualidade.')
    st.markdown('Clique na aba lateral para navegar pelo site')

if option == 'Documentos':
    st.markdown("<h3 style='text-align: center; color: black;'>Documentos</h3>", unsafe_allow_html=True)


    st.markdown("<h6 style='text-align: left; color: black;'>Diretrizes</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    A Constel é um barco, em que todos os colaboradores devem remar na mesma direção. Bem como, a Missão, Visão e Valores compõem um conjunto de diretrizes fundamentais que norteiam a empresa. Além disso, são de extrema importância para orientar o planejamento estratégico e construir uma identidade organizacional, portanto leia atentamente e dissemine seu conteúdo a todos.</p>", unsafe_allow_html=True)
    with open('diretrizes.pdf', 'rb') as f:
        st.download_button('Baixar', f, file_name='diretrizes.pdf')
    st.write('')

    st.markdown("<h6 style='text-align: left; color: black;'>Política de Qualidade</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    A empresa possuí Política de Qualidade? O que é melhoria contínua? Sabe me dar exemplo? O que são profissionais capacitados e comprometidos? Perguntas que podem ser feitas, e devem ser respondidas com base na Política de Qualidade que é definida a parti de escopo, visando abranger todos os serviços prestados ou que serão prestados pela Constel, então estude, interprete, dissemine e discuta o seu conteúdo com todos da empresa, mas principalmente com os seus subordinados..</p>", unsafe_allow_html=True)
    with open('politica_de_qualidade.pdf', 'rb') as f:
        st.download_button('Baixar', f, file_name='politica_de_qualidade.pdf')
    st.write('')

    st.markdown("<h6 style='text-align: left; color: black;'>Organograma</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    Quem é seu gestor? Para quem você responde? Onde está escrito pra quem você responde? Essas são algumas das perguntas que podem serem feitas a fim de verificar o conhecimento dos colaboradores sobre o Organograma. Após algumas atualizações a versão definitiva está disponível a todos, por isso consulte-o e veja de forma gráfica a estrutura organizacional da empresa e a hierarquia a ser respeitada. </p>", unsafe_allow_html=True)
    with open('organograma.pdf', 'rb') as f:
        st.download_button('Baixar', f, file_name='organograma.pdf')
    st.write('')


    st.markdown("<h6 style='text-align: left; color: black;'>Fluxograma de Interação de Processos</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    Onde seu processo está inserido no SGQ? É processo de apoio? Processo operacional? O gestor deve saber responder a estas perguntas, por isso é fundamental o entendimento sobre a última versão do Fluxo de Interação dos Processos que visa representar de maneira gráfica o fluxo ideal para a estrutura organizacional da empresa. </p>", unsafe_allow_html=True)
    with open('fluxo_de_interacao.pdf', 'rb') as f:
        st.download_button('Baixar', f, file_name='fluxo_de_interacao.pdf')
    st.write('')


    st.markdown("<h6 style='text-align: left; color: black;'>Fluxograma de Entradas e Saídas</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    Como funciona o seu processo? Quais são as entradas? Quais os recursos necessários? Quais as Saídas? Quais entradas vem de outro processo? As suas saídas são entradas de outros processos? Muitas perguntas que podem ser feitas, mas a resposta é a mesma. Com base no fluxo de interação dos processos, foi gerado a Matriz de Entradas e Saídas a qual contém todas as entradas, recursos e saídas do processo. Você como gestor deve saber, além de manter organizado e ter EVIDÊNCIAS de tudo (planilhas, documentos, sistemas etc.), por isso entender o fluxo entre os processos é fundamental. Para facilitar, pode consultar o grande fluxograma desenvolvido pelo Rafael Andreatta, com todos os processos suas respectivas entradas e saídas. </p>", unsafe_allow_html=True)
    with open('Fluxograma.jpg', 'rb') as f:
        st.download_button('Baixar', f, file_name='Fluxograma.jpg')
    st.write('')


    st.markdown("<h6 style='text-align: left; color: black;'>Plano de Contingência</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    O que fazer em caso de acidente? Acabar a luz? Acabar a água? Greve do transporte coletivo? Acidente de trabalho? Incêndio? Falta de materiais? Problemas com o carro? Para responder a essas perguntas, verificar todos os itens presentes no plano de contingência, dando ênfase aos que são inerentes ao processo e as pessoas envolvidas, disponibilizar cópia impressa no setor e disseminar seu conteúdo a todos (escritório e campo). </p>", unsafe_allow_html=True)
    with open('planodecontingencia.pdf', 'rb') as f:
        st.download_button('Baixar', f, file_name='planodecontingencia.pdf')
    st.write('')


    st.markdown("<h6 style='text-align: left; color: black;'>Controle de Documentos</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    Qual versão está o documento utilizado pelo processo? Quando foi feita última revisão? E propriedade da empresa ou do cliente? Todos os documentos e registros que forem criados ou alterados devem ser comunicados ao responsável pela Gestão da Qualidade a fim de verificar se possuem as informações básicas, como: Processo, data de elaboração, número e data da última revisão. Além disso, TUDO que é criado e utilizado pelo processo deve ser inserido no Controle de Documentos, essa planilha possui informações importantes que visa facilitar a busca de todos os colaboradores a documentos e registros existentes. </p>", unsafe_allow_html=True)
    st.write('')


    st.markdown("<h6 style='text-align: left; color: black;'>Análise de Risco da Mudança Solicitada</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    Você precisou realizar alguma mudança no processo? Teve algo que mudaram e teve impacto ao SGQ? Quando houver necessidade de mudança no seu processo, o que você faz? Para toda mudança no processo, deve-se analisar quais os riscos associados e o impacto que causará ao Sistema de Gestão da Qualidade (quer realocar a mesa dentro do seu setor – OK, porém se quiser realizar uma melhoria/ alteração que vá influenciar nos demais processos é necessário realizar essa análise). Para isso, deve-se utilizar o documento Análise de Risco da Mudança Solicitada em conjunto com um cronograma de execução, para que as etapas da mudança sejam implementadas. </p>", unsafe_allow_html=True)
    st.write('')


    st.markdown("<h6 style='text-align: left; color: black;'>Análise SWOT com Riscos</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    Qual o risco do seu processo para o negócio? Qual é o grau desse risco? Quais as ações que visam mitigá-lo? O plano de ação é para 1 ou 2 anos? A matriz SWOT, ou FOFA é uma ferramenta de planejamento estratégico, a qual contém os pontos fortes e fracos, relacionados ao ambiente interno (Forças e Fraquezas) e externo da empresa (Oportunidades e Ameaças). Assim como os indicadores, as ações presentes no planejamento estratégico devem ser analisadas periodicamente (semestral), fazendo uma análise completa sobre tudo o que foi feito durante o período e quais serão as próximas ações. A planilha está disponível de forma online a fim de facilitar a edição simultânea por parte dos gestores. TODOS que fazem parte do seu processo devem ter conhecimento do(s) risco(s) que pode(m) impactar de forma positiva ou negativa o planejamento estratégico da empresa. </p>", unsafe_allow_html=True)
    st.write('')



if option == 'Desempenho':
    worksheet = "Desempenho do Processo 2021"
    choice = st.selectbox('Escolha o processo: ',('Selecione', 'Instalação','Almoxarifado','Planejamento',
    'Seg. Trabalho','Projetos', 'Manutenção', 'RH'))
    # Desempenho do setor de Manutenção
    if choice == 'Manutenção':
        sheet = choice
        df = leitor(worksheet, sheet)
        # Avaliação primeiro trimestre
        check1t = st.checkbox('1º Trimestre/2021')
        if check1t == 1:
            st.markdown('**'+list(df.iloc[42])[0]+'**')
            st.write(list(df.iloc[43])[0])
        # Avaliação segundo trimestre
        check2t = st.checkbox('2º Trimestre/2021')
        if check2t == 1:
            st.markdown('**'+list(df.iloc[44])[0]+'**')
            st.write(list(df.iloc[45])[0])
        # Avaliação terceiro trimestre
        check3t = st.checkbox('3º Trimestre/2021')
        if check3t == 1:
            st.markdown('**'+list(df.iloc[46])[0]+'**')
            st.write(list(df.iloc[47])[0])
        # Avaliação quarto trimestre
        check4t = st.checkbox('4º Trimestre/2021')
        if check4t == 1:
            st.markdown('**'+list(df.iloc[48])[0]+'**')
            st.write(list(df.iloc[49])[0])
        # Desempenho
        st.markdown('**Tabela do desempenho por mês do ano de 2021**')
        desempenho = desempenho_manutencao(df)
        st.table(desempenho)

    if choice == 'Instalação':
        sheet = choice
        df = leitor(worksheet, sheet)
        st.markdown('**Avaliações de desempenho**')
        # Avaliação primeiro trimestre
        check1t = st.checkbox('1º Trimestre/2021')
        if check1t == 1:
            st.markdown('**'+list(df.iloc[29])[0]+'**')
            st.write(list(df.iloc[30])[0])
        # Avaliação segundo trimestre
        check2t = st.checkbox('2º Trimestre/2021')
        if check2t == 1:
            st.markdown('**'+list(df.iloc[31])[0]+'**')
            st.write(list(df.iloc[32])[0])
        # Avaliação terceiro trimestre
        check3t = st.checkbox('3º Trimestre/2021')
        if check3t == 1:
            st.markdown('**'+list(df.iloc[33])[0]+'**')
            st.write(list(df.iloc[34])[0])
        # Avaliação quarto trimestre
        check4t = st.checkbox('4º Trimestre/2021')
        if check4t == 1:
            st.markdown('**'+list(df.iloc[35])[0]+'**')
            st.write(list(df.iloc[36])[0])
        # Desempenho
        st.markdown('**Tabela do desempenho por mês do ano de 2021**')
        desempenho = desempenho_instalação_rh(df)
        st.table(desempenho)

    if choice == 'Almoxarifado':
        sheet = choice
        df = leitor(worksheet, sheet)
                # Avaliação primeiro trimestre
        check1t = st.checkbox('1º Trimestre/2021')
        if check1t == 1:
            st.markdown('**'+list(df.iloc[95])[0]+'**')
            st.write(list(df.iloc[96])[0])
        # Avaliação segundo trimestre
        check2t = st.checkbox('2º Trimestre/2021')
        if check2t == 1:
            st.markdown('**'+list(df.iloc[97])[0]+'**')
            st.write(list(df.iloc[98])[0])
        # Avaliação terceiro trimestre
        check3t = st.checkbox('3º Trimestre/2021')
        if check3t == 1:
            st.markdown('**'+list(df.iloc[99])[0]+'**')
            st.write(list(df.iloc[100])[0])
        # Avaliação quarto trimestre
        check4t = st.checkbox('4º Trimestre/2021')
        if check4t == 1:
            st.markdown('**'+list(df.iloc[101])[0]+'**')
            st.write(list(df.iloc[102])[0])
        # Desempenho
        st.markdown('**Tabela do desempenho por mês do ano de 2021**')
        desempenho = desempenho_almoxarifado(df)
        # Filtra o df pelo mês e retorna df com base no intervalo mensal
        month = st.selectbox('Selecione o mês:', ('Selecione', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
        'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'))
        if month == 'Janeiro':
            st.table(desempenho[0:6])
        if month == 'Fevereiro':
            st.table(desempenho[6:12])
        if month == 'Março':
            st.table(desempenho[12:18])
        if month == 'Abril':
            st.table(desempenho[18:24])
        if month == 'Maio':
            st.table(desempenho[24:30])
        if month == 'Junho':
            st.table(desempenho[30:36])
        if month == 'Julho':
            st.table(desempenho[36:42])
        if month == 'Agosto':
            st.table(desempenho[42:48])
        if month == 'Setembro':
            st.table(desempenho[48:54])
        if month == 'Outubro':
            st.table(desempenho[54:60])
        if month == 'Novembro':
            st.table(desempenho[60:66])
        if month == 'Dezembro':
            st.table(desempenho[66:72])

    if choice == 'Planejamento':
        sheet = choice
        df = leitor(worksheet, sheet)
                # Avaliação primeiro trimestre
        check1t = st.checkbox('1º Trimestre/2021')
        if check1t == 1:
            st.markdown('**'+list(df.iloc[38])[0]+'**')
            st.write(list(df.iloc[39])[0])
        # Avaliação segundo trimestre
        check2t = st.checkbox('2º Trimestre/2021')
        if check2t == 1:
            st.markdown('**'+list(df.iloc[40])[0]+'**')
            st.write(list(df.iloc[41])[0])
        # Avaliação terceiro trimestre
        check3t = st.checkbox('3º Trimestre/2021')
        if check3t == 1:
            st.markdown('**'+list(df.iloc[42])[0]+'**')
            st.write(list(df.iloc[43])[0])
        # Avaliação quarto trimestre
        check4t = st.checkbox('4º Trimestre/2021')
        if check4t == 1:
            st.markdown('**'+list(df.iloc[44])[0]+'**')
            st.write(list(df.iloc[45])[0])
        # Desempenho
        st.markdown('**Tabela do desempenho por mês do ano de 2021**')
        desempenho = desempenho_plan_proj(df)
        st.table(desempenho)

    if choice == 'Projetos':
        sheet = choice
        df = leitor(worksheet, sheet)
                # Avaliação primeiro trimestre
        check1t = st.checkbox('1º Trimestre/2021')
        if check1t == 1:
            st.markdown('**'+list(df.iloc[34])[0]+'**')
            st.write(list(df.iloc[35])[0])
        # Avaliação segundo trimestre
        check2t = st.checkbox('2º Trimestre/2021')
        if check2t == 1:
            st.markdown('**'+list(df.iloc[36])[0]+'**')
            st.write(list(df.iloc[37])[0])
        # Avaliação terceiro trimestre
        check3t = st.checkbox('3º Trimestre/2021')
        if check3t == 1:
            st.markdown('**'+list(df.iloc[38])[0]+'**')
            st.write(list(df.iloc[39])[0])
        # Avaliação quarto trimestre
        check4t = st.checkbox('4º Trimestre/2021')
        if check4t == 1:
            st.markdown('**'+list(df.iloc[40])[0]+'**')
            st.write(list(df.iloc[41])[0])
        # Desempenho
        st.markdown('**Tabela do desempenho por mês do ano de 2021**')
        desempenho = desempenho_plan_proj(df)
        st.table(desempenho)

    if choice == 'Seg. Trabalho':
        sheet = choice
        df = leitor(worksheet, sheet)
                # Avaliação primeiro trimestre
        check1t = st.checkbox('1º Trimestre/2021')
        if check1t == 1:
            st.markdown('**'+list(df.iloc[17])[0]+'**')
            st.write(list(df.iloc[18])[0])
        # Avaliação segundo trimestre
        check2t = st.checkbox('2º Trimestre/2021')
        if check2t == 1:
            st.markdown('**'+list(df.iloc[19])[0]+'**')
            st.write(list(df.iloc[20])[0])
        # Avaliação terceiro trimestre
        check3t = st.checkbox('3º Trimestre/2021')
        if check3t == 1:
            st.markdown('**'+list(df.iloc[21])[0]+'**')
            st.write(list(df.iloc[22])[0])
        # Avaliação quarto trimestre
        check4t = st.checkbox('4º Trimestre/2021')
        if check4t == 1:
            st.markdown('**'+list(df.iloc[23])[0]+'**')
            st.write(list(df.iloc[24])[0])
        # Desempenho
        st.markdown('**Tabela do desempenho por mês do ano de 2021**')
        desempenho = desempenho_seg_trabalho(df)
        st.table(desempenho)
    
    if choice == 'RH':
        sheet = choice
        df = leitor(worksheet, sheet)
                # Avaliação primeiro trimestre
        check1t = st.checkbox('1º Trimestre/2021')
        if check1t == 1:
            st.markdown('**'+list(df.iloc[29])[0]+'**')
            st.write(list(df.iloc[30])[0])
        # Avaliação segundo trimestre
        check2t = st.checkbox('2º Trimestre/2021')
        if check2t == 1:
            st.markdown('**'+list(df.iloc[31])[0]+'**')
            st.write(list(df.iloc[32])[0])
        # Avaliação terceiro trimestre
        check3t = st.checkbox('3º Trimestre/2021')
        if check3t == 1:
            st.markdown('**'+list(df.iloc[33])[0]+'**')
            st.write(list(df.iloc[34])[0])
        # Avaliação quarto trimestre
        check4t = st.checkbox('4º Trimestre/2021')
        if check4t == 1:
            st.markdown('**'+list(df.iloc[35])[0]+'**')
            st.write(list(df.iloc[36])[0])
        # Desempenho
        st.markdown('**Tabela do desempenho por mês do ano de 2021**')
        desempenho = desempenho_instalação_rh(df)
        st.table(desempenho)


if option == 'Indicadores':
    st.markdown('Nesta aba é possível visualizar os indicadores dos processos da empresa.')
    choice = st.selectbox('Escolha o setor: ',('Selecione', 'Instalação', 'Manutenção','Planejamento','Comercial','Controle de Qualidade', 
    'Seg. do Trabalho', 'Fechamento', 'Projetos', 'RH'))
    # Indicador geral da empresa, mostrando os processos que puxam pra baixo, se for preciso definir pesos para os processos
    worksheet = "Plano de Objetivos e Metas 2021 e Controle de Documentos"
    sheet = choice
    if choice == 'Instalação':
        st.markdown('**Indicador:** Instalação')
        df = leitor(worksheet, sheet)
        ind = indicador(df)
        st.table(ind)
        
    if choice == 'Manutenção':
        st.markdown('**Indicador:** Manutenção')
        df = leitor(worksheet, sheet)
        ind = indicador(df)
        st.table(ind)

    if choice == 'Planejamento':
        st.markdown('**Indicador:** Planejamento')
        df = leitor(worksheet, sheet)
        ind = indicador(df)
        st.table(ind)

    if choice == 'Comercial':
        st.markdown('**Indicador:** Comercial')
        df = leitor(worksheet, sheet)
        ind = indicador(df)
        st.table(ind)

    if choice == 'Qualidade':
        st.markdown('**Indicador:** Qualidade')
        df = leitor(worksheet, sheet)
        ind = indicador(df)
        st.table(ind)

    if choice == 'Seg. do Trabalho':
        st.markdown('**Indicador:** Seg. do Trabalho')
        df = leitor(worksheet, sheet)
        ind = indicador(df)
        st.table(ind)

    if choice == 'Fechamento':
        st.markdown('**Indicador:** Fechamento')
        df = leitor(worksheet, sheet)
        ind = indicador(df)
        st.table(ind)

    if choice == 'Projetos':
        st.markdown('**Indicador:** Projetos')
        df = leitor(worksheet, sheet)
        ind = indicador(df)
        st.table(ind)

    if choice == 'RH':
        st.markdown('**Indicador:** RH')
        df = leitor(worksheet, sheet)
        ind = indicador(df)
        st.table(ind)

if option == "Sobre":
    st.markdown('**Autor:** Leonardo de Oliveira Melo')
    st.markdown('**Formação:** Graduando em Eng. Cartógrafica e de Agrimensura')
    st.markdown('**Instituição:** Universidade Federal do Paraná')
    st.markdown('**Linkedin:** https://www.linkedin.com/in/leonardo-oliveira-melo-287593164/')
    st.markdown('**Projeto:** Desenvolver plataforma com os indicadores da Constel')
    st.markdown('**Status:** Em desenvolvimento.')
    st.image(logo_Capa, caption=None, width=150)
