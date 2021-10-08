import streamlit as st
import pandas as pd
from PIL import Image
import gspread
from google.oauth2 import service_account


json_file = "./planejamento-constel123-1b8f07026a82.json"
scopes = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]

def login():
    credentials = service_account.Credentials.from_service_account_file(json_file)
    scoped_credentials = credentials.with_scopes(scopes)
    gc = gspread.authorize(scoped_credentials)
    return gc

def leitor(worksheet,sheet): # Acessa a planilha, a aba específica e retorna um dataframe
    gc = login()
    planilha = gc.open(worksheet)
    aba = planilha.worksheet(sheet)
    dados = aba.get_all_values()
    dfi = pd.DataFrame(dados)
    return dfi

def indicador(df):
    head = df.iloc[3]
    header = list(head[:5])
    dfc = df[4:16]
    dfc = dfc.rename(columns={0: header[0], 1: header[1], 2: header[2], 3: header[3], 4: header[4]})
    filtered_df = dfc.loc[:,header]
    return filtered_df

def desempenho_manutencao(df):
    head = df.iloc[0]
    header = list(head[:18])
    dfc = df[1:13]
    dfc = dfc.rename(columns={0: header[0], 1: header[1], 2: header[2], 3: header[3], 4: header[4],
    5: header[5], 6: header[6], 7: header[7], 8: header[8], 9: header[9], 10: header[10], 11: header[11],
    12: header[12], 13: header[13], 14: header[14], 15: header[15], 16: header[16], 17: header[17]})
    filtered_df = dfc.loc[:,header]
    return filtered_df

def desempenho_instalação_rh(df):
    head = df.iloc[0]
    header = list(head[:6])
    dfc = df[1:13]
    dfc = dfc.rename(columns={0: header[0], 1: header[1], 2: header[2], 3: header[3], 4: header[4],
    5: header[5]})
    filtered_df = dfc.loc[:,header]
    return filtered_df

def desempenho_almoxarifado(df):
    head = df.iloc[0]
    header = list(head[:8])
    dfc = df[1:73]
    dfc = dfc.rename(columns={0: header[0], 1: header[1], 2: header[2], 3: header[3], 4: header[4],
    5: header[5], 6: header[6], 7: header[7]})
    filtered_df = dfc.loc[:,header]
    return filtered_df

def desempenho_plan_proj(df):
    head = df.iloc[0]
    header = list(head[:5])
    dfc = df[1:13]
    dfc = dfc.rename(columns={0: header[0], 1: header[1], 2: header[2], 3: header[3], 4: header[4]})
    filtered_df = dfc.loc[:,header]
    return filtered_df

def desempenho_seg_trabalho(df):
    head = df.iloc[3]
    header = list(head[:5])
    dfc = df[4:16]
    dfc = dfc.rename(columns={0: header[0], 1: header[1], 2: header[2], 3: header[3], 4: header[4]})
    filtered_df = dfc.loc[:,header]
    return filtered_df

logo_C = Image.open("./LogoC.png")
logo_Capa = Image.open("./Logo_C_capa.png")
header = Image.open("./header.png")
logo_Cinza = Image.open("./Logo_Site.png")
fluxograma = Image.open("./Fluxograma.jpg")
contigencia = open("planodecontingencia.pdf")
organograma = open("organograma.pdf")


# Barra lateral
st.sidebar.image(logo_C, caption=None, width=75)
st.sidebar.title('**Home**')
option = st.sidebar.selectbox('Selecione a página desejada', ['Início', 'Indicadores', 'Desempenho', 'Documentos', 'Sobre'])
if option == 'Início':
    # Página inicial
    st.image(header, caption=None, width=800)
    st.header('**Bem vindo!**')
    st.markdown('Nesta plataforma você encontrará os indicadores do Plano de Objetivos e Metas e o desempenho dos processos da Constel')
    st.markdown('Clique na aba lateral para navegar pelo site')

if option == 'Documentos':
    st.markdown('**Fluxograma de Entradas e Saídas**')
    st.markdown('O documento contém as entradas e saídas dos processos da empresa')
    with open('Fluxograma.jpg', 'rb') as f:
	    st.download_button('Baixar', f, file_name='Fluxograma.jpg')
    st.markdown('**Plano de Contingência**')
    st.markdown('O documento contém o plano de contingêcia da empresa')
    with open('planodecontingencia.pdf', 'rb') as f:
	    st.download_button('Baixar', f, file_name='planodecontingencia.pdf')
    st.markdown('**Organograma**')
    st.markdown('O documento contém a hierarquia dos cargos da empresa')
    with open('organograma.pdf', 'rb') as f:
	    st.download_button('Baixar', f, file_name='organograma.pdf')


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
    st.markdown('Nesta aba é possível visualizar os indicadores dos setores da empresa.')
    choice = st.selectbox('Escolha o setor: ',('Selecione', 'Instalação', 'Manutenção','Planejamento','Comercial','Controle de Qualidade', 
    'Seg. do Trabalho', 'Fechamento', 'Projetos', 'RH', 'Geral'))
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

if option == 'Sobre':
    st.markdown('**Autor:** Leonardo de Oliveira Melo')
    st.markdown('**Formação:** Graduando em Eng. Cartógrafica e de Agrimensura')
    st.markdown('**Instituição:** Universidade Federal do Paraná')
    st.markdown('**Linkedin:** https://www.linkedin.com/in/leonardo-oliveira-melo-287593164/')
    st.markdown('**Projeto:** Desenvolver plataforma com os indicadores da Constel')
    st.markdown('**Status:** Em desenvolvimento.')
    st.image(logo_Capa, caption=None, width=150)
