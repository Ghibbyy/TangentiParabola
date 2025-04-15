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
        # Sezione per l'input dei dati sopra il grafico
        html.Div(
            style={
                "flex": 0.2,  # La sezione dell'input occupa 1/5 dello schermo
                "padding": "20px", 
                "textAlign": "center",
            },
            children=[
                html.H2("Inserisci i valori per l'equazione della retta"),
                dcc.Input(id="pendenza", type="number", value=2, step=0.5, debounce=True, placeholder="Pend. (a)", style={"margin": "10px", "width": "150px"}),
                dcc.Input(id="intercetta", type="number", value=3, step=0.5, debounce=True, placeholder="Intercetta (b)", style={"margin": "10px", "width": "150px"}),
            ]
        ),
        # Grafico che occupa tutta la parte rimanente della schermata
        html.Div(
            dcc.Graph(id='grafico_retta'),
            style={"flex": 1, "height": "100%"}  # Grafico occupa il restante spazio
        ),
    ]
)

# Funzione di callback per aggiornare il grafico
@app.callback(
    Output('grafico_retta', 'figure'),
    [Input('pendenza', 'value'),
     Input('intercetta', 'value')]
)
def aggiorna_grafico(a, b):
    # Crea il grafico
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

    # Calcola i punti della retta y = ax + b (rettangolo lungo)
    x = np.linspace(-1000, 1000, 1000)  # Rettangolo lungo
    y = float(a) * x + float(b)

    # Aggiungi la retta come una traccia
    fig.add_trace(lib.Scatter(x=x, y=y, mode='lines', name=f'y = {a}x + {b}'))

    initial_range = 50  # zoom
    fig.update_layout(
        title=f"y = {a}x + {b}",
        xaxis=dict(range=[-initial_range, initial_range], zeroline=False, showgrid=True, gridcolor='lightgrey'),
        yaxis=dict(range=[-initial_range, initial_range], zeroline=False, showgrid=True, gridcolor='lightgrey'),
        plot_bgcolor="white",
        autosize=True,  # Grafico adattabile alle dimensioni della finestra
    )
    
    return fig

# Esegui l'app
if __name__ == '__main__':
    app.run(debug=True)