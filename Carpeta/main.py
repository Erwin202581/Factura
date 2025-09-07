
from palabras import elegir
from juego import jugar_ronda
from puntaje import crear_jugador, premio, falla, mostrar_estado


def main():
    jugador = crear_jugador(intentos=3)

    while jugador["intentos"] > 0:
        palabra = elegir()
        acertó = jugar_ronda(palabra)
        if acertó:
            print("✅ Correcto!")
            premio(jugador)
        else:
            print(f"❌ Incorrecto. La palabra era: {palabra}")
            falla(jugador)
        mostrar_estado(jugador)

    print("🎮 Fin del juego")
    print("Puntaje final:", jugador["puntos"])


if __name__ == "__main__":
    main()
