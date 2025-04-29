import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as lib
import numpy as np

app = dash.Dash(__name__)

# Layout dell'app (HTML)
app.layout = html.Div(
    style={"display": "flex", "flexDirection": "column", "height": "100vh"},
    children=[
        # Titolo dell'app
        html.Div(
            style={"textAlign": "center", "padding": "0px"},
            children=[
                html.H2("Inviluppo delle tangenti alla parabola")
            ]
        ),
        
        # Input dei dati sopra il grafico
        html.Div(
            style={
                "flex": 0.2,
                "padding": "20px", 
                "textAlign": "center",
                "display": "flex",
                "flexDirection": "row",  # Disposizione orizzontale
                "justifyContent": "center",  # Centra gli input nella riga
                "gap": "15px",  # Spaziatura tra gli input
                "alignItems": "center",  # Allinea gli input verticalmente
            },
            children=[
                # Etichetta e input per il coefficiente a
                html.Div(
                    style={"display": "flex", "flexDirection": "column", "alignItems": "center"},
                    children=[
                        html.Label("Coefficiente a"),
                        dcc.Input(id="a", type="number", value=2, step=0.1, debounce=True, placeholder="Coefficiente a", style={"width": "150px"}),
                    ]
                ),

                # Etichetta e input per il coefficiente b
                html.Div(
                    style={"display": "flex", "flexDirection": "column", "alignItems": "center"},
                    children=[
                        html.Label("Coefficiente b"),
                        dcc.Input(id="b", type="number", value=0, step=0.1, debounce=True, placeholder="Coefficiente b", style={"width": "150px"}),
                    ]
                ),

                # Etichetta e input per il coefficiente c
                html.Div(
                    style={"display": "flex", "flexDirection": "column", "alignItems": "center"},
                    children=[
                        html.Label("Coefficiente c"),
                        dcc.Input(id="c", type="number", value=0, step=0.1, debounce=True, placeholder="Coefficiente c", style={"width": "150px"}),
                    ]
                ),

                # Etichetta e input per il numero di tangenti
                html.Div(
                    style={"display": "flex", "flexDirection": "column", "alignItems": "center"},
                    children=[
                        html.Label("Numero di tangenti"),
                        dcc.Input(id="num_tangenti", type="number", value=20, min=1, max=500, step=1, debounce=True, placeholder="Numero di tangenti", style={"width": "150px"}),
                    ]
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
    ])
def aggiorna_parabola_tangenti(a, b, c, num_tangenti):
    fig = lib.Figure()

    # Vertice della parabola
    x_vertice = -b / (2 * a)
    y_vertice = a * x_vertice**2 + b * x_vertice + c

    # Distanza da centrare rispetto al vertice
    range_offset = 100  # Aumentato per una visualizzazione più ampia
    
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
    
    # Genera i valori per x (ad esempio, da -1000 a 1000 per una visione più ampia)
    x = np.linspace(-1000, 1000, 10000)
    y = float(a) * x**2 + float(b) * x + float(c)  # Equazione della parabola

    # Aggiungi la parabola al grafico
    fig.add_trace(lib.Scatter(x=x, y=y, mode='lines', line=dict(width=3), name=f'y = {a}x² + {b}x + {c}', showlegend=False))

    # Calcoliamo e aggiungiamo le tangenti in vari punti
    tangent_x = np.linspace(x_vertice - 50, x_vertice + 50, num_tangenti)  # Più ampio intervallo di tangenti
    for x0 in tangent_x:
        m = 2 * a * x0 + b  # Pendenza della tangente
        y0 = a * x0**2 + b * x0 + c  # Punto sulla parabola
        tangent_y = m * (x - x0) + y0
        fig.add_trace(lib.Scatter(x=x, y=tangent_y, mode='lines', line=dict(dash='solid', color='red', width=1.25), showlegend=False))

    # Aggiungi gli assi "infiniti" estesi
    fig.add_shape(
        type="line",
        x0=-10000, y0=0, x1=10000, y1=0,  # Estendere oltre i limiti
        line=dict(color="black", width=2),
    )

    fig.add_shape(
        type="line",
        x0=0, y0=-10000, x1=0, y1=10000,  # Estendere oltre i limiti
        line=dict(color="black", width=2),
    )

    # Aggiornamenti del layout
    fig.update_layout(
        xaxis=dict(
            range=[x_vertice - range_offset, x_vertice + range_offset], 
            zeroline=False, 
            showgrid=True, 
            gridcolor='lightgrey',
            fixedrange=False,  # Consente lo zoom
        ),
        yaxis=dict(
            range=[y_vertice - range_offset, y_vertice + range_offset], 
            zeroline=False, 
            showgrid=True, 
            gridcolor='lightgrey',
            fixedrange=False,  # Consente lo zoom
        ),
        plot_bgcolor="white",
        autosize=True, 
        dragmode='zoom',  # Permette lo zoom, ma disabilita il pan
    )
    
    return fig

# Esegui l'app
if __name__ == '__main__':
    app.run(debug=True)