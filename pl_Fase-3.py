import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as lib
import numpy as np

# Crea l'app Dash
app = dash.Dash(__name__)

# Layout dell'app
app.layout = html.Div(
    style={"display": "flex", "flexDirection": "column", "height": "100vh"},
    children=[
        #input dei dati sopra il grafico
        html.Div(
            style={
                "flex": 0.2,
                "padding": "20px", 
                "textAlign": "center",
            },
            children=[
                html.H2("Inserisci i valori per l'equazione della parabola"),
                dcc.Input(id="a", type="number", value=2, step=0.5, debounce=True, placeholder="Coefficiente a", style={"margin": "10px", "width": "150px"}),
                dcc.Input(id="b", type="number", value=5, step=0.5, debounce=True, placeholder="Coefficiente b", style={"margin": "10px", "width": "150px"}),
                dcc.Input(id="c", type="number", value=0, step=0.5, debounce=True, placeholder="Coefficiente c", style={"margin": "10px", "width": "150px"}),
            ]
        ),
        # Grafico
        html.Div(
            dcc.Graph(id='grafico_parabola'),
            style={"flex": 1, "height": "100%"}
        ),
    ]
)

# Funzione di callback per aggiornare il grafico
@app.callback(
    Output('grafico_parabola', 'figure'),
    [Input('a', 'value'),
     Input('b', 'value'),
     Input('c', 'value')]
)
def aggiorna_parabola(a, b, c):
    fig = lib.Figure()

    # Asse X (linea orizzontale)
    fig.add_shape(
        type="line",
        x0=-1000, y0=0, x1=1000, y1=0,
        line=dict(color="grey", width=2),
    )

    # Asse Y (linea verticale)
    fig.add_shape(
        type="line",
        x0=0, y0=-1000, x1=0, y1=1000,
        line=dict(color="grey", width=2),
    )
    
    x = np.linspace(-100, 100, 400) 
    y = float(a) * x**2 + float(b) * x + float(c)

    # Aggiungi la parabola
    fig.add_trace(lib.Scatter(x=x, y=y, mode='lines', name=f'y = {a}x² + {b}x + {c}'))

    initial_range = 15  # Zoom iniziale (limita la vista iniziale)
    fig.update_layout(
        title=f"y = {a}x² + {b}x + {c}",
        xaxis=dict(range=[-initial_range, initial_range], zeroline=False, showgrid=True, gridcolor='lightgrey'),
        yaxis=dict(range=[-initial_range, initial_range], zeroline=False, showgrid=True, gridcolor='lightgrey'),
        plot_bgcolor="white",
        autosize=True,
    )
    
    return fig

# Esegui l'app
if __name__ == '__main__':
    app.run(debug=True)