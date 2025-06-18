import random

def adivina_numero():
    numero_secreto = random.randint(1, 20) #randint() es una función específica dentro de random que genera un número entero aleatorio (de ahí "rand-int").
    intentos_maximos = 5
    intentos_realizados = 0

    print('Estoy pensando en un número del 1 al 20...')
    print('¿Puedes adivinarlo?')
    print(f'Tines {intentos_maximos} intentos. ¿Te ves capaz?')

    suposicion_int = 0 #Se pone para que se inicie el bulge

    while suposicion_int != numero_secreto and intentos_realizados < intentos_maximos:
        try:
            suposicion_str=input('Adivina el número:')
            suposicion_int = int(suposicion_str)
        except ValueError:
            print('Mmm... Creo que eso no es un número.')
            continue

        intentos_realizados += 1

        if suposicion_int == numero_secreto:
            print(f'Felicidades has acertado, ese era mi número. Has acertado con {intentos_realizados} intentos.')
            break # Salir del bucle
        elif suposicion_int < numero_secreto:
            print('Estás cerca, mi número es mayor.')
        else:
            print('Casi, te pasaste, el número menor.')
        
        if suposicion_int != numero_secreto and intentos_realizados<intentos_maximos:
            intentos_restantes = intentos_maximos - intentos_realizados
            print(f'Te quedan {intentos_restantes} intentos.')
    
    if suposicion_int != numero_secreto and intentos_realizados == intentos_maximos:
        print(f'¡Oh no! Te has quedado sin intentos lo siento. El número secreto era {numero_secreto}.')

    print('¡Gracias por jugar! :D')

adivina_numero()

jugar_otra_vez = True


