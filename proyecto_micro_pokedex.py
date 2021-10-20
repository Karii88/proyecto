"""
Proyecto Micro Pokédex.
Karina Damaris Avila Castillo. A01705203
Programa de consulta de información de ciertos pokémon.
El programa presenta al usuario los pokémon consultables dentro del programa
para que el usuario pueda consultar los datos relacionados a los pokémon de su
interés así como una comparación entre los puntos que posee cada uno para conocer
aquel con mejores estadísticas.
"""

#---------------Funciones----------------------------
def consulta_pokemon(respuesta_usuario):
    """
    recibe: respuesta_usuario cadena de caracteres
    compara si la respuesta del usuario se encuentra dentro de los pokémon consultables
    devuelve: se manda a llamar una segunda y tercera función con las variables
              correspondientes al pokémon consultado para imprimirlas en pantalla
    """

    while respuesta_usuario not in pokemones:

        print("No se encontró el Pokémon que buscas, vuelve a intentarlo")
        respuesta_usuario=str(input())

    if respuesta_usuario == pokemones[0]:
        print("-Estas son sus características base de combate:")
        datos_pokemon(pokemon1)
        print()
        print(caracteristicas_pokemon(movpoke1,evolpoke1))
             
    elif respuesta_usuario == pokemones[1]:
        print("-Estas son sus características base de combate:")
        datos_pokemon(pokemon2)
        print()
        print(caracteristicas_pokemon(movpoke2,evolpoke2))
                
    elif respuesta_usuario == pokemones[2]:
        print("-Estas son sus características base de combate:")
        datos_pokemon(pokemon3)
        print()
        print(caracteristicas_pokemon(movpoke3,evolpoke3))

def datos_pokemon(datos):
    """
    recibe: datos matriz
    devuelve: se recorre la matriz que contiene las estadísticas del
              pokémon y va imprimiendo el contenido de la misma.
    """
    for linea in datos:
      for columna in linea:
        print(columna, end = " ")
      print()

def caracteristicas_pokemon(movpoke,evolpoke):
    """
    recibe: movpoke cadena de caracteres, evolpoke cadena de caracteres
    devuelve: se envían los movimientos y evoluciones del pokémon consultado
              a la función que mandó llamar a esta segunda función.
    """
    return movpoke + "\n" + evolpoke

def puntos_vida(ps1, ps2, ps3):
    """
    recibe: ps1 valor numérico, ps2 valor numérico, ps3 valor numérico
    se obtiene el valor máximo entre los valores numéricos que recibe la función
    devuelve: valor máximo numérico de los puntos de vida
    """
    return max(ps1, ps2, ps3)

def puntos_ataque(ataque1, ataque2, ataque3):
    """
    recibe: ataque1 valor numérico, ataque2 valor numérico, ataque3 valor numérico
    se obtiene el valor máximo entre los valores numéricos que recibe la función
    devuelve: valor máximo numérico de los puntos de ataque
    """
    return max(ataque1, ataque2, ataque3)

def puntos_defensa(defensa1, defensa2, defensa3):
    """
    recibe: defensa1 valor numérico, defensa2 valor numérico, defensa3 valor numérico
    se obtiene el valor máximo entre los valores numéricos que recibe la función
    devuelve: valor máximo numérico de los puntos de defensa
    """
    return max(defensa1, defensa2, defensa3)

def puntos_at_esp(at_esp1, at_esp2, at_esp3):
    """
    recibe: at_esp1 valor numérico, at_esp2 valor numérico, at_esp3 valor numérico
    se obtiene el valor máximo entre los valores numéricos que recibe la función
    devuelve: valor máximo numérico de los puntos de ataque especial
    """
    return max(at_esp1, at_esp2, at_esp3)

def puntos_def_esp(def_esp1, def_esp2, def_esp3):
    """
    recibe: def_esp1 valor numérico, def_esp2 valor numérico, def_esp3 valor numérico
    se obtiene el valor máximo entre los valores numéricos que recibe la función
    devuelve: valor máximo numérico de los puntos de defensa especial
    """
    return max(def_esp1, def_esp2, def_esp3)

def puntos_velocidad(velocidad1, velocidad2, velocidad3):
    """
    recibe: velocidad1 valor numérico, velocidad2 valor numérico, velocidad3 valor numérico
    se obtiene el valor máximo entre los valores numéricos que recibe la función
    devuelve: valor máximo numérico de los puntos de velocidad
    """
    return max(velocidad1, velocidad2, velocidad3)

#Variables,listas y matrices

#--------------------------Variables--------------

movpoke1 = "-Estos son los movimientos que puede aprender subiendo de nivel:\n Batería asalto\n Doble golpe\n Campo de hierba\n Rugido de guerra\n Arañazo\n Gruñido\n Punzada rama\n Mofa\n Hoja afilada\n Chirrido\n Desarme\n Atizar\n Alboroto\n Mazazo\n Esfuerzo\n Estruendo"
movpoke2 = "-Estos son los movimientos que puede aprender subiendo de nivel:\n Balon ígneo\n Amago\n Placaje\n Gruñido\n Ascuas\n Ataque rápido\n Doble patada\n Nitrocarga\n Agilidad\n Golpe cabeza\n Contraataque\n Bote\n Doble filo\n Cambio de cancha"
movpoke3 = "-Estos son los movimientos que puede aprender subiendo de nivel:\n Disparo certero\n Acróbata\n Destructor\n Gruñido\n Pistola agua\n Atadura\n Hidropulso\n Ojos llorosos\n Golpe bajo\n Ida y vuelta\n Hidroariete\n Anegar\n Danza lluvia\n Hidrobomba"
evolpoke1 = "-Estas son sus pre-evoluciones:\n Grookey\n Thwackey"
evolpoke2 = "-Estas son sus pre-evoluciones:\n Scorbunny\n Raboot"
evolpoke3 = "-Estas son sus pre-evoluciones:\n Sobble\n Drizzile"

#--------------------------Listas--------------

pokemones=["Rillaboom","Cinderace","Inteleon"]

#--------------------------Matrices--------------

pokemon1 = [[' Tipo: ','Planta'],
         [' Ps:','100'],
         [' Ataque:','125'],
         [' Defensa:', '90'],
         [' Ataque especial:','60'],
         [' Defensa especial:','70'],
         [' Velocidad:','85']]
pokemon2 = [[' Tipo: ','Fuego'],
         [' Ps:','80'],
         [' Ataque:','116'],
         [' Defensa:', '75'],
         [' Ataque especial:','65'],
         [' Defensa especial:','75'],
         [' Velocidad:','119']]
pokemon3 = [[' Tipo: ','Agua'],
         [' Ps:','70'],
         [' Ataque:','85'],
         [' Defensa:', '65'],
         [' Ataque especial:','125'],
         [' Defensa especial:','65'],
         [' Velocidad:','120']]

#-------------Instrucciones para el usuario--------

print("Estos son los Pokémon iniciales consultables de la región de Galar:", pokemones[0], pokemones[1], pokemones[2])
print("Teclea correctamente el nombre del Pokémon que deseas consultar:")

respuesta_usuario = str(input())
consulta_pokemon(respuesta_usuario)

#-------Comparación entre puntajes de los pokémon---

print("-Comparando puntos de vida, los más altos son: ", puntos_vida(100,80,70), "correspondientes a :", pokemones[0])
print("-Comparando puntos de ataque, los más altos son: ", puntos_ataque(125,116,85), "correspondientes a :", pokemones[0])
print("-Comparando puntos de defensa, los más altos son: ", puntos_defensa(90,75,65), "correspondientes a :", pokemones[0])
print("-Comparando puntos de ataque especial, los más altos son: ", puntos_at_esp(60,65,125), "correspondientes a :", pokemones[2])
print("-Comparando puntos de defensa especial, los más altos son: ", puntos_def_esp(70,75,65), "correspondientes a :", pokemones[1])
print("-Comparando puntos de velocidad, los más altos son: ", puntos_velocidad(85,119,120), "correspondientes a :", pokemones[2])

#--------------Nuevas consultas------------------------

print("¿Deseas consultar otro pokémon? Teclea 'si' o 'no'")
nueva_consulta = str(input())

while nueva_consulta != "no" and nueva_consulta != "si":
    print("No existe esa opción, vuelve a intentarlo")
    print("¿Deseas consultar otro pokémon? Teclea 'si' o 'no'")
    nueva_consulta = str(input())
    
while nueva_consulta == "si":
    print("Teclea correctamente el nombre del Pokémon que deseas consultar:")
    respuesta_usuario = str(input())
    consulta_pokemon(respuesta_usuario)
    print("¿Deseas consultar otro pokémon? Teclea 'si' o 'no'")
    nueva_consulta = str(input())

#EF------Fin del programa-------

print("¡Gracias por consultar en la micro pokédex!")



    
