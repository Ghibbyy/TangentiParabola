"""
FASE 1: Rappresentazione del piano cartesiano

Obiettivo: Creare un grafico vuoto con assi cartesiani ben definiti
"""

import matplotlib.pyplot as plt

# Creo la figura e gli assi
fig, ax = plt.subplots()

# Possibilità di modificare la grandezza degli assi
ax.set_xlim(-50, 50)
ax.set_ylim(-10, 50)

# Disegno gli assi cartesiani
ax.annotate("", xy=(50, 0), xytext=(-50, 0), arrowprops=dict(arrowstyle="->", color='grey', linewidth=1))  # Asse X
ax.annotate("", xy=(0, 50), xytext=(0, -10), arrowprops=dict(arrowstyle="->", color='grey', linewidth=1)) # Asse Y

# Possibilità di aggiungere la griglia
ax.grid(False)

# Titolo
ax.set_title('Fase-01, creazione assi cartesiani')

# Nascondo i bordi esterni 
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# layout dinamico con spazio bianco in basso
plt.subplots_adjust(
    left=0.1,   # bordo sinistro
    right=0.9,  # bordo destro
    top=0.9,    # bordo alto
    bottom=0.3  # bordo basso
)

plt.show()