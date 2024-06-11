# Performate

Esse é um projeto pessoal que eu sempre quis fazer para facilitar a vida dos analistas de mídia que querem realizar uma análise básica de leads e cliques. A ideia é simplificar o processo de estimativa de leads e cliques das campanhas publicitárias, oferecendo uma interface amigável e intuitiva. Além disso, permite o envio instantâneo da análise por email de um jeito rápido e eficiente.

## Tecnologias Usadas

- [Streamlit](https://streamlit.io/): Para criação da interface web interativa.
- [Plotly](https://plotly.com/): Para geração de gráficos interativos.
- [smtplib](https://docs.python.org/3/library/smtplib.html): Para envio de emails.

## Cálculos Realizados

1. **Cliques**:
   - Calcula o número de cliques com base no investimento médio mensal e no CPC (Custo por Clique) médio.
   - Fórmula: `Número de Cliques = Investimento Mensal / CPC`

2. **Leads**:
   - Calcula o número de leads com base no investimento médio mensal e no CPA (Custo por Aquisição) médio.
   - Fórmula: `Número de Leads = Investimento Mensal / CPA`
   - Também calcula a média esperada de leads, ajustando 1% do resultado obtido e fazendo uma média entre os dois valores.

3. ### Análise Final

- **Médias Diárias**: Divide os resultados mensais por 30 para obter médias diárias de investimento, cliques e leads.
- **Taxa de Conversão**: Calcula a taxa de conversão de cliques para leads.
- **Visualização**: Gera gráficos interativos mostrando o investimento, cliques e leads tanto em bases diárias quanto mensais.
- **Envio por Email**: Permite enviar a análise de texto completa por email para facilitar o compartilhamento de resultados. ( o Grafico ainda não foi configurado para envio )


Link do Projeto = https://perfomate.streamlit.app/

![Resultado Final](https://i.postimg.cc/y6QC6q9W/perfor-update.png)