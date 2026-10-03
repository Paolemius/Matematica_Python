import math

import numpy as np
import matplotlib.pyplot as plt

NUMERO_MASSIMO = 1000 

def numeri_Fibonacci(n):
    serie_numeri_fibonacci = []
    serie_numeri_fibonacci.append(1)
    for i in range(1, n + 1):
        serie_numeri_fibonacci.append(serie_numeri_fibonacci[i-1] + serie_numeri_fibonacci[i-2])
    return serie_numeri_fibonacci

numeri = range(1, NUMERO_MASSIMO + 1)
numeri_np = np.array(numeri)

numeri_fibonacci = numeri_Fibonacci(NUMERO_MASSIMO)
x = numeri_np * np.cos(numeri_np)
y = numeri_np * np.sin(numeri_np)
maschera_numeri_fibonacci = np.array([n in numeri_fibonacci for n in numeri])
x_numeri_fibonacci = x[maschera_numeri_fibonacci]
y_numeri_fibonacci = y[maschera_numeri_fibonacci]



figura, assi = plt.subplots(figsize=(8, 8))
assi.scatter(x, y, color="yellow", s=6, label="tutti gli interi")
assi.scatter(x_numeri_fibonacci, y_numeri_fibonacci, color="red", s=14, label="numeri fibonacci")
assi.set_title(f"Tutti i numeri (fibonacci in rosso)")
assi.set_aspect("equal")
assi.set_xticks([])
assi.set_yticks([])
plt.show()  