
import streamlit as st
import plotly.express as px
import pandas as pd

if 'progresso' not in st.session_state:
    st.session_state['progresso'] = {'Respiração': 0, 'Frio': 0, 'Mente': 0}

if 'qa_list' not in st.session_state:
    st.session_state['qa_list'] = []

st.title("🌬️ Método Wim Hof - App em Python")

st.header("✅ Protocolos Práticos")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Respiração"):
        st.session_state['progresso']['Respiração'] += 1
        st.info("Respiração: Inspire fundo 30x, prenda, solte, repita 3x.")

with col2:
    if st.button("Frio"):
        st.session_state['progresso']['Frio'] += 1
        st.info("Frio: Termine o banho com 30s de água fria, aumente aos poucos.")

with col3:
    if st.button("Mente"):
        st.session_state['progresso']['Mente'] += 1
        st.info("Mente: Medite antes da prática, visualize seu sucesso.")

st.header("❓ Tire sua Dúvida")

pergunta = st.text_input("Digite sua pergunta:")

if st.button("Responder"):
    resposta = ""
    if "frio" in pergunta.lower():
        resposta = "A exposição ao frio fortalece sua imunidade."
    elif "respiração" in pergunta.lower():
        resposta = "A respiração oxigena e regula o pH do corpo."
    elif "mente" in pergunta.lower():
        resposta = "Foco mental é essencial para superar limites."
    else:
        resposta = "Explore o livro para respostas mais profundas!"

    st.session_state['qa_list'].append({'pergunta': pergunta, 'resposta': resposta})
    st.success(resposta)

st.header("🗂️ Perguntas Salvas")

if st.session_state['qa_list']:
    for i, item in enumerate(st.session_state['qa_list']):
        st.write(f"**{i+1}.** {item['pergunta']} ➡️ {item['resposta']}")
else:
    st.write("Nenhuma pergunta ainda.")

st.header("📊 Seu Progresso")

df = pd.DataFrame({
    'Protocolo': list(st.session_state['progresso'].keys()),
    'Práticas': list(st.session_state['progresso'].values())
})

fig = px.bar(df, x='Protocolo', y='Práticas', color='Protocolo', text='Práticas')
st.plotly_chart(fig, use_container_width=True)

total = sum(st.session_state['progresso'].values())
if total < 5:
    nivel = "Iniciante"
elif total < 15:
    nivel = "Intermediário"
else:
    nivel = "Avançado"

st.subheader(f"🏅 Nível: {nivel}")
