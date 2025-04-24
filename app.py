import streamlit as st
import requests

st.set_page_config(page_title="QuantumLine - Arena QuIIN 2025", page_icon="🔢", layout="centered")

st.markdown("""
    <style>
        .stApp {
            background-color: #e6f0ff;
        }
        .title-style {
            text-align: center;
            font-size: 2em;
            font-weight: bold;
        }
        .subtitle-style {
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 20px;
        }
        .footer-style {
            text-align: center;
            font-size: 0.9em;
            color: #666;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-style">QuantumLine - Arena QuIIN 2025</div>
<div class="subtitle-style">
    Desafio: Geradores Quânticos de Números Aleatórios para Instituições Financeiras<br>
    Nome do Projeto: QuantumLine<br>
    Time do Projeto: Equipe 13 – Shirley Maria, Rafael Bittencourt, Cristian Griebler
</div>
""", unsafe_allow_html=True)

st.image("https://i.imgur.com/FKX6NkI.png", width=150)

st.header("Validador de Saques com Números Quânticos")

if st.button("Gerar e validar número quântico"):
    response = requests.get("https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint8")
    if response.status_code == 200:
        numero = response.json()['data'][0]
        st.success(f"Número quântico gerado: {numero}")

        if numero % 2 == 0:
            st.markdown("✅ **Saque aprovado automaticamente.**")
        else:
            st.markdown("⚠️ **Saque enviado para análise manual.**")
    else:
        st.error("Erro ao acessar a API de números quânticos da ANU.")

st.markdown("""
<div class="footer-style">
    © 2025 Equipe 13 - Projeto QuantumLine - Arena QuIIN
</div>
""", unsafe_allow_html=True)
