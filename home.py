import streamlit as st # type: ignore
from graphic import create_performance_analysis_plot
from forms import show_investment_form, show_cliques_form, show_leads_form
from email_utils import send_analysis_email
from info_texts import get_analysis_text

st.set_page_config(page_title="Performate")

st.title("Bem-vindo(a) ao Performate :wave:")

st.subheader("Preencha suas Métricas:")
col1, col2, col3 = st.columns(3)

# Inicializa as variáveis fora do escopo dos formulários
resultado = st.session_state.get('resultado', None)
lead_media = st.session_state.get('lead_media', None)
investimento = st.session_state.get('investimento', None)

# Formulários
number_invest_cli = show_investment_form(col1)
resultado = show_cliques_form(col2, number_invest_cli)
lead_media = show_leads_form(col3, number_invest_cli)

# Análise final
if resultado is not None and lead_media is not None:
    st.header("Análise final")
    investimento_diario = number_invest_cli / 30
    cliques_diario = resultado / 30
    leads_diario = lead_media / 30

    analysis_text = get_analysis_text(number_invest_cli, resultado, lead_media, investimento_diario, cliques_diario, leads_diario)
    st.markdown(analysis_text, unsafe_allow_html=True)

    fig = create_performance_analysis_plot(number_invest_cli, investimento_diario, resultado, cliques_diario, leads_diario, lead_media)
    st.plotly_chart(fig)

    # Input do email e botão de envio
    email = st.text_input("Digite o email do destinatário:")
    send_email = st.button("Enviar Análise por Email")

    if send_email and email:
        send_analysis_email(email, analysis_text, number_invest_cli, resultado, lead_media, investimento_diario, cliques_diario, leads_diario)

# Adiciona o CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
