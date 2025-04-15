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
        # Input dei dati sopra il grafico
        html.Div(
            style={
                "flex": 0.2,
                "padding": "20px", 
                "textAlign": "center",
            },
            children=[
                html.H2("Inserisci i valori per l'equazione della parabola"),
                dcc.Input(id="a", type="number", value=2, step=0.5, debounce=True, placeholder="Coefficiente a", style={"margin": "10px", "width": "150px"}),
                dcc.Input(id="b", type="number", value=0, step=0.5, debounce=True, placeholder="Coefficiente b", style={"margin": "10px", "width": "150px"}),
                dcc.Input(id="c", type="number", value=0, step=0.5, debounce=True, placeholder="Coefficiente c", style={"margin": "10px", "width": "150px"}),

                # Numero di tangenti
                dcc.Input(id="num_tangenti", type="number", value=20, min=1, max=500, step=1, debounce=True, placeholder="Numero di tangenti", style={"margin": "10px", "width": "150px"}),

                # Tipo di linea per le tangenti
                dcc.Dropdown(
                    id="tipo_linea",
                    options=[
                        {'label': 'Continua', 'value': 'solid'},
                        {'label': 'Tratteggiata', 'value': 'dot'}
                    ],
                    value='solid',  # Impostazione di default
                    style={"margin": "10px", "width": "150px"}
                ),
            ]
        ),
        # Grafico
        html.Div(
            dcc.Graph(id='grafico_parabola_tangenti'),
            style={"flex": 1, "height": "100%"}
        ),
    ]
)

# Funzione di callback per aggiornare il grafico
@app.callback(
    Output('grafico_parabola_tangenti', 'figure'),
    [Input('a', 'value'),
     Input('b', 'value'),
     Input('c', 'value'),
     Input('num_tangenti', 'value'),
     Input('tipo_linea', 'value')]
)
def aggiorna_parabola_tangenti(a, b, c, num_tangenti, tipo_linea):
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
    
    # Genera i valori per x (ad esempio, da -100 a 100)
    x = np.linspace(-100, 100, 400)
    y = float(a) * x**2 + float(b) * x + float(c)  # Equazione della parabola

    # Aggiungi la parabola al grafico
    fig.add_trace(lib.Scatter(x=x, y=y, mode='lines', name=f'y = {a}x² + {b}x + {c}', showlegend=False))

    # Calcoliamo e aggiungiamo le tangenti in vari punti
    tangent_x = np.linspace(-10, 10, num_tangenti)  # Punti su cui calcolare le tangenti (range più ampio)
    for x0 in tangent_x:
        # Derivata prima della parabola
        m = 2 * a * x0 + b  # Pendenza della tangente
        y0 = a * x0**2 + b * x0 + c  # Punto sulla parabola
        # Equazione della tangente
        tangent_y = m * (x - x0) + y0
        fig.add_trace(lib.Scatter(x=x, y=tangent_y, mode='lines', line=dict(dash=tipo_linea, color='red'), showlegend=False))

    # Aggiornamenti del layout
    initial_range = 50  # Zoom iniziale (limita la vista iniziale)
    fig.update_layout(
        title=f"Parabola e Tangenti",
        xaxis=dict(range=[-initial_range, initial_range], zeroline=False, showgrid=True, gridcolor='lightgrey'),
        yaxis=dict(range=[-initial_range, initial_range], zeroline=False, showgrid=True, gridcolor='lightgrey'),
        plot_bgcolor="white",
        autosize=True,  # Grafico adattabile alle dimensioni della finestra
    )
    
    return fig

# Esegui l'app
if __name__ == '__main__':
    app.run(debug=True)