#Variables y tipos
#Una variable es sólo un lugar para asignar un valor que podría cambiar a un nombre. El hecho de que pueda cambiar es lo que la convierte en una variable.  

phone_count = 9                 # int
phone_width_inches = 2.54       # float
phone_height_inches = 6.20      # float
phone_make = "Example"          # str
phone_model = "i2000"           # str
phone_available = True          # bool

phone_area = phone_width_inches * phone_height_inches
phone_name = f"{phone_make} {phone_model}"
print(f"{phone_name} is {phone_area:.5} square inches")


#Condicionales
#Las condicionales deciden qué líneas del código se ejecutan, qué ruta a través de su código toma la ejecución.
#Lea el código siguiente. Intente adivinar cuál será la salida antes de ejecutar el código. También puede realizar algunos cambios en el código y volver a ejecutarlo para comprobar sus suposiciones.

number_one = 7
number_two = 5

if number_one > number_two:
    print("number one is greater than number 2")
if number_two > number_one:
    print("number two is greater than number 1")
if number_one == number_two:
    print("the numbers are equal")

#Funciones
#Una función es un bloque con nombre de código reutilizable que realiza una tarea específica. Usted utiliza funciones para ayudar a organizar y simplificar su código, haciéndolo más fácil de entender y mantener.
#Actualice la función siguiente para calcular correctamente el cuadrado del número de la variable parámetro.  Utilice el botón de ejecución para probar sus cambios.

def square_number(number):
    # Fix the calculation below
    return number * number

#Listas y diccionarios
#Una lista es "una lista de elementos". Podemos construir una lista poniendo los elementos dentro de corchetes.

# constructing a list
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
capacities = [10000, 12000, 9000, 8000, 10000, 11000, 9000]

# operations on a list
print(sum(capacities) / len(capacities))
capacities.append(12000)
capacities.insert(0, 1000)
capacities.remove(9000)
print(colors.index('Blue'))
print('Red' in colors)
print('Red' not in colors)

# accessing items in a list
colors[0] = "Bright Red"
print(colors[0])
print(capacities[1])

#También puede trocear una lista.  Al trocear una lista se crea una copia de la misma, y puede controlar los índices que desea incluir en la nueva lista.  Los parámetros que pasamos son los índices de y a y, opcionalmente, un paso. 

colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

# slice: list[from:to:step]
print(colors[:]) 
print(colors[2:])
print(colors[:3])
print(colors[-4:])

print(colors[::-1])
print(colors[::2])

#Un diccionario nos proporciona un mapeo simple de una clave a un valor. En otros lenguajes de programación puede que haya oído hablar de un "mapa" o un "hashtable". 

#Podemos crear un diccionario con la sintaxis curly brace.

info = {
    'ImageId': 'ami-069eb5ebcbc6b0f91',
    'InstanceId': 'i-0c5c2bb0a41ef1b29',
    'InstanceType': 'm5.large'
}

# With a dictionary use the keys to access values
info['ExtraInfo'] = 'This is extra info'
print(info['ImageId'])


#Bucles
#Hay operaciones que querrá hacer varias veces, digamos que quiero escribir código para enviar 50 correos electrónicos. Lo haré en un bucle.
#Ejecute un bucle simple a continuación. Aquí estamos utilizando una función de rango para crear una secuencia de números para el bucle.

for i in range(10):
    print(i)

#Podemos operar sobre estructuras de datos como listas y diccionarios en un bucle for.

colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
for c in colors:
    print(c)
    
color_values = { 'Red' : 'ff0000',  'Green' : '008000', 'Blue' : '0000ff'}
for k in color_values:
    print(k, color_values[k])

#Comprensiones de listas
#Utilizamos las comprensiones de lista para construir una nueva lista utilizando una sintaxis que se parece mucho a la de un bucle for.

colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

# build a list of the colors uppercased
print( [ c.upper() for c in colors ] )

# build a list of colors that start with G
print( [ c for c in colors if c.startswith('G') ] )