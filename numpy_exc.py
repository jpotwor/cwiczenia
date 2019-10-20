import numpy as np


tab = np.arange(1, 16)
# print(tab)

tab = np.arange(15).reshape(3, 5)
# print(tab)

# wyciagnac z tab tablice [10 11 12 13 14] i pozniej sama liczbe 8
# print(tab[2])
# print(tab[1][3])

# sprawdzic wymiar, typ obiektu, typ danych
print(tab.size)
print(type(tab))
print(tab.dtype)


# liczby urojone
c = np.array([[1, 2], [3, 4]], dtype=complex)
# print(c)
