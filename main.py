import streamlit as st

pg = st.navigation( [st.Page("sobre_mim.py", title= 'Sobre mim', default=True),
                    st.Page("Projetos.py", title= 'Projetos', default=False),
                    st.Page("artigos.py", title= 'Artigos', default=False),
                    st.Page("conteudo.py", title= 'Conteúdos', default=False)]
)

pg.run()