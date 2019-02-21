from matplotlib.pyplot import cm
import numpy as np
import matplotlib.pyplot as plt


# Contour Plot
X, Y = np.mgrid[-6.6: 6.6, -6.6: 6.6]
Z = (np.cos(X) * np.sin(Y))
cp = plt.contourf(X, Y, Z)
cb = plt.colorbar(cp)

X, Y = np.mgrid[-6.6: 6.6, -6.6: 6.6]
U = np.cos(X)
V = np.sin(Y)
quiv = plt.quiver(X, Y, U, V)



plt.show()