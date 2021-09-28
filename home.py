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

def leitor(worksheet,sheet): # Entra na planilha e pega as informações necessárias
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

def write_month(value):
    if value == 1:
        value = 'Janeiro'
    if value == 2:
        value = 'Fevereiro'
    if value == 3:
        value = 'Março'
    if value == 4:
        value = 'Abril'
    if value == 5:
        value = 'Maio'
    if value == 6:
        value = 'Junho'
    if value == 7:
        value = 'Julho'
    if value == 8:
        value = 'Agosto'
    if value == 9:
        value = 'Setembro'
    if value == 10:
        value = 'Outubro'
    if value == 11:
        value = 'Novembro'
    if value == 12:
        value = 'Dezembro'
    return value

def filter_value(value, df):
    value = write_month(value)
    df_mask = df['Mês'] == value
    filtered_df = df[df_mask]
    return filtered_df

#@st.cache(suppress_st_warning=True)
def map_plot():
    points = pd.DataFrame({"lat": [-25.5, -25.4],
                            "lon": [-49.265, -49.285]})
    map = st.map(points)
    return map

logo_C = Image.open("./LogoC.png")
logo_Capa = Image.open("./Logo_C_capa.png")
st.sidebar.image(logo_C, caption=None, width=75)

# Barra lateral
st.sidebar.title('**Bem vindo**!')
option = st.sidebar.selectbox('Selecione a página desejada', ['Início', 'Indicadores', 'Sobre'])
if option == 'Início':
    # Página inicial
    st.image(logo_Capa, caption=None, width=200)
    st.header('**Página Inicial**')
    st.markdown('Navegue pela plataforma e visualize os indicadores das atividades realizadas pela empresa')
    st.markdown('"**A plataforma está em desenvolvimento !**"')
    
# if option == 'Rede Horizons':
#     st.header('**Rede Horizons**')
#     st.markdown('A idéia é implementar um mapa da rede da Horizons, para que o gestor procure pela atividade e encontre recurso próximo sem depender do setor')
#     st.markdown('-Inserir mapa aqui-')
#     map_plot()
#     st.markdown('A página está em desenvolvimento')

if option == 'Indicadores':
    st.markdown('Nesta aba é possível visualizar os indicadores dos setores da empresa.')
    choice = st.selectbox('Escolha o indicador: ',('Selecione', 'Instalação', 'Manutenção','Planejamento', 'Compras', 'Financeiro', 'Comercial','Controle de Qualidade', 
    'Manutenção', 'Seg. do Trabalho', 'Fechamento', 'Projetos', 'RH', 'Geral'))
    # Indicador geral da empresa, mostrando os processos que puxam pra baixo, se for preciso definir pesos para os processos
    worksheet = "Plano de Objetivos e Metas 2021 e Controle de Documentos" # Podemos colocar selecionando o ano
    sheet = choice
    if choice == 'Instalação':
        st.markdown('**Indicador:** Instalação')
        df = leitor(worksheet, sheet)
        ind = indicador(df)
        st.table(ind)
        select = st.checkbox('Selecione para ver o indicador por mês: ')
        if select == 1:
            month = st.slider('Selecione o Mês', min_value=0, max_value=12)
            st.write(write_month(month))
            st.table(filter_value(month, ind))

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

    if choice == 'Compras':
        st.markdown('**Indicador:** Compras')
        df = leitor(worksheet, sheet)
        ind = indicador(df)
        st.table(ind)

    if choice == 'Financeiro':
        st.markdown('**Indicador:** Financeiro')
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
    st.markdown('**Projeto:** Desenvolver uma plataforma com os indicadores da Constel')
    st.markdown('**Status:** Em desenvolvimento.')
    st.image(logo_Capa, caption=None, width=150)
