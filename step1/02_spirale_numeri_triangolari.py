import math

import numpy as np
import matplotlib.pyplot as plt

NUMERO_MASSIMO = 1000 

def numeri_Triangolari(n):
    serie_numeri_triangolari = []
    for i in range(1, n + 1):
        serie_numeri_triangolari.append((i * (i + 1) // 2))
        print(i*(i + 1) // 2)
    return serie_numeri_triangolari



numeri = range(1, NUMERO_MASSIMO + 1)
numeri_np = np.array(numeri)

numeri_triangolari = numeri_Triangolari(NUMERO_MASSIMO)
x = numeri_np * np.cos(numeri_np)
y = numeri_np * np.sin(numeri_np)
maschera_numeri_triangolari = np.array([n in numeri_triangolari for n in numeri])
x_numeri_triangolari = x[maschera_numeri_triangolari]
y_numeri_triangolari = y[maschera_numeri_triangolari]



figura, assi = plt.subplots(figsize=(8, 8))
assi.scatter(x, y, color="yellow", s=6, label="tutti gli interi")
assi.scatter(x_numeri_triangolari, y_numeri_triangolari, color="red", s=14, label="numeri triangolari")
assi.set_title(f"Tutti i numeri (triangolari in rosso)")
assi.set_aspect("equal")
assi.set_xticks([])
assi.set_yticks([])
plt.show()  