import streamlit as st
from PIL import Image
from functions import leitor, indicador, desempenho_manutencao, desempenho_instalação_rh
from functions import desempenho_almoxarifado, desempenho_plan_proj, desempenho_seg_trabalho, indicador4t
import streamlit.components.v1 as components

# Abre arquivos de imagem

logo_C = Image.open("./thumbnail/LogoC.png")
logo_Capa = Image.open("./thumbnail/Logo_C_capa.png")
header = Image.open("./thumbnail/header.png")
header_indicadores = Image.open("./thumbnail/header_indicadores.png")
header_desempenho = Image.open("./thumbnail/header_desempenho.png")
logo_Cinza = Image.open("./thumbnail/Logo_Site.png")
st.set_page_config(
page_title="Constel",
page_icon=logo_C,
layout="wide",
initial_sidebar_state="expanded")
# Define os acessos para cada colaborador
huawei_wl = ['Leonardo Melo','Daniel Souza', 'Fernando Cerqueira', 'Iago Iabiku']
constr_prumadas = None

# Barra lateral
st.sidebar.image(logo_C, caption=None, width=75)
st.sidebar.title('**Constel Engenharia Elétrica**')
option = st.sidebar.selectbox('Selecione a página desejada', ["Início", "Formulários","Indicadores", "Desempenho", "Documentos", "Sobre"])

# Abas da aplicação
if option == "Início":
    # Página inicial
    st.image(header, caption=None, use_column_width=True)
    st.markdown("<h3 style='text-align: center; color: black;'>Bem vindo!</h3>", unsafe_allow_html=True)
    st.markdown("----")
    st.markdown("<p style='text-align: center; color: black;'>Nesta plataforma você encontrará:</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; color: black;'>▪️ Indicadores dos processos;</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; color: black;'>▪️ Desempenho dos processos;</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; color: black;'>▪️ Formulários;</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; color: black;'>▪️ Documentos relacionados ao Sistema de Gestão da Qualidade</p>", unsafe_allow_html=True)
    st.markdown("----")

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

if option == "Formulários":
    st.markdown("<h3 style='text-align: center; color: black;'>Formulários</h3>", unsafe_allow_html=True)       
    st.markdown("----")
    components.iframe("https://docs.google.com/forms/d/e/1FAIpQLSeoJkyF1mkJIeA9kcrKGHswg68SGcEYjGc4i4kKKoZXieIxKw/viewform?embedded=true", width=640, height=1550)
    st.markdown("---")

if option == 'Indicadores':
    st.image(header_indicadores, caption=None, use_column_width=True)
    year = st.selectbox('Selecione o ano desejado: ',('Selecione','2021','2022'))
    if year != "Selecione":
        if year == '2021':
            st.info("""
                Em 2021 ocorreu uma reestruturação da empresa, devido ao encerramento do contrato com a Copel Telecom.\n
                Foram então remodelados os indicadores de alguns processos atendendo as novas demandas da empresa.""")
            st.markdown("----")
            choice = st.selectbox('Selecione o processo para visualizar: ', ('Selecione', 'Instalação Wireless', 'Instalação de Prumadas', 'Instalação (Instalação de Internet)', 'Planejamento', 'Projetos', 'Comercial',
            'RH','Controle de Qualidade', 'Seg. do Trabalho', 'Fechamento (descontinuado)', 'Manutenção (descontinuado)'))
    
            if choice != 'Selecione':

                if choice == 'Instalação Wireless':
                    sheet = 'Instalação Wireless'
                    worksheet = 'Plano de Objetivos e Metas 2021 (Revisão 01 Readequação devido término do contrato da Copel)'
                    df = leitor(worksheet, sheet)
                    st.markdown("<h4 style='text-align: center; color: black'>Plano de Objetivos e Metas</h4", unsafe_allow_html=True)
                    st.info("""Atendendo a nova demanda de serviços wireless, este processo foi integrado a empresa no 4º Trimestre de 2021.\n
                            """)
                    st.markdown('**Indicador:** Aumentar a quantidade de sites finalizados no trimestre.')
                    ind = indicador(df)
                    mask = ind['SITES FINALIZADOS']!=''
                    ind_mask = ind[mask]
                    st.table(ind_mask)
                    check4t = st.checkbox((list(df.iloc[23])[0]).title())
                    if check4t == 1:
                        st.write(list(df.iloc[24])[0])

                if choice == 'Instalação de Prumadas':
                    sheet = 'Instalação de Prumadas'
                    worksheet = 'Plano de Objetivos e Metas 2021 (Revisão 01 Readequação devido término do contrato da Copel)'
                    df = leitor(worksheet, sheet)
                    st.markdown("<h4 style='text-align: center; color: black'>Plano de Objetivos e Metas</h4", unsafe_allow_html=True)
                    st.info("""Atendendo a nova demanda de serviços de prumada, este processo foi integrado a empresa no 4º Trimestre de 2021.\n
                            """)
                    st.markdown('**Indicador:** Fazer o maior número possível dentre as prumadas liberadas para execução.')
                    ind = indicador(df)
                    mask = ind['Atividades Concluídas']!= '0'
                    ind = ind.drop(columns=[''])
                    ind_mask = ind[mask]
                    st.table(ind_mask)
                    check4t = st.checkbox((list(df.iloc[30])[0]).title())
                    if check4t == 1:
                        st.write(list(df.iloc[31])[0])

                if choice == 'Instalação (Instalação de Internet)':
                    sheet = 'Instalação de Internet'
                    worksheet = 'Plano de Objetivos e Metas 2021 (Revisão 01 Readequação devido término do contrato da Copel)'
                    df = leitor(worksheet, sheet)
                    st.info("Após a readequação ocorrida para o 4º trimestre, este processo sofreu alteração no nome, passando de **Instalação** para **Instalação de Internet**, para diferenciar com os demais tipos de instalação realizados pela empresa.")
                    st.markdown("<h4 style='text-align: center; color: black'>Plano de Objetivos e Metas</h4", unsafe_allow_html=True)
                    st.markdown('**Indicador:** Atender a meta trimestral de atividades concluídas x total de instalações')
                    ind = indicador(df)
                    st.table(ind)
                    check1 = st.checkbox((list(df.iloc[24])[0]).title())
                    if check1 == 1:
                        st.write(list(df.iloc[25])[0])
                    check2 = st.checkbox((list(df.iloc[26])[0].title()))
                    if check2 == 1:
                        st.write(list(df.iloc[27])[0])
                    check3 = st.checkbox((list(df.iloc[28])[0].title()))
                    if check3 == 1:
                        st.write(list(df.iloc[29])[0])
                    check4 = st.checkbox((list(df.iloc[30])[0].title()))
                    if check4 == 1:
                        st.write(list(df.iloc[31])[0])
                    st.markdown('----')
                    st.markdown('**Indicador de Desempenho:** Quantidade de instalações x Quantidade de vendas')
                    st.info("Os indicadores de desempenho são os responsáveis por ajudar você a atingir suas metas e objetivos.")
                    worksheet_d = 'Desempenho do Processo 2021_Readequação_4º Trimestre'
                    sheet_d = 'Instalação'
                    df_desempenho = leitor(worksheet_d, sheet_d)
                    st.markdown("<h4 style='text-align: center; color: black'>Desempenho</h4", unsafe_allow_html=True)
                    check_desempenho = st.checkbox('Selecione para ver os indicadores de desempenho do processo.')
                    if check_desempenho == 1:
                        desempenho = desempenho_instalação_rh(df_desempenho)
                        st.table(desempenho)
                        check1_d = st.checkbox((list(df_desempenho.iloc[29])[0]).title() + " - Desempenho")
                        if check1_d == 1:
                            st.write(list(df_desempenho.iloc[30])[0])
                        check2_d = st.checkbox((list(df_desempenho.iloc[31])[0]).title() + " - Desempenho")
                        if check2_d == 1:
                            st.write(list(df_desempenho.iloc[32])[0])
                        check3_d = st.checkbox((list(df_desempenho.iloc[33])[0]).title() + " - Desempenho")
                        if check3_d == 1:
                            st.write(list(df_desempenho.iloc[34])[0])
                        check4_d = st.checkbox((list(df_desempenho.iloc[35])[0]).title() + " - Desempenho")
                        if check4_d == 1:
                            st.write(list(df_desempenho.iloc[36])[0])
                            
                if choice == 'Planejamento':
                    sheet = choice
                    worksheet = 'Plano de Objetivos e Metas 2021'
                    df = leitor(worksheet, sheet)
                    worksheet2 = 'Plano de Objetivos e Metas 2021 (Revisão 01 Readequação devido término do contrato da Copel)'
                    sheet2 = 'Planejamento 1'
                    df1 = leitor(worksheet2, sheet2)
                    sheet3 = 'Planejamento 2'
                    df2 = leitor(worksheet2, sheet3)
                    st.markdown("<h4 style='text-align: center; color: black'>Plano de Objetivos e Metas</h4", unsafe_allow_html=True)
                    st.markdown('----')
                    st.markdown('**Indicador:** Reduzir a média de cabo óptico drop utilizado por atividade (antes da readequação)')
                    ind = indicador(df)
                    mask = ind['Quantidade de atividades']!=''
                    ind = ind.drop(columns=[''])
                    st.table(ind[mask])
                    check1t = st.checkbox((list(df.iloc[24])[0]).title())
                    if check1t == 1:
                        st.write(list(df.iloc[25])[0])
                    check2t = st.checkbox((list(df.iloc[26])[0]).title())
                    if check2t == 1:
                        st.write(list(df.iloc[27])[0])
                    check3t = st.checkbox((list(df.iloc[28])[0]).title())
                    if check3t == 1:
                        st.write(list(df.iloc[29])[0])
                    st.markdown('----')
                    st.info("""Após a readequação ocorrida, este processo assumiu novos indicadores definidos para o 4º trimestre e para o ano vigente.""")
                    st.markdown('**Indicador:** Planejamento: Solicitação de acessos antecipadamente. (após a readequação)')
                    ind1 = indicador(df1)
                    mask1 = ind1['Quantidade de solicitações de acessos']!='0'
                    ind1 = ind1.drop(columns=[''])
                    st.table(ind1[mask1])
                    check4t1 = st.checkbox((list(df1.iloc[30])[0]).title() + " - Acessos")
                    if check4t1 == 1:
                        st.write(list(df1.iloc[31])[0])
                    st.markdown('----')
                    st.markdown('**Indicador:** Planejamento: Elaborar os pré-projetos da prumada em função das vistorias executadas. (após a readequação)')
                    ind2 = indicador(df2)
                    mask2 = ind2['Quantidade de vistorias']!='0'
                    ind2 = ind2.drop(columns=[''])
                    st.table(ind2[mask2])
                    check4t1 = st.checkbox((list(df2.iloc[30])[0]).title() + " - Prumadas")
                    if check4t1 == 1:
                        st.write(list(df2.iloc[31])[0])
                    st.markdown('----')
                    st.markdown("<h4 style='text-align: center; color: black'>Desempenho</h4", unsafe_allow_html=True)
                    st.markdown('**Indicador de Desempenho:** Planejamentos acertivos')
                    st.info("Os indicadores de desempenho são os responsáveis por ajudar você a atingir suas metas e objetivos.")
                    worksheet_d = 'Desempenho do Processo 2021'
                    sheet_d = 'Planejamento'
                    df_desempenho = leitor(worksheet_d, sheet_d)
                    check_desempenho = st.checkbox('Selecione para ver os indicadores de desempenho do processo.')
                    if check_desempenho == 1:
                        desempenho = desempenho_plan_proj(df_desempenho)
                        st.table(desempenho)
                        check1_d = st.checkbox((list(df_desempenho.iloc[38])[0]).title() + " - Desempenho")
                        if check1_d == 1:
                            st.write(list(df_desempenho.iloc[39])[0])
                        check2_d = st.checkbox((list(df_desempenho.iloc[40])[0]).title() + " - Desempenho")
                        if check2_d == 1:
                            st.write(list(df_desempenho.iloc[41])[0])
                        check3_d = st.checkbox((list(df_desempenho.iloc[42])[0]).title() + " - Desempenho")
                        if check3_d == 1:
                            st.write(list(df_desempenho.iloc[43])[0])

                if choice == 'Projetos':
                    worksheet = 'Plano de Objetivos e Metas 2021 (Revisão 01 Readequação devido término do contrato da Copel)'
                    sheet = choice
                    df = leitor(worksheet, sheet)
                    st.markdown("<h4 style='text-align: center; color: black'>Plano de Objetivos e Metas</h4", unsafe_allow_html=True)
                    st.markdown('----')
                    st.markdown('**Indicador:** Entregas executadas x Entregas planejadas')
                    ind = indicador(df)
                    mask = ind['Entregas Plan']!=''
                    ind = ind.drop(columns=[''])
                    st.table(ind[mask])
                    check1t = st.checkbox((list(df.iloc[24])[0]).title())
                    if check1t == 1:
                        st.write(list(df.iloc[25])[0])
                    check2t = st.checkbox((list(df.iloc[26])[0]).title())
                    if check2t == 1:
                        st.write(list(df.iloc[27])[0])
                    check3t = st.checkbox((list(df.iloc[28])[0]).title())
                    if check3t == 1:
                        st.write(list(df.iloc[29])[0])
                    check4t = st.checkbox((list(df.iloc[30])[0]).title())
                    if check4t == 1:
                        st.write(list(df.iloc[31])[0])
                    st.markdown('----')
                    st.markdown("<h4 style='text-align: center; color: black'>Desempenho</h4", unsafe_allow_html=True)

                if choice == 'Comercial':
                    worksheet = 'Plano de Objetivos e Metas 2021 (Revisão 01 Readequação devido término do contrato da Copel)'
                    sheet = choice
                    df = leitor(worksheet, sheet)
                    st.markdown("<h4 style='text-align: center; color: black'>Plano de Objetivos e Metas</h4", unsafe_allow_html=True)
                    st.markdown('----')
                    st.markdown('**Indicador:** Comercial')
                    ind = indicador(df)
                    ind = ind.drop(columns=[''])
                    st.table(ind)
                    check1t = st.checkbox((list(df.iloc[24])[0]).title())
                    if check1t == 1:
                        st.write(list(df.iloc[25])[0])
                    check2t = st.checkbox((list(df.iloc[26])[0]).title())
                    if check2t == 1:
                        st.write(list(df.iloc[27])[0])
                    check3t = st.checkbox((list(df.iloc[28])[0]).title())
                    if check3t == 1:
                        st.write(list(df.iloc[29])[0])
                    check4t = st.checkbox((list(df.iloc[30])[0]).title())
                    if check4t == 1:
                        st.write(list(df.iloc[31])[0])                    

                if choice == 'RH': 
                    worksheet = 'Plano de Objetivos e Metas 2021 (Revisão 01 Readequação devido término do contrato da Copel)'
                    sheet = choice
                    df = leitor(worksheet, sheet)
                    st.markdown("<h4 style=' text-align: center; color: black'>Plano de Objetivos e Metas</h4", unsafe_allow_html=True)
                    st.markdown('**Indicador:** Absenteísmo')
                    ind = indicador(df)
                    st.table(ind)
                    st.info("""
                            Absenteísmo é a falta de pontualidade e assiduidade e está relacionado a faltas e ou atrasos do colaborador. 
                            """)
                    check1 = st.checkbox((list(df.iloc[24])[0]).title())
                    if check1 == 1:
                        st.write(list(df.iloc[25])[0])
                    check2 = st.checkbox((list(df.iloc[26])[0]).title())
                    if check2 == 1:
                        st.write(list(df.iloc[27])[0])
                    check3 = st.checkbox((list(df.iloc[28])[0]).title())
                    if check3 == 1:
                        st.write(list(df.iloc[29])[0])
                    check4 = st.checkbox((list(df.iloc[30])[0]).title())
                    if check4 == 1:
                        st.write(list(df.iloc[31])[0])  
                    st.markdown('----')
                    st.markdown("<h4 style=' text-align: center; color: black'>Desempenho</h4", unsafe_allow_html=True)
                    st.markdown('**Indicador de Desempenho:** Turnover')
                    st.info("Os indicadores de desempenho são os responsáveis por ajudar você a atingir suas metas e objetivos.")
                    worksheet_d = 'Desempenho do Processo 2021_Readequação_4º Trimestre'
                    sheet_d = 'RH'
                    df_desempenho = leitor(worksheet_d, sheet_d)
                    check_desempenho = st.checkbox('Selecione para ver os indicadores de desempenho do processo.')
                    if check_desempenho == 1:
                        desempenho = desempenho_instalação_rh(df_desempenho)
                        st.table(desempenho)
                        check1_d = st.checkbox((list(df_desempenho.iloc[29])[0]).title() + " - Desempenho")
                        if check1_d == 1:
                            st.write(list(df_desempenho.iloc[30])[0])
                        check2_d = st.checkbox((list(df_desempenho.iloc[31])[0]).title() + " - Desempenho")
                        if check2_d == 1:
                            st.write(list(df_desempenho.iloc[32])[0])
                        check3_d = st.checkbox((list(df_desempenho.iloc[33])[0]).title() + " - Desempenho")
                        if check3_d == 1:
                            st.write(list(df_desempenho.iloc[34])[0])
                        check4_d = st.checkbox((list(df_desempenho.iloc[35])[0]).title() + " - Desempenho")
                        if check4_d == 1:
                            st.write(list(df_desempenho.iloc[36])[0])

                if choice == 'Controle de Qualidade':
                    worksheet = 'Plano de Objetivos e Metas 2021 (Revisão 01 Readequação devido término do contrato da Copel)'
                    sheet = choice
                    df = leitor(worksheet, sheet)
                    st.markdown("<h4 style=' text-align: center; color: black'>Plano de Objetivos e Metas</h4", unsafe_allow_html=True)
                    st.markdown("**Indicador:** Número de reclamações / avaliações negativas (instalador) x Número de ativações ")
                    ind = indicador(df)
                    st.table(ind)
                    check1t = st.checkbox((list(df.iloc[23])[0]).title())
                    if check1t == 1:
                        st.write(list(df.iloc[24])[0])
                    # Avaliação segundo trimestre
                    check2t = st.checkbox((list(df.iloc[25])[0]).title())
                    if check2t == 1:
                        st.write(list(df.iloc[26])[0])
                    # Avaliação terceiro trimestre
                    check3t = st.checkbox((list(df.iloc[27])[0]).title())
                    if check3t == 1:
                        st.write(list(df.iloc[28])[0])
                    # Avaliação quarto trimestre
                    check4t = st.checkbox((list(df.iloc[29])[0]).title())
                    if check4t == 1:
                        st.write(list(df.iloc[30])[0])

                if choice == 'Seg. do Trabalho':
                    worksheet = 'Plano de Objetivos e Metas 2021 (Revisão 01 Readequação devido término do contrato da Copel)'
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
                    # Avaliação terceiro trimestre
                    check4t = st.checkbox('4º Trimestre/2021')
                    if check4t == 1:
                        st.markdown('**'+list(df.iloc[30])[0]+'**')
                        st.write(list(df.iloc[31])[0])
                    st.markdown('**Indicador:** Seg. do Trabalho')
                    ind = indicador(df)
                    st.table(ind)

                if choice == 'Fechamento (descontinuado)':
                    worksheet = 'Plano de Objetivos e Metas 2021'
                    sheet = 'Fechamento'
                    df = leitor(worksheet, sheet)
                    st.markdown("<h4 style=' text-align: center; color: black'>Plano de Objetivos e Metas</p", unsafe_allow_html=True)
                    st.error('Com a readequação ocorrida na empresa, este processo foi descontinuado para o 4º trimestre e para o ano vigente.')
                    st.markdown('**Indicador:** "Número de ativações aprovadas no mês x Número de ativações realizadas no mês anterior"')
                    ind = indicador(df)
                    mask = ind["Ativações aprovadas"] != ''
                    st.table(ind[mask])
                    check1t = st.checkbox((list(df.iloc[24])[0]).title())
                    if check1t == 1:
                        st.write(list(df.iloc[25])[0])
                    check2t = st.checkbox((list(df.iloc[26])[0]).title())
                    if check2t == 1:
                        st.write(list(df.iloc[27])[0])
                    check3t = st.checkbox((list(df.iloc[28])[0]).title())
                    if check3t == 1:
                        st.write(list(df.iloc[29])[0])

                if choice == 'Manutenção (descontinuado)':
                    sheet = 'Manutenção'
                    worksheet = 'Plano de Objetivos e Metas 2021'
                    df = leitor(worksheet, sheet)
                    st.info('Com a readequação ocorrida na empresa, este processo foi descontinuado para o 4º trimestre e para o ano vigente.')
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


        if year == '2022':
            st.markdown('Aguardando a definição.')

if option == 'Desempenho':
    st.image(header_desempenho, caption=None, width=650)
    year = st.selectbox('Selecione o ano desejado: ',('Selecione','2021','2022'))
    if year != "Selecione":
        if year == '2021':
            st.warning("""
            O desempenho de um processo \n
            Foram então remodelados os indicadores de desempenho de alguns processos atendendo as novas demandas da empresa.""")
            st.markdown('----')
            st.markdown("----")
            choice = st.selectbox('Selecione o processo para visualizar: ', ('Selecione'))
                        # Plano de Objetivos e Metas 2021 (Revisão 01 Readequação devido término do contrato da Copel)
            if choice != 'Selecione':
                
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