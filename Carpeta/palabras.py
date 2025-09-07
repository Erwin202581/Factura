
import random

PALABRAS = [
    "mesa", "silla", "llave", "plato", "guerra", "maestro", "helado",
            "galleta", "pantalla", "sistema", "desarrollo", "resultados", "portapapeles"
]

def elegir(nivel=None):
    """Devuelve una palabra según el nivel (opcional)."""
    if nivel is None:
        return random.choice(PALABRAS)
    if nivel == 1:
        opciones = [p for p in PALABRAS if len(p) <= 4]
    elif nivel == 2:
        opciones = [p for p in PALABRAS if 5 <= len(p) <= 7]
    else:
        opciones = [p for p in PALABRAS if len(p) >= 8]
    return random.choice(opciones) if opciones else random.choice(PALABRAS)
