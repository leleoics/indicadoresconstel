import streamlit as st
import pandas as pd
from PIL import Image
from functions import leitor, indicador, desempenho_manutencao, desempenho_instalação_rh
from functions import desempenho_almoxarifado, desempenho_plan_proj, desempenho_seg_trabalho
import streamlit.components.v1 as components
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


logo_C = Image.open("./LogoC.png")
logo_Capa = Image.open("./Logo_C_capa.png")
header = Image.open("./header.png")
logo_Cinza = Image.open("./Logo_Site.png")
fluxograma = Image.open("./Fluxograma.jpg")
contigencia = open("planodecontingencia.pdf")
organograma = open("organograma.pdf")
legend_site_emandamento = Image.open("./legenda_site_em_andamento.png")
legend_site_aguardando = Image.open("./legenda_site_aguardando.png")


# Barra lateral
st.sidebar.image(logo_C, caption=None, width=75)
st.sidebar.title('**Constel Engenharia Elétrica**')

option = st.sidebar.selectbox('Selecione a página desejada', ["Início", "Atuação", "Gestão da Qualidade", "Sobre"])

if option == "Início":
    # Página inicial
    st.image(header, caption=None, width=800)
    st.header('**Bem vindo!**')
    st.markdown('Nesta plataforma você encontrará os indicadores do Plano de Objetivos e Metas e o desempenho dos processos da Constel')
    st.markdown('Clique na aba lateral para navegar pelo site')
    # pwd = st.text_input ("Senha: ", type ="password")
    # if pwd == id:
    #     st.write('Acesso liberado para colaborador interno')
    #     nivel_acesso = 1
    # if pwd == '':
    #     st.write('Digite a senha')
    # if pwd != id:
    #     st.write('Senha incorreta!')

if option == "Atuação":
    worksheet = option
    choice = st.sidebar.selectbox('Selecione a área de atuação', ['Selecione', 'Huawey'])
    if choice == 'Huawey':
        st.markdown('**Instalação WL**')
        check1 = st.checkbox('Mostrar estatísticas:')
        if check1 == 1:
            sheet = "Dados"
            df = leitor(worksheet, sheet)
            st.markdown('**Status dos Sites**')
            df2 = df.T
            s_concluido = df2[2][1]
            s_andamento = df2[3][1]
            s_mos = df2[4][1]
            s_agint = df2[5][1]
            t_mes = df2[6][1]
            # Imprime o status Concluído 
            st.markdown('*' + list(df.iloc[2])[0]+ '*' + ': ' + s_concluido)
            # Imprime o status Em andamento 
            st.markdown('*' + list(df.iloc[3])[0]+ '*' + ': ' + s_andamento)
            # Imprime o status Entrega do material 
            st.markdown('*' + list(df.iloc[4])[0]+ '*' + ': ' + s_mos)
            # Imprime o status Aguardando início 
            st.markdown('*' + list(df.iloc[5])[0]+ '*' + ': ' + s_agint)
            # Imprime a quantidade mês
            st.markdown('*' + list(df.iloc[6])[0]+ '*' + ': ' + t_mes)
     
        check2 = st.checkbox('Ver no mapa:')
        if check2 == 1:
            components.iframe(src="https://www.google.com/maps/d/u/0/embed?mid=1r6xzmsAeiSD3cniV-oXD_MWHGMPyYVZ8", width=640, height=480)
            st.markdown("**Simbologia do mapa**")
            st.write("Em andamento: ")
            st.image(legend_site_emandamento, width=30, )
            st.write("Aguardando início: ")
            st.image(legend_site_aguardando, width=30)
        
    
        sheet = "Instalação WL"
        df = leitor(worksheet, sheet)
        # Alterar cabeçalho para primeira linha e excluir   
        df.columns = df.iloc[0]
        df = df.drop(df.index[0])
        fig, ax =plt.subplots(figsize=(12,4))
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
        pp = PdfPages("foo.pdf")
        pp.savefig(fig, bbox_inches='tight')
        pp.close()
        st.markdown('**Baixar relatório de instalação WL**')
        with open('foo.pdf', 'rb') as f:
            st.download_button('Baixar', f, file_name='Relatório Instalação WL.pdf')
            
    else:
        st.image(logo_Capa, caption=None, width=150)
        st.markdown("Nesta aba é possível visualizar as diversas frentes de atuação da empresa, conferindo estatísticas e mapas")

if option == "Gestão da Qualidade":
    option2 = st.sidebar.selectbox('Selecione a página desejada', ['Selecione', 'Indicadores', 'Desempenho', 'Documentos'])
    if option2 == 'Documentos':
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


    if option2 == 'Desempenho':
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


    if option2 == 'Indicadores':
        st.markdown('Nesta aba é possível visualizar os indicadores dos setores da empresa.')
        choice = st.selectbox('Escolha o setor: ',('Selecione', 'Instalação', 'Manutenção','Planejamento','Comercial','Controle de Qualidade', 
        'Seg. do Trabalho', 'Fechamento', 'Projetos', 'RH', 'Financeiro', 'Compras'))
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
