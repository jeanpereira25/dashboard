import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Simulação de dados
data = {
    'Categoria': ['Salário', 'Mercado', 'Escola', 'Internet', 'Gastos Extras'],
    'Valor': [5000, 300, 200, 100, 50],
    'Data': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05']
}
df = pd.DataFrame(data)

# Inicialização do app
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div(
    style={'backgroundColor': '#121212', 'color': 'white'},
    children=[
        # Cabeçalho
        html.Div(
            className='header',
            children=[
                html.H1("Dashboard Finanças Pessoais", style={'color': 'white'}),
                html.Div(
                    id='saldo-container',
                    children=[
                        html.Span("Saldo:", style={'font-weight': 'bold'}),
                        html.Span("R$ 4,216", style={'color': '#FF5733'})
                    ],
                    style={'background': 'linear-gradient(45deg, #FF5733, #FFB86C)', 'padding': '10px', 'borderRadius': '10px'}
                )
            ]
        ),
        
        # Seção de Entradas e Despesas
        html.Div(
            className='section',
            children=[
                html.Div(
                    className='card',
                    children=[
                        html.H3("Entradas", style={'color': 'white'}),
                        dcc.Graph(
                            figure=px.line(df, x='Data', y='Valor', title="Histórico de Entradas"),
                            config={'displayModeBar': False}
                        )
                    ]
                ),
                html.Div(
                    className='card',
                    children=[
                        html.H3("Despesas", style={'color': 'white'}),
                        dcc.Graph(
                            figure=px.line(df, x='Data', y='Valor', title="Histórico de Despesas"),
                            config={'displayModeBar': False}
                        )
                    ]
                )
            ],
            style={'display': 'flex', 'gap': '20px'}
        ),
        
        # Top 5 Entradas e Despesas
        html.Div(
            className='section',
            children=[
                html.Div(
                    className='card',
                    children=[
                        html.H3("Top 5 Entradas por Categoria", style={'color': 'white'}),
                        dcc.Graph(
                            figure=px.bar(df.head(5), x='Categoria', y='Valor', color='Categoria', title="Top 5 Entradas"),
                            config={'displayModeBar': False}
                        )
                    ]
                ),
                html.Div(
                    className='card',
                    children=[
                        html.H3("Top 5 Despesas por Categoria", style={'color': 'white'}),
                        dcc.Graph(
                            figure=px.pie(df.head(5), names='Categoria', values='Valor', title="Top 5 Despesas"),
                            config={'displayModeBar': False}
                        )
                    ]
                )
            ],
            style={'display': 'flex', 'gap': '20px'}
        ),
        
        # Ícones interativos
        html.Div(
            className='section',
            children=[
                html.Button(
                    html.I(className='fas fa-school'),  # Ícone de escola
                    id='btn-escola',
                    style={'background': 'none', 'border': 'none', 'color': 'white', 'fontSize': '2em'}
                ),
                html.Button(
                    html.I(className='fas fa-bolt'),  # Ícone de energia elétrica
                    id='btn-energia',
                    style={'background': 'none', 'border': 'none', 'color': 'white', 'fontSize': '2em'}
                ),
                # Adicionar mais ícones aqui...
            ],
            style={'display': 'flex', 'gap': '20px'}
        )
    ]
)

# Execução do app
if __name__ == '__main__':
    app.run_server(debug=True)