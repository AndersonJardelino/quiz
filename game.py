import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="Quiz Corporativo", page_icon="🧠", layout="centered")

st.title("🧠 Quiz de Conhecimentos")

# Entrada do nome
nome = st.text_input("Digite seu nome para começar:")

if nome:
    st.write(f"👋 Olá, *{nome}*! Responda às perguntas abaixo:")

    pontuacao = 0

    # Pergunta 1
    q1 = st.radio("1️⃣ Qual linguagem é usada para criar esse quiz?", 
                  ["Java", "Python", "C++"])
    if q1 == "Python":
        pontuacao += 1

    # Pergunta 2
    q2 = st.radio("2️⃣ Qual dessas bibliotecas é usada para visualização de dados?", 
                  ["NumPy", "Pandas", "Matplotlib"])
    if q2 == "Matplotlib":
        pontuacao += 1

    # Pergunta 3
    q3 = st.radio("3️⃣ O que é Streamlit?", 
                  ["Um framework de backend", "Uma ferramenta de visualização", "Uma biblioteca para apps interativos em Python"])
    if q3 == "Uma biblioteca para apps interativos em Python":
        pontuacao += 1

    if st.button("Enviar respostas"):
        st.success(f"✅ {nome}, sua pontuação foi: {pontuacao}/3")
        if pontuacao == 3:
            st.balloons()
            st.info("🎉 Parabéns! Você foi muito bem!")
        elif pontuacao == 2:
            st.warning("👏 Bom resultado! Mas pode melhorar.")
        else:
            st.error("💡 Continue estudando e tente novamente!")