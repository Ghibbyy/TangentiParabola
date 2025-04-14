"""
FASE 1: Rappresentazione del piano cartesiano

Obiettivo: Creare un grafico vuoto con assi cartesiani ben definiti
"""

import plotly.graph_objs as lib

# Creo la figura vuota
fig = lib.Figure()

# Asse X
fig.add_shape(
    type="line",
    x0=-1000, y0=0, x1=10000, y1=0,
    line=dict(color="grey", width=2),
)
fig.add_annotation(
    x=50, y=0,
    ax=48, ay=0,
    xref="x", yref="y",
    axref="x", ayref="y",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="grey"
)

# Asse Y 
fig.add_shape(
    type="line",
    x0=0, y0=-10000, x1=0, y1=10000,
    line=dict(color="grey", width=2),
)
fig.add_annotation(
    x=0, y=50,
    ax=0, ay=48,
    xref="x", yref="y",
    axref="x", ayref="y",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="grey",
    xanchor="center",  # Ancoraggio della freccia al centro
    yanchor="top",  # Ancoraggio della freccia in alto
)


# Layout generale
fig.update_layout(
    title="Fase-01, creazione assi cartesiani",
    xaxis=dict(range=[-50, 50], zeroline=False, showgrid=True, gridcolor='lightgrey'),
    yaxis=dict(range=[-50, 50], zeroline=False, showgrid=True, gridcolor='lightgrey'),
    plot_bgcolor="white",  # sfondo bianco
    margin=dict(l=50, r=50, t=50, b=150),  # spazio bianco in basso
    autosize=True,  # Adatta automaticamente la dimensione del grafico
    dragmode="pan",  # Abilita lo spostamento (pan) del grafico
    hovermode="closest"  # Abilita l'interazione con il grafico
)

fig.show()
