
import random

def mezclar_palabra(palabra):
    letras = list(palabra)
    random.shuffle(letras)
    mezcla = "".join(letras)
    
    while mezcla == palabra:
        random.shuffle(letras)
        mezcla = "".join(letras)
    return mezcla

def jugar_ronda(palabra):
    mezcla = mezclar_palabra(palabra)
    print(f"Adivina la palabra: {mezcla}")
    respuesta = input("Tu respuesta: ").strip().lower()
    return respuesta == palabra  
