# fac5.py
def calcular_totales(productos, cantidades, precios):
    ivas = []
    subtotales = []
    totales = []

    for i in range(len(productos)):
        subtotal = cantidades[i] * precios[i]
        iva = precios[i] * 0.19
        total = subtotal + (iva * cantidades[i])

        subtotales.append(subtotal)
        ivas.append(iva)
        totales.append(total)

    return subtotales, ivas, totales
