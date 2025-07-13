import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="Quiz Iroudas", page_icon="❤️", layout="centered")

st.title("❤️ Quiz de Conhecimentos sobre Anderson")

# Entrada do nome
nome = st.text_input("Digite seu nome para começar:")

if nome:
    st.write(f"👋 Olá, *{nome}*! Responda às perguntas abaixo:")

    pontuacao = 0

    # Pergunta 1
    q1 = st.radio("1️⃣ Qual cidade do seu nascimento?", 
                  ["Rio de Janeiro", "Campina Grande", "João Pessoa"])
    if q1 == "Campina Grande":
        pontuacao += 1

    # Pergunta 2
    q2 = st.radio("2️⃣ Qual a cor preferida dele?", 
                  ["Rosa", "Verde", "Azul marinho"])
    if q2 == "Azul marinho":
        pontuacao += 1

    # Pergunta 3
    q3 = st.radio("3️⃣ Quanto ele calça?", 
                  ["43", "42", "38"])
    if q3 == "42":
        pontuacao += 1

    if st.button("Enviar respostas"):
        st.success(f"✅ {nome}, sua pontuação foi: {pontuacao}/3")
        if pontuacao == 3:
            st.balloons()
            st.info("🎉 Parabéns! Você realmente conhece ele.")
        elif pontuacao == 2:
            st.warning("👏 Bom resultado! Mas pode melhorar.")
        else:
            st.error("💡 Abre o olho, Ioudas")