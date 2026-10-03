import math

import numpy as np
import matplotlib.pyplot as plt

NUMERO_MASSIMO = 1000 

numeri =range(1, NUMERO_MASSIMO + 1)
numeri_np = np.array(numeri)
print(numeri_np)
x = numeri_np * np.cos(numeri_np)
y = numeri_np * np.sin(numeri_np)



figura, assi = plt.subplots(figsize=(8, 8))
assi.scatter(x, y, color="yellow", s=6, label="tutti gli interi")
assi.set_title(f"Tutti i numeri")
assi.set_aspect("equal")
assi.set_xticks([])
assi.set_yticks([])
plt.show()  