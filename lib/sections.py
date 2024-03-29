import requests
import streamlit as st
from streamlit_lottie import st_lottie


class Sections:
    def __init__(self) -> None:
        pass

    def load_lottieurl(self, url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None

        return r.json()

    def header(self):
        _, col_header1, col_header2 = st.columns((0.4, 2.0, 2.0))
        with col_header1:
            lottie_world = self.load_lottieurl(
               "https://assets10.lottiefiles.com/packages/lf20_n7eytpy8.json"
            )
            st_lottie(lottie_world, speed=1, height=200)

        with col_header2:
            lottie_book = self.load_lottieurl(
                "https://assets10.lottiefiles.com/packages/lf20_i9mtrven.json"
            )
            st_lottie(lottie_book, speed=1, height=200, key="initial")

        return None

    def hello_card():
        _, row0_1, _, row0_2, _ = st.columns((0.1, 2, 0.2, 1, 0.1))

        row0_1.title("World Happiness")
        with row0_2:
            st.write("")

        row0_2.subheader(
            "A Web App by [Jeová Ramos](https://github.com/jeovaramos)"
        )

        col1_spacer1, row1_1, row1_spacer2 = st.columns((3.0, 2.0, 2.5))

        col1_spacer1.markdown(
            "Oi, tudo bem? Este é o produto de dados, resultado de um "
            "projeto pessoal. Aqui estou trazendo somente a visualização dos "
            "principais resultados. "
            "Não deixe de conferir o [relatório de resultados]"
            "(https://docs.google.com/document/d/1yYwSWtm4WC0OuR-4VREUkzJ"
            "p3iORV3rBGOyZmN1H_-8/edit?usp=sharing) para conferir as "
            "motivações e discussões dos mesmos. "
            "Confira também o [relatório de atividades](https://docs.google."
            "com/document/d/1-fdSSZdLONQsEqbWauxyfFhzOCtKa0i2Ru-Gi43Pzzc/edit"
            "?usp=sharing) e o [repositório](https://github.com/jeovaramos/"
            "world_happiness) do projeto para entender o processo de "
            "desenvolvimento."
        )

        row1_spacer2.markdown(
            "Cientista de dados, mestre em meteorologia pela USP e "
            "amante de música esquisita. Experiencia em engenharia de "
            "software, modelagem numérica, testes estatísticos e "
            "análise de dados. "
            "**Espero que goste.**"
        )

        return None
