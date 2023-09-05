if True:
    print('debería ejecutarse')

if False:
    print('Nnca se ejecuta')


pet = input('¿Cúal es tu mascota favorita? ')

if pet == 'perro':
    print('Genial tienes buen gusto')

elif pet == 'gato':
    print('espero tengas suerte')

elif pet == 'pez':
    print('eres lo maximo')

else:
    print('No tienes ninguna mascota interesante')

'''
stock = int(input('Digita el stock => '))

if stock>=102 and stock <=1002:
    print ('el stock es correcto')
else:
    print('el stock es incorrecto')


Programa que evalua si un numero es par o inpar
'''

numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("Este numero es par")
else:
    print("Este numero es impar")    

