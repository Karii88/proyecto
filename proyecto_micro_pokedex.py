#EO
#---------------Funciones----------------------------
def caracteristicas_pokemon(statspoke,movpoke,evolpoke):
    return statspoke + "\n" + movpoke + "\n" + evolpoke

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
statspoke1 = "-Estas son sus características base de combate:\n PS: 100\n Ataque: 125\n Defensa: 90\n At.esp.: 60\n Def.esp.: 70\n Velocidad: 85"
statspoke2 = "-Estas son sus características base de combate:\n PS: 80\n Ataque: 116\n Defensa: 75\n At.esp.: 65\n Def.esp.: 75\n Velocidad: 119"
statspoke3 = "-Estas son sus características base de combate:\n PS: 70\n Ataque: 85\n Defensa: 65\n At.esp.: 125\n Def.esp.: 65\n Velocidad: 120"
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
#--------------Condicionales------------------------
if respuesta_usuario == poke1:
    print(caracteristicas_pokemon(statspoke1,movpoke1,evolpoke1))
    
elif respuesta_usuario == poke2:
    print(caracteristicas_pokemon(statspoke2,movpoke2,evolpoke2))
    
elif respuesta_usuario == poke3:
    print(caracteristicas_pokemon(statspoke3,movpoke3,evolpoke3))

else:
    print("No se encontró el Pokémon que buscas")
#--------------------------------------------------------------
print("-Comparando puntos de vida, los más altos son: ", puntos_vida(100,80,70), "correspondientes a :", poke1)

print("-Comparando puntos de ataque, los más altos son: ", puntos_ataque(125,116,85), "correspondientes a :", poke1)

print("-Comparando puntos de defensa, los más altos son: ", puntos_defensa(90,75,65), "correspondientes a :", poke1)

print("-Comparando puntos de ataque especial, los más altos son: ", puntos_at_esp(60,65,125), "correspondientes a :", poke3)

print("-Comparando puntos de defensa especial, los más altos son: ", puntos_def_esp(70,75,65), "correspondientes a :", poke2)

print("-Comparando puntos de velocidad, los más altos son: ", puntos_velocidad(85,119,120), "correspondientes a :", poke3)

#EF
print("¡Gracias por consultar en la micro pokédex!")


    
