"""
STIMA DI PI GRECO CON IL METODO MONTE CARLO
=============================================

L'IDEA (spiegata semplice):
Immagina un quadrato di lato 1, con un angolo nell'origine (0,0).
Dentro questo quadrato disegniamo un quarto di cerchio di raggio 1
(il centro del cerchio è proprio nell'angolo del quadrato, in (0,0)).

Se lanciamo tantissimi "dardi" a caso dentro il quadrato, alcuni
cadranno DENTRO il quarto di cerchio, altri cadranno FUORI (ma
sempre dentro il quadrato).

La probabilità che un dardo cada dentro il cerchio è data dal
rapporto tra le due aree:

    area quarto di cerchio      (pi * r^2) / 4         pi
    -----------------------  =  ---------------  =  --------   (con r = 1)
    area quadrato                  1 * 1                4

Quindi, se contiamo quanti punti cadono dentro il cerchio rispetto
al totale dei punti lanciati, possiamo stimare pi con questa formula:

    pi ≈ 4 * (punti dentro il cerchio) / (punti totali)

Più punti lanciamo, più la nostra stima si avvicina al vero valore
di pi greco (3.14159...). Questo è un esempio di "esperimento
computazionale": non calcoliamo pi con una formula esatta, ma lo
STIMIAMO ripetendo un esperimento casuale tantissime volte!
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# 1) SCEGLIAMO QUANTI PUNTI LANCIARE
# ---------------------------------------------------------------
NUMERO_PUNTI = 2000

# ---------------------------------------------------------------
# 2) GENERIAMO I PUNTI CASUALI
# ---------------------------------------------------------------
x = np.random.uniform(0, 1, NUMERO_PUNTI)
y = np.random.uniform(0, 1, NUMERO_PUNTI)

# ---------------------------------------------------------------
# 3) CAPIAMO QUALI PUNTI SONO DENTRO AL QUARTO DI CERCHIO
# ---------------------------------------------------------------
# (è il teorema di Pitagora: la distanza dall'origine è sqrt(x^2+y^2),
distanza_al_quadrato = x**2 + y**2
dentro_al_cerchio = distanza_al_quadrato <= 1

# "dentro_al_cerchio" è un array di True/False, uno per ogni punto.
# Contiamo quanti True ci sono (Python considera True come 1 e False come 0).
numero_punti_dentro = np.sum(dentro_al_cerchio)

# ---------------------------------------------------------------
# 4) STIMIAMO PI GRECO
# ---------------------------------------------------------------
pi_stimato = 4 * numero_punti_dentro / NUMERO_PUNTI

print(f"Punti lanciati:        {NUMERO_PUNTI}")
print(f"Punti dentro il cerchio: {numero_punti_dentro}")
print(f"Stima di pi greco:      {pi_stimato}")
print(f"Valore vero di pi:      {np.pi}")
print(f"Errore:                 {abs(pi_stimato - np.pi):.5f}")

# ---------------------------------------------------------------
# 5) DISEGNIAMO IL RISULTATO CON MATPLOTLIB
# ---------------------------------------------------------------
# Vogliamo un disegno quadrato (altrimenti il cerchio sembrerebbe
# una "uovo" invece che rotondo), con i punti colorati in base
# a dove sono caduti:
#   - verde  -> dentro al cerchio
#   - rosso  -> fuori dal cerchio

figura, assi = plt.subplots(figsize=(6, 6))

# Disegniamo prima i punti FUORI dal cerchio (colore rosso)
assi.scatter(
    x[~dentro_al_cerchio],   # il simbolo ~ significa "il contrario di", quindi qui prendiamo i punti FUORI
    y[~dentro_al_cerchio],
    color="red",
    s=8,                     # dimensione dei punti
    label="fuori dal cerchio",
)

# Poi disegniamo i punti DENTRO al cerchio (colore verde)
assi.scatter(
    x[dentro_al_cerchio],
    y[dentro_al_cerchio],
    color="green",
    s=8,
    label="dentro il cerchio",
)

# Disegniamo anche il bordo del quarto di cerchio, per vederlo bene
angoli = np.linspace(0, np.pi / 2, 200)   # 200 angoli tra 0 e 90 gradi (in radianti)
assi.plot(np.cos(angoli), np.sin(angoli), color="black", linewidth=2)

# Sistemiamo l'aspetto del grafico
assi.set_xlim(0, 1)
assi.set_ylim(0, 1)
assi.set_aspect("equal")   # fondamentale: senza questo il cerchio sembrerebbe ovale!
assi.set_title(f"Stima di pi greco con Monte Carlo\npi ≈ {pi_stimato:.5f}  (valore vero: {np.pi:.5f})")
assi.set_xlabel("x")
assi.set_ylabel("y")
assi.legend(loc="upper right")

plt.show()
