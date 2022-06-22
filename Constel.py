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
    <p class="card-text">Para navegar entre as abas, expanda o menu de seleção e selecione a página desejada</p>
  </div>
</div>
"""

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

#CABEÇALHO COM ACESSO AOS APPs
st.markdown("----")
menu = st.expander("- Menu de seleção",expanded=False)
with menu:
    st.image(logo_Capa, width=75)
    pagina = st.radio(
        "Selecione a página: ",
        ("Início", "Formulários","Indicadores", "Documentos", "Sobre"))
st.markdown("----")



# # Barra lateral
# st.sidebar.image(logo_C, caption=None, width=75)
# st.sidebar.title('**Constel Engenharia Elétrica**')
# option = st.sidebar.selectbox('Selecione a página desejada', ["Início", "Formulários","Indicadores", "Documentos", "Sobre"])

# Abas da aplicação
if pagina == "Início":
    # Página inicial
    # st.image(header, caption=None, use_column_width=True)
    col11, col12 = st.columns([1, 1])
    with col11:
        st.markdown("<h4 style='text-align: left; color: black;'>Apresentação</h4>", unsafe_allow_html=True)
        st.markdown(" ")
        components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTU0773TwwYa249dB9ZbieogaeK8g2h_wlE-fghJvK4V0DTPcWxzzosx-jKO7tNvWJzE-RNCNvsn_ka/embed?start=false&loop=false&delayms=3000", width=400, height=295)   

    with col12:
        st.markdown("<h4 style='text-align: left; color: black;'>Aniversariantes do mês</h4>", unsafe_allow_html=True)
        st.markdown(" ")
        components.iframe("https://docs.google.com/spreadsheets/d/e/2PACX-1vRVvM6x4YULHM3MGUYQxDcCS0BgF6xB6p-e2WXnH91joME173m8_Nn1QB9ws7qT3fxCFqqN2B7cAq0_/pubhtml?widget=true&amp;headers=false", width=400, height=500)
    st.markdown(texto_inicial(),unsafe_allow_html=True)
                 


    # st.markdown("<h3 style='text-align: center; color: black;'>Bem vindo!</h3>", unsafe_allow_html=True)
    st.markdown("----")
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
    st.markdown("<h3 style='text-align: center; color: black;'>Formulários</h3>", unsafe_allow_html=True)       
    st.markdown("----")
    avaliation = st. selectbox('Selecione a avaliação:', ('Selecione','Avaliação 1', 'Avaliação 2'))
    if avaliation != 'Selecione':
        if avaliation == 'Avaliação 1':
            components.iframe("https://docs.google.com/forms/d/e/1FAIpQLSeoJkyF1mkJIeA9kcrKGHswg68SGcEYjGc4i4kKKoZXieIxKw/viewform?embedded=true", width=860, height=4000)
        else:
            components.iframe("https://docs.google.com/forms/d/e/1FAIpQLScZ0VeavfUM2rWkwKkjhCXpVgvPRbs4M3A8a89lV0k4ranKMw/viewform?embedded=true", width=860, height=4200)
        st.markdown("---")
    else:
        st.markdown("<p style=' text-align: center; color: black'>Nesta seção é possível encontrar avaliações relacionadas ao Sistema de Gestão da Qualidade.</p>", unsafe_allow_html=True)

if pagina == 'Indicadores':
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
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTgk6GSKylyIMLmGXGWqHMzAwI1yrT3t-Zc4WGQn2q_HVlAVYzDBcHimceZa4tPe48kG5NVhv_id8su/embed?start=false&loop=false&delayms=3000", width=797, height=486)
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTU0773TwwYa249dB9ZbieogaeK8g2h_wlE-fghJvK4V0DTPcWxzzosx-jKO7tNvWJzE-RNCNvsn_ka/embed?start=false&loop=false&delayms=3000", width=797, height=486)                    


                if choice == 'Instalação de Prumadas':
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTgk6GSKylyIMLmGXGWqHMzAwI1yrT3t-Zc4WGQn2q_HVlAVYzDBcHimceZa4tPe48kG5NVhv_id8su/embed?start=false&loop=false&delayms=3000", width=797, height=486)
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTU0773TwwYa249dB9ZbieogaeK8g2h_wlE-fghJvK4V0DTPcWxzzosx-jKO7tNvWJzE-RNCNvsn_ka/embed?start=false&loop=false&delayms=3000", width=797, height=486)                    


                if choice == 'Instalação (Instalação de Internet)':
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTgk6GSKylyIMLmGXGWqHMzAwI1yrT3t-Zc4WGQn2q_HVlAVYzDBcHimceZa4tPe48kG5NVhv_id8su/embed?start=false&loop=false&delayms=3000", width=797, height=486)
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTU0773TwwYa249dB9ZbieogaeK8g2h_wlE-fghJvK4V0DTPcWxzzosx-jKO7tNvWJzE-RNCNvsn_ka/embed?start=false&loop=false&delayms=3000", width=797, height=486)                    
    

                if choice == 'Planejamento':
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTgk6GSKylyIMLmGXGWqHMzAwI1yrT3t-Zc4WGQn2q_HVlAVYzDBcHimceZa4tPe48kG5NVhv_id8su/embed?start=false&loop=false&delayms=3000", width=460, height=295)
                    # components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTU0773TwwYa249dB9ZbieogaeK8g2h_wlE-fghJvK4V0DTPcWxzzosx-jKO7tNvWJzE-RNCNvsn_ka/embed?start=false&loop=false&delayms=3000", width=797, height=486)                    


                if choice == 'Projetos':
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTgk6GSKylyIMLmGXGWqHMzAwI1yrT3t-Zc4WGQn2q_HVlAVYzDBcHimceZa4tPe48kG5NVhv_id8su/embed?start=false&loop=false&delayms=3000", width=797, height=486)
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTU0773TwwYa249dB9ZbieogaeK8g2h_wlE-fghJvK4V0DTPcWxzzosx-jKO7tNvWJzE-RNCNvsn_ka/embed?start=false&loop=false&delayms=3000", width=797, height=486)                    


                if choice == 'Comercial':
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTgk6GSKylyIMLmGXGWqHMzAwI1yrT3t-Zc4WGQn2q_HVlAVYzDBcHimceZa4tPe48kG5NVhv_id8su/embed?start=false&loop=false&delayms=3000", width=797, height=486)
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTU0773TwwYa249dB9ZbieogaeK8g2h_wlE-fghJvK4V0DTPcWxzzosx-jKO7tNvWJzE-RNCNvsn_ka/embed?start=false&loop=false&delayms=3000", width=797, height=486)                    
                  

                if choice == 'RH': 
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTgk6GSKylyIMLmGXGWqHMzAwI1yrT3t-Zc4WGQn2q_HVlAVYzDBcHimceZa4tPe48kG5NVhv_id8su/embed?start=false&loop=false&delayms=3000", width=797, height=486)
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTU0773TwwYa249dB9ZbieogaeK8g2h_wlE-fghJvK4V0DTPcWxzzosx-jKO7tNvWJzE-RNCNvsn_ka/embed?start=false&loop=false&delayms=3000", width=797, height=486)                    


                if choice == 'Controle de Qualidade':
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTgk6GSKylyIMLmGXGWqHMzAwI1yrT3t-Zc4WGQn2q_HVlAVYzDBcHimceZa4tPe48kG5NVhv_id8su/embed?start=false&loop=false&delayms=3000", width=797, height=486)
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTU0773TwwYa249dB9ZbieogaeK8g2h_wlE-fghJvK4V0DTPcWxzzosx-jKO7tNvWJzE-RNCNvsn_ka/embed?start=false&loop=false&delayms=3000", width=797, height=486)                    


                if choice == 'Seg. do Trabalho':
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTgk6GSKylyIMLmGXGWqHMzAwI1yrT3t-Zc4WGQn2q_HVlAVYzDBcHimceZa4tPe48kG5NVhv_id8su/embed?start=false&loop=false&delayms=3000", width=797, height=486)
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTU0773TwwYa249dB9ZbieogaeK8g2h_wlE-fghJvK4V0DTPcWxzzosx-jKO7tNvWJzE-RNCNvsn_ka/embed?start=false&loop=false&delayms=3000", width=797, height=486)                    


                if choice == 'Fechamento (descontinuado)':
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTgk6GSKylyIMLmGXGWqHMzAwI1yrT3t-Zc4WGQn2q_HVlAVYzDBcHimceZa4tPe48kG5NVhv_id8su/embed?start=false&loop=false&delayms=3000", width=797, height=486)
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTU0773TwwYa249dB9ZbieogaeK8g2h_wlE-fghJvK4V0DTPcWxzzosx-jKO7tNvWJzE-RNCNvsn_ka/embed?start=false&loop=false&delayms=3000", width=797, height=486)                    


                if choice == 'Manutenção (descontinuado)':
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTgk6GSKylyIMLmGXGWqHMzAwI1yrT3t-Zc4WGQn2q_HVlAVYzDBcHimceZa4tPe48kG5NVhv_id8su/embed?start=false&loop=false&delayms=3000", width=797, height=486)
                    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTU0773TwwYa249dB9ZbieogaeK8g2h_wlE-fghJvK4V0DTPcWxzzosx-jKO7tNvWJzE-RNCNvsn_ka/embed?start=false&loop=false&delayms=3000", width=797, height=486)                    


        if year == '2022':
            st.markdown("----")
            st.markdown("<p style=' text-align: justify; color: black'>Aguardando preenchimento...</p>", unsafe_allow_html=True)
            st.markdown("----")
                        
if pagina == 'Documentos':
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

if pagina == "Sobre":
    st.markdown('**Autor:** Leonardo de Oliveira Melo')
    st.markdown('**Formação:** Graduando em Eng. Cartógrafica e de Agrimensura')
    st.markdown('**Instituição:** Universidade Federal do Paraná')
    st.markdown('**Linkedin:** https://www.linkedin.com/in/leonardo-oliveira-melo-287593164/')
    st.markdown('**Projeto:** Desenvolver plataforma com os indicadores da Constel')
    st.markdown('**Status:** Em desenvolvimento.')
    st.image(logo_Capa, caption=None, width=150)