
from fac2 import encabezado
from fac3 import datos_cliente
from fac4 import productos, cantidades, precios
from fac5 import calcular_totales
from fac6 import aplicar_descuento_o_recargo


encabezado()


print(f"Cliente: {datos_cliente['cliente']}")
print(f"Fecha:   {datos_cliente['fecha']}")
print(f"Nit:     {datos_cliente['nit']}")
print("="*60)


subtotales, ivas, totales = calcular_totales(productos, cantidades, precios)

print("{:<12} {:<10} {:<15} {:<15} {:<15}".format(
    "Producto", "Cantidad", "Precio", "IVA", "Total"))
print("-"*60)

total_general = 0
unidades_totales = sum(cantidades)

for i in range(len(productos)):
    print("{:<12} {:<10} {:<15} {:<15} {:<15}".format(
        productos[i],
        cantidades[i],
        f"${precios[i]:,}".replace(",", "."),
        f"${ivas[i]:,.0f}".replace(",", "."),
        f"${totales[i]:,.0f}".replace(",", ".")
    ))
    total_general += totales[i]

print("-"*60)

total_general = aplicar_descuento_o_recargo(
    unidades_totales, total_general, len(productos))

print(f"{'TOTAL A PAGAR':<45} ${total_general:,.0f}".replace(",", "."))
print("="*60)
print("Gracias por su compra!")
