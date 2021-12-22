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
# Abre arquivos de imagem
logo_C = Image.open("./thumbnail/LogoC.png")
logo_Capa = Image.open("./thumbnail/Logo_C_capa.png")
header = Image.open("./thumbnail/header.png")
header_indicadores = Image.open("./thumbnail/header_indicadores.png")
header_desempenho = Image.open("./thumbnail/header_desempenho.png")
logo_Cinza = Image.open("./thumbnail/Logo_Site.png")


# Barra lateral
st.sidebar.image(logo_C, caption=None, width=75)
st.sidebar.title('**Constel Engenharia Elétrica**')
option = st.sidebar.selectbox('Selecione a página desejada', ["Início", "Indicadores", "Desempenho", "Documentos", "Sobre"])

if option == "Início":
    # Página inicial
    st.image(header, caption=None, width=650)
    st.markdown("<h2 style='text-align: center; color: black;'>Bem vindo!</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: black;'>Nesta plataforma você encontrará os indicadores dos processos, desempenho dos processos e também documentos relacionados a Gestão da Qualidade.</p>", unsafe_allow_html=True)
    st.markdown('       ')
    st.markdown("<p style='text-align: center; color: black;'>👈 Clique na aba lateral para navegar pelo site.</p>", unsafe_allow_html=True)
    st.markdown('       ')
    st.markdown("<p style='text-align: center; color: black;'>Abaixo é possível visualizar as áreas de atuação da empresa: </p>", unsafe_allow_html=True)
    acting = st.selectbox('Selecione a área de atuação para ver o mapa: ', ('Instalação de Sites', 'Construção de prumadas', 'Instalação de internet'))
    if acting == 'Instalação de Sites':
        components.iframe("https://www.google.com/maps/d/embed?mid=1r6xzmsAeiSD3cniV-oXD_MWHGMPyYVZ8&ehbc=2E312F", width=700, height=380)
    if acting == 'Construção de prumadas':
        components.iframe("https://www.google.com/maps/d/embed?mid=18q5jUlCf0BM9RQ-gygQDPUcvLq_OcwxU&ehbc=2E312F", width=700, height=380)

if option == 'Indicadores':
    st.image(header_indicadores, caption=None, width=650)
    year = st.selectbox('Selecione o ano desejado: ',('Selecione','2021','2022'))
    if year != "Selecione":
        if year == '2021':
            st.markdown("<h6 style='text-align: center; color: black;'>⚠️ Observação!</h6>", unsafe_allow_html=True)
            st.markdown("")
            st.markdown("<p style='text-align: justify; color: black;'>Em 2021 ocorreu uma reestruturação da empresa, com o encerramento do contrato com a Copel Telecom.</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: justify; color: black;'>Foram então remodelados os indicadores atendendo as novas demandas da empresa.</p>", unsafe_allow_html=True)
            st.markdown("")
            period = st.selectbox('Selecione o período para visualizar: ',('Selecione','1º ao 3º trimestre','4º trimestre'))
                        
            if period != 'Selecione':
                
                if period == '1º ao 3º trimestre':
                    worksheet = "Plano de Objetivos e Metas 2021"
                    choice = st.selectbox('Selecione o processo: ',('Selecione', 'Instalação', 'Manutenção','Planejamento','Comercial','Controle de Qualidade', 
                    'Seg. do Trabalho', 'Fechamento', 'Projetos', 'RH'))
                    sheet = choice

                if period == '4º trimestre':
                    st.markdown("<p style='text-align: center; color: black;'> Em definição...</p>", unsafe_allow_html=True)
                    worksheet = "Plano de Objetivos e Metas 2021" #inserir planilha readequação
                    choice = 'Selecione'
                    # choice = st.selectbox('Selecione o processo: ',('Selecione',''))
                    sheet = choice
                
                if choice == 'Instalação':
                    sheet = choice
                    df = leitor(worksheet, sheet)
                    # Avaliação primeiro trimestre
                    check1t = st.checkbox('1º Trimestre/2021')
                    if check1t == 1:
                        st.markdown('**'+list(df.iloc[24])[0]+'**')
                        st.write(list(df.iloc[25])[0])
                    # Avaliação segundo trimestre
                    check2t = st.checkbox('2º Trimestre/2021')
                    if check2t == 1:
                        st.markdown('**'+list(df.iloc[26])[0]+'**')
                        st.write(list(df.iloc[27])[0])
                    # Avaliação terceiro trimestre
                    check3t = st.checkbox('3º Trimestre/2021')
                    if check3t == 1:
                        st.markdown('**'+list(df.iloc[28])[0]+'**')
                        st.write(list(df.iloc[29])[0])
                    st.markdown('**Indicador:** Instalação')
                    ind = indicador(df)
                    st.table(ind)
                    
                if choice == 'Manutenção':
                    sheet = choice
                    df = leitor(worksheet, sheet)
                    # Avaliação primeiro trimestre
                    check1t = st.checkbox('1º Trimestre/2021')
                    if check1t == 1:
                        st.markdown('**'+list(df.iloc[19])[0]+'**')
                        st.write(list(df.iloc[20])[0])
                    # Avaliação segundo trimestre
                    check2t = st.checkbox('2º Trimestre/2021')
                    if check2t == 1:
                        st.markdown('**'+list(df.iloc[21])[0]+'**')
                        st.write(list(df.iloc[22])[0])
                    # Avaliação terceiro trimestre
                    check3t = st.checkbox('3º Trimestre/2021')
                    if check3t == 1:
                        st.markdown('**'+list(df.iloc[23])[0]+'**')
                        st.write(list(df.iloc[24])[0])
                    st.markdown('**Indicador:** Manutenção')
                    ind = indicador(df)
                    st.table(ind)

                if choice == 'Planejamento':
                    sheet = choice
                    df = leitor(worksheet, sheet)
                    # Avaliação primeiro trimestre
                    check1t = st.checkbox('1º Trimestre/2021')
                    if check1t == 1:
                        st.markdown('**'+list(df.iloc[24])[0]+'**')
                        st.write(list(df.iloc[25])[0])
                    # Avaliação segundo trimestre
                    check2t = st.checkbox('2º Trimestre/2021')
                    if check2t == 1:
                        st.markdown('**'+list(df.iloc[26])[0]+'**')
                        st.write(list(df.iloc[27])[0])
                    # Avaliação terceiro trimestre
                    check3t = st.checkbox('3º Trimestre/2021')
                    if check3t == 1:
                        st.markdown('**'+list(df.iloc[28])[0]+'**')
                        st.write(list(df.iloc[29])[0])
                    st.markdown('**Indicador:** Planejamento')
                    ind = indicador(df)
                    st.table(ind)

                if choice == 'Comercial':
                    sheet = choice
                    df = leitor(worksheet, sheet)
                    # Avaliação primeiro trimestre
                    check1t = st.checkbox('1º Trimestre/2021')
                    if check1t == 1:
                        st.markdown('**'+list(df.iloc[24])[0]+'**')
                        st.write(list(df.iloc[25])[0])
                    # Avaliação segundo trimestre
                    check2t = st.checkbox('2º Trimestre/2021')
                    if check2t == 1:
                        st.markdown('**'+list(df.iloc[26])[0]+'**')
                        st.write(list(df.iloc[27])[0])
                    # Avaliação terceiro trimestre
                    check3t = st.checkbox('3º Trimestre/2021')
                    if check3t == 1:
                        st.markdown('**'+list(df.iloc[28])[0]+'**')
                        st.write(list(df.iloc[29])[0])
                    st.markdown('**Indicador:** Comercial')
                    ind = indicador(df)
                    st.table(ind)

                if choice == 'Controle de Qualidade':
                    sheet = choice
                    df = leitor(worksheet, sheet)
                    # Avaliação primeiro trimestre
                    check1t = st.checkbox('1º Trimestre/2021')
                    if check1t == 1:
                        st.markdown('**'+list(df.iloc[21])[0]+'**')
                        st.write(list(df.iloc[22])[0])
                    # Avaliação segundo trimestre
                    check2t = st.checkbox('2º Trimestre/2021')
                    if check2t == 1:
                        st.markdown('**'+list(df.iloc[23])[0]+'**')
                        st.write(list(df.iloc[24])[0])
                    # Avaliação terceiro trimestre
                    check3t = st.checkbox('3º Trimestre/2021')
                    if check3t == 1:
                        st.markdown('**'+list(df.iloc[25])[0]+'**')
                        st.write(list(df.iloc[26])[0])
                    st.markdown('**Indicador:** Qualidade')
                    ind = indicador(df)
                    st.table(ind)

                if choice == 'Seg. do Trabalho':
                    sheet = choice
                    df = leitor(worksheet, sheet)
                    # Avaliação primeiro trimestre
                    check1t = st.checkbox('1º Trimestre/2021')
                    if check1t == 1:
                        st.markdown('**'+list(df.iloc[24])[0]+'**')
                        st.write(list(df.iloc[25])[0])
                    # Avaliação segundo trimestre
                    check2t = st.checkbox('2º Trimestre/2021')
                    if check2t == 1:
                        st.markdown('**'+list(df.iloc[26])[0]+'**')
                        st.write(list(df.iloc[27])[0])
                    # Avaliação terceiro trimestre
                    check3t = st.checkbox('3º Trimestre/2021')
                    if check3t == 1:
                        st.markdown('**'+list(df.iloc[28])[0]+'**')
                        st.write(list(df.iloc[29])[0])
                    st.markdown('**Indicador:** Seg. do Trabalho')
                    ind = indicador(df)
                    st.table(ind)

                if choice == 'Fechamento':
                    sheet = choice
                    df = leitor(worksheet, sheet)
                    # Avaliação primeiro trimestre
                    check1t = st.checkbox('1º Trimestre/2021')
                    if check1t == 1:
                        st.markdown('**'+list(df.iloc[24])[0]+'**')
                        st.write(list(df.iloc[25])[0])
                    # Avaliação segundo trimestre
                    check2t = st.checkbox('2º Trimestre/2021')
                    if check2t == 1:
                        st.markdown('**'+list(df.iloc[26])[0]+'**')
                        st.write(list(df.iloc[27])[0])
                    # Avaliação terceiro trimestre
                    check3t = st.checkbox('3º Trimestre/2021')
                    if check3t == 1:
                        st.markdown('**'+list(df.iloc[28])[0]+'**')
                        st.write(list(df.iloc[29])[0])
                    st.markdown('**Indicador:** Fechamento')
                    ind = indicador(df)
                    st.table(ind)

                if choice == 'Projetos':
                    sheet = choice
                    df = leitor(worksheet, sheet)
                    # Avaliação primeiro trimestre
                    check1t = st.checkbox('1º Trimestre/2021')
                    if check1t == 1:
                        st.markdown('**'+list(df.iloc[24])[0]+'**')
                        st.write(list(df.iloc[25])[0])
                    # Avaliação segundo trimestre
                    check2t = st.checkbox('2º Trimestre/2021')
                    if check2t == 1:
                        st.markdown('**'+list(df.iloc[26])[0]+'**')
                        st.write(list(df.iloc[27])[0])
                    # Avaliação terceiro trimestre
                    check3t = st.checkbox('3º Trimestre/2021')
                    if check3t == 1:
                        st.markdown('**'+list(df.iloc[28])[0]+'**')
                        st.write(list(df.iloc[29])[0])
                    st.markdown('**Indicador:** Projetos')
                    ind = indicador(df)
                    st.table(ind)

                if choice == 'RH':
                    sheet = choice
                    df = leitor(worksheet, sheet)
                    # Avaliação primeiro trimestre
                    check1t = st.checkbox('1º Trimestre/2021')
                    if check1t == 1:
                        st.markdown('**'+list(df.iloc[24])[0]+'**')
                        st.write(list(df.iloc[25])[0])
                    # Avaliação segundo trimestre
                    check2t = st.checkbox('2º Trimestre/2021')
                    if check2t == 1:
                        st.markdown('**'+list(df.iloc[26])[0]+'**')
                        st.write(list(df.iloc[27])[0])
                    # Avaliação terceiro trimestre
                    check3t = st.checkbox('3º Trimestre/2021')
                    if check3t == 1:
                        st.markdown('**'+list(df.iloc[28])[0]+'**')
                        st.write(list(df.iloc[29])[0])
                    st.markdown('**Indicador:** RH')
                    ind = indicador(df)
                    st.table(ind)

        if year == '2022':
            st.markdown('Aguardando a definição.')

if option == 'Desempenho':
    st.image(header_desempenho, caption=None, width=650)
    year = st.selectbox('Selecione o ano desejado: ',('Selecione','2021','2022'))
    if year != "Selecione":
        if year == '2021':
            st.markdown("<h6 style='text-align: center; color: black;'>⚠️ Observação!</h6>", unsafe_allow_html=True)
            st.markdown("")
            st.markdown("<p style='text-align: justify; color: black;'>Em 2021 ocorreu uma reestruturação da empresa, com o encerramento do contrato com a Copel Telecom.</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: justify; color: black;'>Os indicadores de desempenho sofreram alterações, atendendo as novas demandas da empresa.</p>", unsafe_allow_html=True)
            st.markdown("")
            period = st.selectbox('Selecione o período para visualizar: ',('Selecione','1º ao 3º trimestre','4º trimestre'))
                        
            if period != 'Selecione':
                
                if period == '1º ao 3º trimestre':
                    worksheet = "Desempenho do Processo 2021"
                    choice = st.selectbox('Escolha o processo: ',('Selecione', 'Instalação','Almoxarifado','Planejamento',
                    'Seg. Trabalho','Projetos', 'Manutenção', 'RH'))
                    sheet = choice

                if period == '4º trimestre':
                    st.markdown("<p style='text-align: center; color: black;'> Em definição...</p>", unsafe_allow_html=True)
                    worksheet = "Desempenho do Processo 2021" #inserir planilha readequação
                    choice = 'Selecione'
                    # choice = st.selectbox('Selecione o processo: ',('Selecione',''))
                    sheet = choice

                if choice == 'Instalação':
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
                    # Desempenho
                    st.markdown('**Tabela do desempenho por mês do ano de 2021**')
                    desempenho = desempenho_instalação_rh(df)
                    st.table(desempenho)

                # Desempenho do setor de Manutenção
                if choice == 'Manutenção':
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
                    # Desempenho
                    st.markdown('**Tabela do desempenho por mês do ano de 2021**')
                    desempenho = desempenho_manutencao(df)
                    st.table(desempenho)

                if choice == 'Almoxarifado':
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
                    # Desempenho
                    st.markdown('**Tabela do desempenho por mês do ano de 2021**')
                    desempenho = desempenho_almoxarifado(df)
                    # Filtra o df pelo mês e retorna df com base no intervalo mensal
                    months = ['Selecione', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
                    'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
                    i = st.slider('Arraste para o mês desejado: ', 1, 10)
                    month = months[i]
                    st.write("Selecionado o mês de ", month)                  
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
                    # Desempenho
                    st.markdown('**Tabela do desempenho por mês do ano de 2021**')
                    desempenho = desempenho_instalação_rh(df)
                    st.table(desempenho)

        if year == '2022':
            st.markdown('Aguardando a definição.')

if option == 'Documentos':
    st.markdown("<h3 style='text-align: center; color: black;'>Documentos</h3>", unsafe_allow_html=True)

    st.markdown("<h6 style='text-align: left; color: black;'>Diretrizes</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    A Constel é um barco, em que todos os colaboradores devem remar na mesma direção. Bem como, a Missão, Visão e Valores compõem um conjunto de diretrizes fundamentais que norteiam a empresa. Além disso, são de extrema importância para orientar o planejamento estratégico e construir uma identidade organizacional, portanto leia atentamente e dissemine seu conteúdo a todos.</p>", unsafe_allow_html=True)
    with open("./files/diretrizes.pdf", 'rb') as f:
        st.download_button('Baixar', f, file_name='Diretrizes Constel.pdf')
    st.write('')

    st.markdown("<h6 style='text-align: left; color: black;'>Política de Qualidade</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    A empresa possuí Política de Qualidade? O que é melhoria contínua? Sabe me dar exemplo? O que são profissionais capacitados e comprometidos? Perguntas que podem ser feitas, e devem ser respondidas com base na Política de Qualidade que é definida a parti de escopo, visando abranger todos os serviços prestados ou que serão prestados pela Constel, então estude, interprete, dissemine e discuta o seu conteúdo com todos da empresa, mas principalmente com os seus subordinados..</p>", unsafe_allow_html=True)
    with open("./files/politica_de_qualidade.pdf", 'rb') as f:
        st.download_button('Baixar', f, file_name='Politica de Qualidade Constel.pdf')
    st.write('')

    st.markdown("<h6 style='text-align: left; color: black;'>Organograma</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    Quem é seu gestor? Para quem você responde? Onde está escrito pra quem você responde? Essas são algumas das perguntas que podem serem feitas a fim de verificar o conhecimento dos colaboradores sobre o Organograma. Após algumas atualizações a versão definitiva está disponível a todos, por isso consulte-o e veja de forma gráfica a estrutura organizacional da empresa e a hierarquia a ser respeitada. </p>", unsafe_allow_html=True)
    with open("./files/organograma.pdf", 'rb') as f:
        st.download_button('Baixar', f, file_name='Organograma Constel.pdf')
    st.write('')

    st.markdown("<h6 style='text-align: left; color: black;'>Fluxograma de Interação de Processos</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    Onde seu processo está inserido no SGQ? É processo de apoio? Processo operacional? O gestor deve saber responder a estas perguntas, por isso é fundamental o entendimento sobre a última versão do Fluxo de Interação dos Processos que visa representar de maneira gráfica o fluxo ideal para a estrutura organizacional da empresa. </p>", unsafe_allow_html=True)
    with open("./files/fluxo_de_interacao.pdf", 'rb') as f:
        st.download_button('Baixar', f, file_name='Fluxo de Interação Constel.pdf')
    st.write('')

    st.markdown("<h6 style='text-align: left; color: black;'>Fluxograma de Entradas e Saídas</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    Como funciona o seu processo? Quais são as entradas? Quais os recursos necessários? Quais as Saídas? Quais entradas vem de outro processo? As suas saídas são entradas de outros processos? Muitas perguntas que podem ser feitas, mas a resposta é a mesma. Com base no fluxo de interação dos processos, foi gerado a Matriz de Entradas e Saídas a qual contém todas as entradas, recursos e saídas do processo. Você como gestor deve saber, além de manter organizado e ter EVIDÊNCIAS de tudo (planilhas, documentos, sistemas etc.), por isso entender o fluxo entre os processos é fundamental. Para facilitar, pode consultar o grande fluxograma desenvolvido pelo Rafael Andreatta, com todos os processos suas respectivas entradas e saídas. </p>", unsafe_allow_html=True)
    with open("./files/Fluxograma.jpg", 'rb') as f:
        st.download_button('Baixar', f, file_name='Fluxograma Constel.jpg')
    st.write('')

    st.markdown("<h6 style='text-align: left; color: black;'>Plano de Contingência</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    O que fazer em caso de acidente? Acabar a luz? Acabar a água? Greve do transporte coletivo? Acidente de trabalho? Incêndio? Falta de materiais? Problemas com o carro? Para responder a essas perguntas, verificar todos os itens presentes no plano de contingência, dando ênfase aos que são inerentes ao processo e as pessoas envolvidas, disponibilizar cópia impressa no setor e disseminar seu conteúdo a todos (escritório e campo). </p>", unsafe_allow_html=True)
    with open("./files/planodecontingencia.pdf", 'rb') as f:
        st.download_button('Baixar', f, file_name='Plano de Contingência Constel.pdf')
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

if option == "Sobre":
    st.markdown('**Autor:** Leonardo de Oliveira Melo')
    st.markdown('**Formação:** Graduando em Eng. Cartógrafica e de Agrimensura')
    st.markdown('**Instituição:** Universidade Federal do Paraná')
    st.markdown('**Linkedin:** https://www.linkedin.com/in/leonardo-oliveira-melo-287593164/')
    st.markdown('**Projeto:** Desenvolver plataforma com os indicadores da Constel')
    st.markdown('**Status:** Em desenvolvimento.')
    st.image(logo_Capa, caption=None, width=150)
