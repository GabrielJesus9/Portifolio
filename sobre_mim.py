import streamlit as st

coluna1, coluna2 = st.columns(2, gap='small', vertical_alignment='center')

with coluna1:
    st.image("images.png", width=230)
with coluna2:
    st.title("Gabriel Jesus", anchor=False)
    st.write("Analista de dados com experiência em manipulação e visualização de dados, focado em extrair insights e otimizar processos de tomada de decisão usando ferramentas como Python, SQL, Power BI e Excel.")


st.write('\n')
st.subheader("Experiência", anchor=False)
st.write('''
         Dental Cremer - Analista de dados''' )
st.write('01-11-2024 - até o momento')
st.write('''
        - Criação e reporte de dados estratégicos de duas filiais
        - Automação de processos utilizando webscraping e pyautogui
        - Automação de planilhas utilizando pandas e VBA
        - Extração de dados utilizando SQL nos bancos de dados internos (PostegreSQL, Databricks e SQLserver)
        - Criação de Formulários utilizando C#
        - Criação de Dashboards web utilizando Dash e Streamlit
        - Criação de dashboards utilizando Power BI
        - Tratamento de grandes volumes de dados utilizando pyspark
        - Criação de modelos de machine learning utilizando Scikit-learn e calculos com numpy
''')

st.subheader("Educação", anchor=False)

st.write('- Tecnico em tecnologia da informação - Etec Parque da juventude (01-01-2016 - 01-12-2019)')
st.write('- Graduação Ciências da computação - Faculdade das américas (01-01-2023 - 01-01-2027)')

st.subheader("Cursos", anchor=False)

st.write('''
    - Python - Hashtag Treinamentos
    - SQL - Hashtag Treinamentos
    - Python para data science - Data science academy
    - Fundamentos databricks - Databricks Academy
    - Power Bi - Hashtag treinamentos
''')

st.subheader('Habilidades')
st.write('''
        - Python 
        - SQL (Databricks, PostegreSQL e SQLserver)
        - Power BI
        - VBA
        - C#
        - Power automate
        - Excel
''')