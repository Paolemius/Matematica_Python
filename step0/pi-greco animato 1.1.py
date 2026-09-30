"""
Simulazione Monte Carlo per la stima di Pi Greco - Versione 1.1
----------------------------------------------------------------
- Layout: 3 grafici (Simulazione + Evoluzione della stima + Errore assoluto in scala logaritmica).
- Rendering punti: Ottimizzato tramite Matplotlib plot (set_data).
- Configurazione: 100.000 punti totali, aggiornamento ogni 10.000 punti (10 frame).
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n_punti = 100000
punti_per_frame = 500

# 1. Calcoli matematici vettorializzati
x = np.random.uniform(0, 1, n_punti)
y = np.random.uniform(0, 1, n_punti)
dentro_al_cerchio = (x**2 + y**2) <= 1

punti_dentro_cumulativi = np.cumsum(dentro_al_cerchio)
numero_punti_progressivo = np.arange(1, n_punti + 1)

pi_storico = 4 * punti_dentro_cumulativi / numero_punti_progressivo
errore_storico = np.abs(pi_storico - np.pi)

# 2. Creazione della finestra divisa in 3 colonne
figura, (assi_cerchio, assi_pi, assi_errore) = plt.subplots(1, 3, figsize=(15, 5))

# --- GRAFICO 1: CERCHIO ---
assi_cerchio.set_xlim(0, 1)
assi_cerchio.set_ylim(0, 1)
assi_cerchio.set_aspect("equal")
assi_cerchio.set_title("Simulazione Monte Carlo")

angoli = np.linspace(0, np.pi / 2, 200)
assi_cerchio.plot(np.cos(angoli), np.sin(angoli), color="black", linewidth=2)

punti_dentro, = assi_cerchio.plot([], [], linestyle='', marker='o', color="green", markersize=2, label="Dentro")
punti_fuori, = assi_cerchio.plot([], [], linestyle='', marker='o', color="red", markersize=2, label="Fuori")
assi_cerchio.legend(loc="upper right")

testo_valore = assi_cerchio.text(0.05, 0.9, "", fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

# --- GRAFICO 2: STIMA DI PI GRECO ---
assi_pi.set_xlim(0, n_punti)
assi_pi.set_ylim(2.5, 3.8)
assi_pi.set_title("Evoluzione della stima")
assi_pi.axhline(np.pi, color="black", linestyle="--", label=f"Valore reale")
linea_stima, = assi_pi.plot([], [], color="blue", linewidth=2, label="Stima")
assi_pi.legend(loc="upper right")

# --- GRAFICO 3: ERRORE ASSOLUTO (SCALA LOGARITMICA) ---
assi_errore.set_xlim(0, n_punti)

# Impostiamo la scala logaritmica
assi_errore.set_yscale("log")

# Troviamo il minimo errore maggiore di 0 per evitare l'errore matematico del log(0)
errore_minimo_valido = np.min(errore_storico[errore_storico > 0])
errore_massimo = np.max(errore_storico[punti_per_frame:])
assi_errore.set_ylim(errore_minimo_valido, errore_massimo)

assi_errore.set_title("Errore assoluto (Log)")
assi_errore.set_ylabel("Distanza dal Pi reale (Log)")
linea_errore, = assi_errore.plot([], [], color="red", linewidth=2)

# 3. Funzione di aggiornamento dei frame
def aggiorna(frame):
    x_corr = x[:frame]
    y_corr = y[:frame]
    dentro_corr = dentro_al_cerchio[:frame]
    
    punti_dentro.set_data(x_corr[dentro_corr], y_corr[dentro_corr])
    punti_fuori.set_data(x_corr[~dentro_corr], y_corr[~dentro_corr])
    
    linea_stima.set_data(numero_punti_progressivo[:frame], pi_storico[:frame])
    linea_errore.set_data(numero_punti_progressivo[:frame], errore_storico[:frame])
    
    testo_valore.set_text(f"Punti: {frame}\nPi stimato: {pi_storico[frame-1]:.5f}")
    
    return punti_dentro, punti_fuori, linea_stima, linea_errore, testo_valore

# 4. Avvio dell'animazione
animazione = FuncAnimation(
    figura, 
    aggiorna, 
    frames=range(punti_per_frame, n_punti + 1, punti_per_frame), 
    interval=20, 
    blit=False, 
    repeat=False
)

plt.tight_layout()
plt.show()