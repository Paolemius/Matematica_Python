import math

import numpy as np
import matplotlib.pyplot as plt

NUMERO_MASSIMO = 20000

def numeri_primi(n):
    isprimo = True
    if n%2 == 0:
        isprimo = False
    else:
        for x in range(2, np.int64(np.sqrt(n)+1)):
            if n%x == 0:
                isprimo = False
                break
            
    return isprimo

numeri =range(1, NUMERO_MASSIMO + 1)
numeri_np = np.array(numeri)

x = numeri_np * np.cos(numeri_np)
y = numeri_np * np.sin(numeri_np)
maschera_numeri_primi = np.array([numeri_primi(n) for n in numeri])
x_numeri_primi = x[maschera_numeri_primi]
y_numeri_primi = y[maschera_numeri_primi]
print("tutti i numeri:")
print(numeri_np)
print("sono primi?")
print(maschera_numeri_primi)
print("tutti i numeri primi:")
print(numeri_np[maschera_numeri_primi])



figura, assi = plt.subplots(figsize=(8, 8))
assi.scatter(x, y, color=(0.39,0.11,0.98), s=9, label="tutti gli interi")
assi.scatter(x_numeri_primi, y_numeri_primi, color="red", s=15, label="numeri primi")
assi.set_title(f"Tutti i numeri (numeri primi)")
assi.set_aspect("equal")
assi.set_xticks([])
assi.set_yticks([])
plt.show()  