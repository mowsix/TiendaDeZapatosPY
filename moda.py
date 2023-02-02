def obtenerTallaModa(arrayTallasVendidas):
    return max(set(arrayTallasVendidas), key=arrayTallasVendidas.count)


