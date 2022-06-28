from turtle import width
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components


def texto_inicial():
    return """
<div class="card" style='text-align: justify'>
  <div class="card-body">
    <h5 class="card-title"></h5>
    <h5 class="card-title">Aqui você encontrará:</h5>
    <p class="card-text">▪️ Indicadores dos processos;</p>
    <p class="card-text">▪️ Formulários;</p>
    <p class="card-text">▪️ Documentos relacionados ao SGQ</p>
    <p class="card-text"></p>
    <p class="card-text">Para navegar entre as abas, expanda o menu de seleção e selecione a página desejada</p>
  </div>
</div>
"""

# Abre arquivos de imagem

logo_C = Image.open("./thumbnail/LogoC.png")
C_festa = Image.open("./thumbnail/C_festa.png")
C_aviso = Image.open("./thumbnail/C_aviso.png")
logo_Capa = Image.open("./thumbnail/Logo_C_capa.png")
logo_Capa_pagina = Image.open("./thumbnail/Logo_C_capa_pagina.png")
logo_Capa_calendario = Image.open("./thumbnail/Logo_C_capa_calendario.png")
logo_Capa_processo = Image.open("./thumbnail/Logo_C_capa_processo.png")
header = Image.open("./thumbnail/header_inicio.png")
header_indicadores = Image.open("./thumbnail/header_indicadores.png")
header_formularios = Image.open("./thumbnail/header_formularios.png")
header_documentos = Image.open("./thumbnail/header_documento.png")
header_informacoes = Image.open("./thumbnail/header_informacoes.png")
logo_Cinza = Image.open("./thumbnail/Logo_Site.png")
st.set_page_config(
page_title="Constel",
page_icon=logo_C,
layout="wide",
initial_sidebar_state="expanded")
# Define os acessos para cada colaborador
huawei_wl = ['Leonardo Melo','Daniel Souza', 'Fernando Cerqueira', 'Iago Iabiku']
constr_prumadas = None

#CABEÇALHO COM ACESSO AOS APPs
st.markdown("----")
col01, col02, col03 = st.columns([1, 1, 1])
with col01:
    st.image(logo_Capa_pagina, width=100)
    pagina = st.radio(
    "Selecione a página: ",
    ("Início","Indicadores", "Formulários", "Documentos", "Informações"))

with col02:
    if pagina == "Indicadores":
        st.image(logo_Capa_calendario, width=100)
        pagina_year = st.radio(
        "Selecione o ano: ",
        ('Selecione', '2021', '2022', '2023'))
        if pagina_year == '2021':
            processos_tupla = ('Selecione', 'Instalação Wireless', 'Instalação de Prumadas', 'Instalação (Instalação de Internet)', 'Planejamento', 'Projetos', 'Comercial',
            'RH','Controle de Qualidade', 'Seg. do Trabalho', 'Fechamento (descontinuado)', 'Manutenção (descontinuado)')
        else:
            processos_tupla = ('Selecione', 'Instalação', 'Planejamento', 'Projetos', 'Comercial', 'RH','Controle de Qualidade', 'Seg. do Trabalho')

with col03:
    if pagina == "Indicadores":
        if pagina_year != 'Selecione':
            st.image(logo_Capa_processo, width=100)
            pagina_ind = st.radio(
            "Selecione o processo: ", processos_tupla)
st.markdown("----")



# # Barra lateral
# st.sidebar.image(logo_C, caption=None, width=75)
# st.sidebar.title('**Constel Engenharia Elétrica**')
# option = st.sidebar.selectbox('Selecione a página desejada', ["Início", "Formulários","Indicadores", "Documentos", "Sobre"])

# Abas da aplicação
if pagina == "Início":
    # Página inicial
    st.image(header, caption=None, use_column_width=True)
    st.markdown(texto_inicial(),unsafe_allow_html=True)
    st.markdown("----")     
    st.markdown("")
    col11, col12 = st.columns([1, 1])
    with col11:
        st.markdown("<h6 style='text-align: center; color: black;'>Apresentação</h6>", unsafe_allow_html=True)
        st.markdown(" ")
        components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTU0773TwwYa249dB9ZbieogaeK8g2h_wlE-fghJvK4V0DTPcWxzzosx-jKO7tNvWJzE-RNCNvsn_ka/embed?start=false&loop=false&delayms=3000", width=360, height=239)   
        # st.markdown("<h6 style='text-align: center; color: black;'Aniversariantes do mês</h6>", unsafe_allow_html=True)
        st.markdown("----")
        st.image(C_festa, caption=None, width=75)
        st.markdown("<h6 style='text-align: center; color: black;'Aniversariantes do mês</h6>", unsafe_allow_html=True)
        st.markdown(" ")
        components.iframe("https://docs.google.com/spreadsheets/d/e/2PACX-1vRVvM6x4YULHM3MGUYQxDcCS0BgF6xB6p-e2WXnH91joME173m8_Nn1QB9ws7qT3fxCFqqN2B7cAq0_/pubhtml?gid=304685294&amp;single=true&amp;widget=true&amp;headers=false", width=360, height=500)

    with col12:
        st.markdown("<h6 style='text-align: center; color: black;'>Mural de avisos</h6>", unsafe_allow_html=True)
        st.image(C_aviso, caption=None, width=75)
        st.markdown(" ")
        components.iframe("https://docs.google.com/spreadsheets/d/e/2PACX-1vS5okgUghoWGn4_ZaKN5qvERwm1WGAvtsE-edaqTXsjdjEa9BMo7JLtQCGQJ01EPLpnWHGnEYTXcG4j/pubhtml?gid=304685294&amp;single=true&amp;widget=true&amp;headers=false", width=360, height=500)
            

    # st.markdown("<h3 style='text-align: center; color: black;'>Bem vindo!</h3>", unsafe_allow_html=True)
    # st.markdown("<p style='text-align: center; color: black;'>Nesta plataforma você encontrará:</p>", unsafe_allow_html=True)
    # st.markdown("<p style='text-align: left; color: black;'>▪️ Indicadores dos processos;</p>", unsafe_allow_html=True)
    # st.markdown("<p style='text-align: left; color: black;'>▪️ Formulários;</p>", unsafe_allow_html=True)
    # st.markdown("<p style='text-align: left; color: black;'>▪️ Documentos relacionados ao Sistema de Gestão da Qualidade</p>", unsafe_allow_html=True)
    # st.markdown("----")

# if option == "Dashboard":
#     names = ['Leonardo Melo', 'Daniel Souza', 'Fernando Cerqueira', 'Iago Iabiku']
#     usernames = ['lmelo', 'dsouza', 'fcerqueira', 'iiabiku']
#     passwords = ['plan2022', 'coord2022', 'proj2022', 'proj2022']
#     hashed_passwords = stauth.hasher(passwords).generate()
#     authenticator = stauth.authenticate(names,usernames,hashed_passwords,
#     'some_cookie_name','some_signature_key',cookie_expiry_days=30)
#     name, authentication_status = authenticator.login('Login','main')
#     if st.session_state['authentication_status']:
#         st.write('Olá **%s**' % (st.session_state['name']))
#         if name in huawei_wl:
#             st.markdown("")
#             st.markdown("<h3 style='text-align: center; color: black;'>Dashboard Huawei WL</h3>", unsafe_allow_html=True)
#             dashboard = st.selectbox('Selecione a dashboard desejada: ', ["Controle Geral dos sites", "Controle Custos dos sites"])
#             if dashboard == "Controle Geral dos sites":
#                 st.markdown("----")
#                 components.iframe("https://datastudio.google.com/embed/reporting/34fc41f4-dea7-4142-a903-ad13eaf5e113/page/p_1zxcslmxqc", width=900, height=650)
#                 st.markdown("---")
#             else: 
#                 st.markdown("----")
#                 components.iframe("https://datastudio.google.com/embed/reporting/68bf276e-80cb-4d8e-9362-c64802376710/page/PgiiC", width=900, height=650)
#                 st.markdown("---")
#             st.markdown("<h6 style='text-align: center; color: black;'>Mapa de localização dos Sites</h6>", unsafe_allow_html=True)
#             components.iframe("https://www.google.com/maps/d/embed?mid=1r6xzmsAeiSD3cniV-oXD_MWHGMPyYVZ8&ehbc=2E312F", width=900, height=550)

#         if name in constr_prumadas:   
#             st.write('Em desenvolvimento...')        
        
    
#     elif st.session_state['authentication_status'] == False:
#         st.error('Usuário ou senha incorretos')
#     elif st.session_state['authentication_status'] == None:
#         st.warning('Por favor entre com o usuário e senha!')

if pagina == "Formulários":
    st.image(header_formularios, caption=None, use_column_width=True)       
    st.markdown("----")
    avaliation = st. selectbox('Selecione a avaliação:', ('Selecione','Avaliação 1', 'Avaliação 2'))
    if avaliation != 'Selecione':
        if avaliation == 'Avaliação 1':
            components.iframe("https://docs.google.com/forms/d/e/1FAIpQLSeoJkyF1mkJIeA9kcrKGHswg68SGcEYjGc4i4kKKoZXieIxKw/viewform?embedded=true", width=360, height=4000)
        else:
            components.iframe("https://docs.google.com/forms/d/e/1FAIpQLScZ0VeavfUM2rWkwKkjhCXpVgvPRbs4M3A8a89lV0k4ranKMw/viewform?embedded=true", width=360, height=4200)
        st.markdown("---")
    else:
        st.markdown("<p style=' text-align: center; color: black'>Nesta seção é possível encontrar avaliações relacionadas ao Sistema de Gestão da Qualidade.</p>", unsafe_allow_html=True)

if pagina == 'Indicadores':

    st.image(header_indicadores, caption=None, use_column_width=True)

    if pagina_year != "Selecione":

        if pagina_ind != 'Selecione':

            if pagina_ind == 'Instalação Wireless':
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSf9r-Fa3eHb2hRK7QAlO8tfRzr9yo6jV2VwQoQL0XSMTQWa8Sb5UwGLde96LvkRt9VqhCmqwbLJ487/embed?start=false&loop=false&delayms=3000", width=360, height=239)                  


            if pagina_ind == 'Instalação de Prumadas':
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQo6yyBBPA2SPhswZy9LtaIJCyPG4uyb5Rcmk43AdeNv4ZRFJl5Oc7BZgjswAEoiK-q4MQnzPHtdOc2/embed?start=false&loop=false&delayms=3000", width=360, height=239)                


            if pagina_ind == 'Instalação (Instalação de Internet)':
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRuL0INb5me9CXnM-Qa8Xjimn6yNI6kTQrKePpeOKJzxXIplKiyQG4h9GL3AIBckDTEOtZIv14dQ2V1/embed?start=false&loop=false&delayms=3000", width=360, height=239)                  


            if pagina_ind == 'Planejamento':
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTgk6GSKylyIMLmGXGWqHMzAwI1yrT3t-Zc4WGQn2q_HVlAVYzDBcHimceZa4tPe48kG5NVhv_id8su/embed?start=false&loop=false&delayms=3000", width=360, height=239)                  


            if pagina_ind == 'Projetos':
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vR8X8lbRZ4wsd95GnqqMxBPzabSDmucjWji33u2vbcu2YzypVveiOgAxYdV4ANsaNAsEdbOetn3l-gf/embed?start=false&loop=false&delayms=3000", width=360, height=239)                   


            if pagina_ind == 'Comercial':
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSLJ0Mam-ZchjJ3sljm40s5EDdyNPLy52lIURT5zyjQkvExLam_cwCW19uVtwp1Ey7CZgO7481QbJGd/embed?start=false&loop=false&delayms=3000", width=360, height=239)                 
                

            if pagina_ind == 'RH': 
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRCrRbsjGljxFSVRu2ij_JMOLF5UaLG-LNG1ZMpCqzk9qUba_fidw5umvmE2ru6cAsYII_ip2b3SPDW/embed?start=false&loop=false&delayms=3000", width=360, height=239)                  


            if pagina_ind == 'Controle de Qualidade':
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSpk2g1Eo1Rp7S0706nRhdjC7M1m3P9ROoFcBkcfAjYnT73ckFPa0HYx4iByAOslXI6HsBMZvYZmYwX/embed?start=false&loop=false&delayms=3000", width=360, height=239)                  


            if pagina_ind == 'Seg. do Trabalho':
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQFHwZxPOpckZzibgwhSpXe3RlSYVtm8_hJ77eiMzkMdX1Zz80nKyPflSk7gHfnk9KfyAEqSzdu_dur/embed?start=false&loop=false&delayms=3000", width=360, height=239)                  


            if pagina_ind == 'Fechamento (descontinuado)':
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSqjnR8S738NoMgDBOz9M-4c0SvH-gQEVWEXnnOfgBi_xyKZNzKK26MLWSBDdJOsjzoOQizP8QRIvQa/embed?start=false&loop=false&delayms=3000", width=360, height=239)                  


            if pagina_ind == 'Manutenção (descontinuado)':
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTJ65Gi958pvOegMi6_0uOV4i-TFjSY3OZCS7i7gKTxqiOY3H98or-XWWmZG7fNLYLkaIUMpwL-R2uX/embed?start=false&loop=false&delayms=3000", width=360, height=239)                   


        if pagina_year == '2022':
            st.markdown("----")
            st.markdown("<p style=' text-align: justify; color: black'>Em preenchimento...</p>", unsafe_allow_html=True)
            st.markdown("----")
                        
if pagina == 'Documentos':
    st.image(header_documentos, caption=None, use_column_width=True)
    st.markdown("----")
    st.markdown("<h6 style='text-align: left; color: black;'>Diretrizes</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    Documento que apresenta a Missão, Visão e Valores compõem um conjunto de diretrizes fundamentais que norteiam a empresa.</p>", unsafe_allow_html=True)
    with open("./files/diretrizes.pdf", 'rb') as f:
        st.download_button('Baixar', f, file_name='Diretrizes Constel.pdf')
    st.markdown("----")
    st.write('')

    st.markdown("<h6 style='text-align: left; color: black;'>Política de Qualidade</h6>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: black;'>    - A empresa possuí Política de Qualidade?</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: black;'>    - O que é melhoria contínua? Sabe me dar exemplo?</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: black;'>    - O que são profissionais capacitados e comprometidos?</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: black;'>    São perguntas que podem ser feitas, e devem ser respondidas com base na Política de Qualidade.</p>", unsafe_allow_html=True)
    with open("./files/politica_de_qualidade.pdf", 'rb') as f:
        st.download_button('Baixar', f, file_name='Politica de Qualidade Constel.pdf')
    st.markdown("----")
    st.write('')

    st.markdown("<h6 style='text-align: left; color: black;'>Organograma</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    - Quem é seu gestor?</p>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    Consulte o organograma e veja de forma gráfica a estrutura organizacional da empresa e a hierarquia a ser respeitada. </p>", unsafe_allow_html=True)
    with open("./files/organograma.pdf", 'rb') as f:
        st.download_button('Baixar', f, file_name='Organograma Constel.pdf')
    st.markdown("----")
    st.write('')

    st.markdown("<h6 style='text-align: left; color: black;'>Fluxograma de Interação de Processos</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    - Onde seu processo está inserido no SGQ?</p>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    - É um processo de apoio? É um processo operacional?</p>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    Consulte onde seu processo está inserido e veja de maneira gráfica o fluxo ideal para a estrutura organizacional da empresa. </p>", unsafe_allow_html=True)
    with open("./files/fluxo_de_interacao.pdf", 'rb') as f:
        st.download_button('Baixar', f, file_name='Fluxo de Interação Constel.pdf')
    st.markdown("----")
    st.write('')

    st.markdown("<h6 style='text-align: left; color: black;'>Fluxograma de Entradas e Saídas</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    Consulte o fluxograma da Matriz de Entradas e Saídas a qual contém todas as entradas, recursos e saídas do processo.</p>", unsafe_allow_html=True)
    with open("./files/Fluxograma.jpg", 'rb') as f:
        st.download_button('Baixar', f, file_name='Fluxograma Constel.jpg')
    st.markdown("----")
    st.write('')

    st.markdown("<h6 style='text-align: left; color: black;'>Plano de Contingência</h6>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    - O que fazer em caso de acidente? o carro?</p>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    - Acabar a luz?</p>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    - Greve do transporte coletivo?</p>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    - Acidente de trabalho?</p>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    - Problemas com o carro?</p>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; color: black;'>    Este documento trás as respostas para todas essas perguntas</p>", unsafe_allow_html=True)
    with open("./files/planodecontingencia.pdf", 'rb') as f:
        st.download_button('Baixar', f, file_name='Plano de Contingência Constel.pdf')
    st.markdown("----")
    # st.write('')

    # st.markdown("<h6 style='text-align: left; color: black;'>Controle de Documentos</h6>", unsafe_allow_html=True)
    # st.write("<p style='text-align: justify; color: black;'>    Qual versão está o documento utilizado pelo processo? Quando foi feita última revisão? E propriedade da empresa ou do cliente? Todos os documentos e registros que forem criados ou alterados devem ser comunicados ao responsável pela Gestão da Qualidade a fim de verificar se possuem as informações básicas, como: Processo, data de elaboração, número e data da última revisão. Além disso, TUDO que é criado e utilizado pelo processo deve ser inserido no Controle de Documentos, essa planilha possui informações importantes que visa facilitar a busca de todos os colaboradores a documentos e registros existentes. </p>", unsafe_allow_html=True)
    # st.markdown("----")
    # st.write('')

    # st.markdown("<h6 style='text-align: left; color: black;'>Análise de Risco da Mudança Solicitada</h6>", unsafe_allow_html=True)
    # st.write("<p style='text-align: justify; color: black;'>    Você precisou realizar alguma mudança no processo? Teve algo que mudaram e teve impacto ao SGQ? Quando houver necessidade de mudança no seu processo, o que você faz? Para toda mudança no processo, deve-se analisar quais os riscos associados e o impacto que causará ao Sistema de Gestão da Qualidade (quer realocar a mesa dentro do seu setor – OK, porém se quiser realizar uma melhoria/ alteração que vá influenciar nos demais processos é necessário realizar essa análise). Para isso, deve-se utilizar o documento Análise de Risco da Mudança Solicitada em conjunto com um cronograma de execução, para que as etapas da mudança sejam implementadas. </p>", unsafe_allow_html=True)
    # st.markdown("----")
    # st.write('')

    # st.markdown("<h6 style='text-align: left; color: black;'>Análise SWOT com Riscos</h6>", unsafe_allow_html=True)
    # st.write("<p style='text-align: justify; color: black;'>    Qual o risco do seu processo para o negócio? Qual é o grau desse risco? Quais as ações que visam mitigá-lo? O plano de ação é para 1 ou 2 anos? A matriz SWOT, ou FOFA é uma ferramenta de planejamento estratégico, a qual contém os pontos fortes e fracos, relacionados ao ambiente interno (Forças e Fraquezas) e externo da empresa (Oportunidades e Ameaças). Assim como os indicadores, as ações presentes no planejamento estratégico devem ser analisadas periodicamente (semestral), fazendo uma análise completa sobre tudo o que foi feito durante o período e quais serão as próximas ações. A planilha está disponível de forma online a fim de facilitar a edição simultânea por parte dos gestores. TODOS que fazem parte do seu processo devem ter conhecimento do(s) risco(s) que pode(m) impactar de forma positiva ou negativa o planejamento estratégico da empresa. </p>", unsafe_allow_html=True)
    # st.markdown("----")
    # st.write('')

if pagina == "Informações":
    st.image(header_informacoes, caption = None, use_column_width=True)
    st.markdown("<p style='text-align: justify; color: black;'><b>Autor:</b> Leonardo de Oliveira Melo", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: black;'><b>Formação:</b> Eng. Cartógrafo e Agrimensor", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: black;'><b>Instituição:</b> <a href='https://www.ufpr.br/portalufpr/'> Universidade Federal do Paraná</a>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: black;'><b>LinkedIn:</b> <a href='https://www.linkedin.com/in/leonardo-oliveira-287593164/'> Visualizar perfil</a>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: black;'><b>Projeto:</b> Disponibilizar através de uma aplicação web, os indicadores dos processos da empresa, visando atingir todos os colaboradores da empresa e facilitando o acesso aos colaboradores externos o contato com os documentos referentes ao SGQ.", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: black;'><b>Funcionamento:</b> A aplicação utiliza aplicações do Google para visualização das informações, onde os gestores atualizam as informações presentes na aplicação por meio do Google Planilhas e Google Apresentações. A escolha destas ferramentas se deu pela facilidade de atualização das informações a fim de que os gestores não precisem de conhecimento de programação para publicar atualizações.", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: black;'><b>Status:</b> Em desenvolvimento.", unsafe_allow_html=True)
    st.image(logo_Capa, caption=None, width=150)