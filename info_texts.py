def get_analysis_text(number_invest_cli, resultado, lead_media, investimento_diario, cliques_diario, leads_diario):
    taxa_conversao_porcent = round((leads_diario / cliques_diario) * 100, 2)
    return f"""
    <h2>Análise de Desempenho</h2>
    <p>Com um investimento de R$ {number_invest_cli:.2f}, você poderá alcançar uma média mensal de {round(resultado)} cliques, impulsionando sua presença online de forma significativa. Além disso, essa estratégia pode gerar uma média mensal de aproximadamente {round(lead_media)} leads valiosos para o seu negócio.</p>
    <p>E se desdobrarmos esses números para um investimento diário, você terá um orçamento diário de aproximadamente R$ {investimento_diario:.2f}, o que resultará em uma média de {round(cliques_diario)} cliques diários e, consequentemente, cerca de {round(leads_diario)} novos leads diariamente.</p>
    <p>A taxa de conversão, de cliques para leads, é de {taxa_conversao_porcent}%.</p>
    <p>Independentemente do resultado, essa análise fornece insights valiosos para otimizar sua estratégia de marketing e alcançar seus objetivos comerciais.</p>
    """
