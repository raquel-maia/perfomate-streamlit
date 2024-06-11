import plotly.graph_objects as go # type: ignore


def create_performance_analysis_plot(number_invest_cli, investimento_diario, resultado, cliques_diario, leads_diario, lead_media):
    fig = go.Figure()
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

        # Gráfico de investimento
        
    return fig