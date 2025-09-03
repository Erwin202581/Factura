
def aplicar_descuento_o_recargo(unidades_totales, total_general, num_productos):
    """
    Aplica descuento o recargo según la cantidad de unidades compradas.
    """
    if unidades_totales > 100:
        descuento = total_general * 0.10
        total_general -= descuento
        print(
            f"DESCUENTO APLICADO (10%): -${descuento:,.0f}".replace(",", "."))
    elif unidades_totales == 90:
        descuento = total_general * 0.09
        total_general -= descuento
        print(f"DESCUENTO APLICADO (9%): -${descuento:,.0f}".replace(",", "."))
    elif unidades_totales == num_productos:
        recargo = total_general * 0.005
        total_general += recargo
        print(f"RECARGO (0.5%): +${recargo:,.0f}".replace(",", "."))

    return total_general
