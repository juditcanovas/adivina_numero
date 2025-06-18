import random
numero_secreto = random.randint(1, 20) #randint() es una función específica dentro de random que genera un número entero aleatorio (de ahí "rand-int").

print('Estoy pensando en un número del 1 al 20...')
print('¿Puedes adivinarlo?')

suposicion_int = 0 #Se pone para que se inicie el bulge

while suposicion_int != numero_secreto:
    try:
        suposicion_str=input('Adivina el número:')
        suposicion_int = int(suposicion_str)
    except ValueError:
        print('Mmm... Creo que eso no es un número.')
        continue



    if suposicion_int == numero_secreto:
         print('Felicidades has acertado, ese era mi número.')
    
    elif suposicion_int < numero_secreto:
        print('Estás cerca, mi número es mayor.')

    else:
        print('Casi, te pasaste, el número menor.')

print('¡Gracias por jugar! :D')