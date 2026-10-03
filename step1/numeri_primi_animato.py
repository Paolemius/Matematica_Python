import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

NUMERO_MASSIMO = 200000
# Numero di numeri da aggiungere in ogni singolo fotogramma dell'animazione
NUMERI_PER_FRAME = 300 

def numeri_primi(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(np.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True

# Generazione dati
numeri_np = np.arange(1, NUMERO_MASSIMO + 1)
x = numeri_np * np.cos(numeri_np)
y = numeri_np * np.sin(numeri_np)

# Maschera booleana per i numeri primi
maschera_numeri_primi = np.array([numeri_primi(n) for n in numeri_np])

# Setup del grafico
figura, assi = plt.subplots(figsize=(8, 8))
figura.patch.set_facecolor('#fdfdfd') # Sfondo pulito

# Creiamo i due "scatter plot" inizialmente vuoti
scatter_tutti = assi.scatter([], [], color=(0.39, 0.11, 0.98), s=2, label="Tutti gli interi")
scatter_primi = assi.scatter([], [], color="red", s=6, label="Numeri primi")

# Impostazioni estetiche degli assi
assi.set_aspect("equal")
assi.set_xticks([])
assi.set_yticks([])
assi.legend(loc="upper right")
titolo = assi.set_title("Evoluzione della Spirale dei Numeri (0 interi)")

# Funzione per inizializzare l'animazione
def init():
    scatter_tutti.set_offsets(np.empty((0, 2)))
    scatter_primi.set_offsets(np.empty((0, 2)))
    return scatter_tutti, scatter_primi, titolo

# Funzione chiamata a ogni fotogramma (frame)
def update(frame):
    # Calcoliamo quanti numeri mostrare in questo frame
    limite_corrente = min((frame + 1) * NUMERI_PER_FRAME, NUMERO_MASSIMO)
    
    # Selezioniamo i dati fino al limite corrente
    x_curr = x[:limite_corrente]
    y_curr = y[:limite_corrente]
    maschera_curr = maschera_numeri_primi[:limite_corrente]
    
    # Aggiorniamo i punti di tutti i numeri
    punti_tutti = np.column_stack((x_curr, y_curr))
    scatter_tutti.set_offsets(punti_tutti)
    
    # Aggiorniamo i punti solo dei numeri primi
    punti_primi = np.column_stack((x_curr[maschera_curr], y_curr[maschera_curr]))
    scatter_primi.set_offsets(punti_primi)
    
    # Espandiamo dinamicamente i limiti del grafico man mano che la spirale cresce
    margine = limite_corrente * 1.05
    assi.set_xlim(-margine, margine)
    assi.set_ylim(-margine, margine)
    
    # Aggiorniamo il titolo con il conteggio corrente
    titolo.set_text(f"Spirale di Ulam in espansione ({limite_corrente} interi)")
    
    return scatter_tutti, scatter_primi, titolo

# Calcoliamo il numero totale di frame necessari
dati_per_frame = NUMERO_MASSIMO // NUMERI_PER_FRAME + 1

# Creiamo l'animazione
animazione = FuncAnimation(
    figura, 
    update, 
    frames=dati_per_frame, 
    init_func=init, 
    blit=False, 
    interval=30,  # Millisecondi di attesa tra un frame e l'altro
    repeat=False  # Si ferma una volta completata
)

plt.show()