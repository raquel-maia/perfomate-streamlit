import streamlit as st # type: ignore

def show_investment_form(column):
    with column:
        st.header("Investimento:")
        number_invest_cli = st.number_input("Digite o investimento Mensal:", key="invest_cli")
        if number_invest_cli > 0:
            st.session_state['investimento'] = number_invest_cli
        return number_invest_cli if number_invest_cli > 0 else None

def show_cliques_form(column, number_invest_cli):
    with column:
        st.header("Cliques:")
        form_cal_cli = st.form(key="Cliques", clear_on_submit=False)
        with form_cal_cli:
            number_cpc = st.number_input("Digite o CPC Médio:", key="cpc")
            button_click_cli = st.form_submit_button('Veja o resultado')
            if button_click_cli and number_invest_cli > 0 and number_cpc > 0:
                resultado = number_invest_cli / number_cpc
                st.session_state['resultado'] = resultado
                st.write("O seu número de cliques será aproximadamente:", round(resultado))
                return resultado
        return st.session_state.get('resultado', None)

def show_leads_form(column, number_invest_cli):
    with column:
        st.header("Leads:")
        form_cal_lead = st.form(key="Leads", clear_on_submit=False)
        with form_cal_lead:
            number_cpa = st.number_input("Digite o CPA Médio:", key="cpa")
            button_click_lead = st.form_submit_button('Veja o resultado')
            if button_click_lead and number_invest_cli > 0 and number_cpa > 0:
                resultado_lead = number_invest_cli / number_cpa
                resultado_lead_esp = resultado_lead * 0.01
                lead_media = (resultado_lead_esp + resultado_lead) / 2
                st.session_state['lead_media'] = lead_media
                st.write("A média de número de leads será aproximadamente:", round(lead_media))
                return lead_media
        return st.session_state.get('lead_media', None)
