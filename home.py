import streamlit as st
import plotly.graph_objects as go
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

st.set_page_config(page_title="Performate")

st.title("Bem-vindo(a) ao Performate :wave:")

st.subheader("Preencha suas Métricas:")
col1, col2 = st.columns(2)

# Inicializa as variáveis fora do escopo dos formulários
resultado = st.session_state.get('resultado', None)
lead_media = st.session_state.get('lead_media', None)

with col1:
    st.header("Cliques:")
    form_cal_cli = st.form(key="Cliques", clear_on_submit=False)
    with form_cal_cli:
        number_invest_cli = st.number_input("Digite a média de investimento Mensal:", key="invest_cli")
        number_cpc = st.number_input("Digite o CPC Médio:", key="cpc")
        
        # Botão de envio sempre visível
        button_click_cli = st.form_submit_button('Veja o resultado')
        
        # Calcula o resultado apenas se os campos estiverem preenchidos
        if button_click_cli and number_invest_cli > 0 and number_cpc > 0:
            resultado = number_invest_cli / number_cpc
            st.session_state['resultado'] = resultado
            st.write("O seu número de cliques será aproximadamente:", round(resultado))

with col2:
    st.header("Leads:")
    form_cal_lead = st.form(key="Leads", clear_on_submit=False)
    with form_cal_lead:
        number_invest_lead = st.number_input("Digite a média de investimento Mensal", key="invest_lead")
        number_cpa = st.number_input("Digite o CPA Médio:", key="cpa")
        
        # Botão de envio sempre visível
        button_click_lead = st.form_submit_button('Veja o resultado')
        
        # Calcula o resultado apenas se os campos estiverem preenchidos
        if button_click_lead and number_invest_lead > 0 and number_cpa > 0:
            resultado_lead = number_invest_lead / number_cpa
            resultado_lead_esp = resultado_lead * 0.01
            lead_media = (resultado_lead_esp + resultado_lead) / 2
            st.session_state['lead_media'] = lead_media
            st.write("A média de número de leads será aproximadamente:", round(lead_media))

with st.container():
    # Verifica se ambos os resultados foram calculados
    if resultado is not None and lead_media is not None:
        st.header("Análise final")
        investimento_diario = number_invest_cli / 30
        cliques_diario = resultado / 30
        leads_diario = lead_media / 30

        # Texto revisado e cálculo da taxa de conversão
        st.write(f"Com um investimento de R$ {number_invest_cli:.2f}, você poderá alcançar uma média mensal de {round(resultado)} cliques, impulsionando sua presença online de forma significativa. Além disso, essa estratégia pode gerar uma média mensal de aproximadamente {round(lead_media)} leads valiosos para o seu negócio.")
        st.write(f"E se desdobrarmos esses números para um investimento diário, você terá um orçamento diário de aproximadamente R$ {investimento_diario:.2f}, o que resultará em uma média de {round(cliques_diario)} cliques diários e, consequentemente, cerca de {round(leads_diario)} novos leads diariamente.")
        # Cálculo da taxa de conversão em porcentagem
        taxa_conversao_porcent = round((leads_diario / cliques_diario) * 100, 2)

        # Output da taxa de conversão em porcentagem
        st.write(f"A taxa de conversão, de cliques para leads, é de {taxa_conversao_porcent}%.")

        st.write("Independentemente do resultado, essa análise fornece insights valiosos para otimizar sua estratégia de marketing e alcançar seus objetivos comerciais.")

        # Gráficos interativos com Plotly
        fig = go.Figure()

        # Gráfico de investimento
        fig.add_trace(go.Bar(
            x=['Diário', 'Mensal'],
            y=[round(investimento_diario), number_invest_cli],
            name='Investimento',
            marker_color='indianred'
        ))

        # Gráfico de cliques
        fig.add_trace(go.Bar(
            x=['Diário', 'Mensal'],
            y=[round(cliques_diario), resultado],
            name='Cliques',
            marker_color='lightsalmon'
        ))

        # Gráfico de leads
        fig.add_trace(go.Bar(
            x=['Diário', 'Mensal'],
            y=[round(leads_diario), round(lead_media)],
            name='Leads',
            marker_color='lightseagreen'
        ))

        fig.update_layout(
            title='Investimento, Cliques e Leads (Diário e Mensal)',
            xaxis_tickfont_size=15,
            yaxis=dict(
                title='Valores',
                titlefont_size=17,
                tickfont_size=15,
            ),
            barmode='group',
            bargap=0.15,
            bargroupgap=0.2
        )

        st.plotly_chart(fig)

        # Adiciona input para email e botão de envio
        email = st.text_input("Digite o email do destinatário:")
        send_email = st.button("Enviar Análise por Email")

        if send_email and email:
            # Criação do corpo do email em formato HTML
            html_content = f"""
            <html>
            <body>
                <h2>Análise de Desempenho</h2>
                <p>Com um investimento de R$ {number_invest_cli:.2f}, você poderá alcançar uma média mensal de {round(resultado)} cliques, impulsionando sua presença online de forma significativa. Além disso, essa estratégia pode gerar uma média mensal de aproximadamente {round(lead_media)} leads valiosos para o seu negócio.</p>
                <p>E se desdobrarmos esses números para um investimento diário, você terá um orçamento diário de aproximadamente R$ {investimento_diario:.2f}, o que resultará em uma média de {round(cliques_diario)} cliques diários e, consequentemente, cerca de {round(leads_diario)} novos leads diariamente.</p>
                <p>A taxa de conversão, de cliques para leads, é de {taxa_conversao_porcent}%.</p>
                <p>Independentemente do resultado, essa análise fornece insights valiosos para otimizar sua estratégia de marketing e alcançar seus objetivos comerciais.</p>
            </body>
            </html>
            """

            # Configuração do servidor SMTP usando SSL
            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login("varishopping123@gmail.com",st.write(st.secrets["MYPASS"]))
                
                # Criação da mensagem Multipart
                msg = MIMEMultipart()
                msg['From'] = "teste@gmail.com"
                msg['To'] = email
                msg['Subject'] = "Análise de Desempenho"

                # Adiciona o corpo do email em formato HTML
                msg.attach(MIMEText(html_content, 'html', _charset='utf-8'))

                # Envie o email
                server.send_message(msg)

                # Encerre a conexão com o servidor SMTP
                server.quit()
                st.success('Email enviado com sucesso!')
            except Exception as e:
                st.error(f"Falha ao enviar email: {e}")

# Adiciona o CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
