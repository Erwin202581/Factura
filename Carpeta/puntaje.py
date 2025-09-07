

def crear_jugador(intentos=3):
    return {"puntos": 0, "intentos": intentos}

def premio(jugador, puntos=1):
    jugador["puntos"] += puntos

def falla(jugador):
    jugador["intentos"] -= 1

def mostrar_estado(jugador):
    print(f"Puntos: {jugador['puntos']} | Intentos: {jugador['intentos']}")
