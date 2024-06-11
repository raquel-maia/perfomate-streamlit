import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st # type: ignore

def send_analysis_email(email, analysis_text, number_invest_cli, resultado, lead_media, investimento_diario, cliques_diario, leads_diario):
    html_content = f"""
    <html>
    <body>
        {analysis_text}
    </body>
    </html>
    """
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("varishopping123@gmail.com",st.secrets.cred.emailpass)
        msg = MIMEMultipart()
        msg['From'] = "teste@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Análise de Desempenho"
        msg.attach(MIMEText(html_content, 'html', _charset='utf-8'))
        server.send_message(msg)
        server.quit()
        st.success('Email enviado com sucesso!')
    except Exception as e:
        st.error(f"Falha ao enviar email: {e}")
