#EO
#---------------Funciones----------------------------
def consulta_pokemon(respuesta_usuario):
    while respuesta_usuario not in pokemones:

        print("No se encontró el Pokémon que buscas, vuelve a intentarlo")
        respuesta_usuario=str(input())

    if respuesta_usuario == pokemones[0]:
        print("-Estas son sus características base de combate:")
        print(" PS:",ps[0])
        print(" Ataque:",ataque[0])
        print(" Defensa:",defensa[0])
        print(" Ataque especial:",at_esp[0])
        print(" Defensa especial:",def_esp[0])
        print(" Velocidad:",velocidad[0])
        print(caracteristicas_pokemon(movpoke1,evolpoke1))
                
    elif respuesta_usuario == pokemones[1]:
        print("-Estas son sus características base de combate:")
        print(" PS:",ps[1])
        print(" Ataque:",ataque[1])
        print(" Defensa:",defensa[1])
        print(" Ataque especial:",at_esp[1])
        print(" Defensa especial:",def_esp[1])
        print(" Velocidad:",velocidad[1])
        print(caracteristicas_pokemon(movpoke2,evolpoke2))
                
    elif respuesta_usuario == pokemones[2]:
        print("-Estas son sus características base de combate:")
        print(" PS:",ps[2])
        print(" Ataque:",ataque[2])
        print(" Defensa:",defensa[2])
        print(" Ataque especial:",at_esp[2])
        print(" Defensa especial:",def_esp[2])
        print(" Velocidad:",velocidad[2])
        print(caracteristicas_pokemon(movpoke3,evolpoke3))

def caracteristicas_pokemon(movpoke,evolpoke):
    return movpoke + "\n" + evolpoke

def puntos_vida(ps1, ps2, ps3):
    return max(ps1, ps2, ps3)

def puntos_ataque(ataque1, ataque2, ataque3):
    return max(ataque1, ataque2, ataque3)

def puntos_defensa(defensa1, defensa2, defensa3):
    return max(defensa1, defensa2, defensa3)

def puntos_at_esp(at_esp1, at_esp2, at_esp3):
    return max(at_esp1, at_esp2, at_esp3)

def puntos_def_esp(def_esp1, def_esp2, def_esp3):
    return max(def_esp1, def_esp2, def_esp3)

def puntos_velocidad(velocidad1, velocidad2, velocidad3):
    return max(velocidad1, velocidad2, velocidad3)

#-------------Variables------------------
poke1="Rillaboom"
poke2="Cinderace"
poke3="Inteleon"
pokemones=["Rillaboom","Cinderace","Inteleon"]
ps=["100","80","70"]
ataque=["125","116","85"]
defensa=["90","75","65"]
at_esp=["60","65","125"]
def_esp=["70","75","65"]
velocidad=["85","119","120"]
movpoke1 = "-Estos son los movimientos que puede aprender subiendo de nivel:\n Batería asalto\n Doble golpe\n Campo de hierba\n Rugido de guerra\n Arañazo\n Gruñido\n Punzada rama\n Mofa\n Hoja afilada\n Chirrido\n Desarme\n Atizar\n Alboroto\n Mazazo\n Esfuerzo\n Estruendo"
movpoke2 = "-Estos son los movimientos que puede aprender subiendo de nivel:\n Balon ígneo\n Amago\n Placaje\n Gruñido\n Ascuas\n Ataque rápido\n Doble patada\n Nitrocarga\n Agilidad\n Golpe cabeza\n Contraataque\n Bote\n Doble filo\n Cambio de cancha"
movpoke3 = "-Estos son los movimientos que puede aprender subiendo de nivel:\n Disparo certero\n Acróbata\n Destructor\n Gruñido\n Pistola agua\n Atadura\n Hidropulso\n Ojos llorosos\n Golpe bajo\n Ida y vuelta\n Hidroariete\n Anegar\n Danza lluvia\n Hidrobomba"
evolpoke1 = "-Estas son sus pre-evoluciones:\n Grookey\n Thwackey"
evolpoke2 = "-Estas son sus pre-evoluciones:\n Scorbunny\n Raboot"
evolpoke3 = "-Estas son sus pre-evoluciones:\n Sobble\n Drizzile"
#-------------Instrucciones para el usuario--------
print("Estos son los Pokémon iniciales consultables de la región de Galar:", poke1, poke2, poke3)
print("Teclea correctamente el nombre del Pokémon que deseas consultar:")

respuesta_usuario=str(input())
consulta_pokemon(respuesta_usuario)
#--------------------------------------------------------------
print("-Comparando puntos de vida, los más altos son: ", puntos_vida(100,80,70), "correspondientes a :", pokemones[0])

print("-Comparando puntos de ataque, los más altos son: ", puntos_ataque(125,116,85), "correspondientes a :", pokemones[0])

print("-Comparando puntos de defensa, los más altos son: ", puntos_defensa(90,75,65), "correspondientes a :", pokemones[0])

print("-Comparando puntos de ataque especial, los más altos son: ", puntos_at_esp(60,65,125), "correspondientes a :", pokemones[2])

print("-Comparando puntos de defensa especial, los más altos son: ", puntos_def_esp(70,75,65), "correspondientes a :", pokemones[1])

print("-Comparando puntos de velocidad, los más altos son: ", puntos_velocidad(85,119,120), "correspondientes a :", pokemones[2])
#---------------------------------------------------------------
print("¿Deseas consultar otro pokémon? Teclea 'si' o 'no'")
nueva_consulta=str(input())

while nueva_consulta != "no" and nueva_consulta != "si":
    print("No existe esa opción, vuelve a intentarlo")
    print("¿Deseas consultar otro pokémon? Teclea 'si' o 'no'")
    nueva_consulta=str(input())
    
while nueva_consulta == "si":
    print("Teclea correctamente el nombre del Pokémon que deseas consultar:")
    respuesta_usuario=str(input())
    consulta_pokemon(respuesta_usuario)
    print("¿Deseas consultar otro pokémon? Teclea 'si' o 'no'")
    nueva_consulta=str(input())
        
#EF
print("¡Gracias por consultar en la micro pokédex!")



    
