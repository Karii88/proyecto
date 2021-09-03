#EO
#-------------Variables------------------
poke1="Rillaboom"
poke2="Cinderace"
poke3="Inteleon"
statspoke1 = ("PS: 100\n Ataque: 125\n Defensa: 90\n At.esp.: 60\n Def.esp.: 70\n Velocidad: 85")
statspoke2 = ("PS: 80\n Ataque: 116\n Defensa: 75\n At.esp.: 65\n Def.esp.: 75\n Velocidad: 119")
statspoke3 = ("PS: 70\n Ataque: 85\n Defensa: 65\n At.esp.: 125\n Def.esp.: 65\n Velocidad: 120")
movpoke1 = ("Batería asalto\n Doble golpe\n Campo de hierba\n Rugido de guerra\n Arañazo\n Gruñido\n Punzada rama\n Mofa\n Hoja afilada\n Chirrido\n Desarme\n Atizar\n Alboroto\n Mazazo\n Esfuerzo\n Estruendo")
movpoke2 = ("Balon ígneo\n Amago\n Placaje\n Gruñido\n Ascuas\n Ataque rápido\n Doble patada\n Nitrocarga\n Agilidad\n Golpe cabeza\n Contraataque\n Bote\n Doble filo\n Cambio de cancha")
movpoke3 = ("Disparo certero\n Acróbata\n Destructor\n Gruñido\n Pistola agua\n Atadura\n Hidropulso\n Ojos llorosos\n Golpe bajo\n Ida y vuelta\n Hidroariete\n Anegar\n Danza lluvia\n Hidrobomba")
evolpoke1 = ("Grookey\n Thwackey")
evolpoke2 = ("Scorbunny\n Raboot")
evolpoke3 = ("Sobble\n Drizzile")
#-------------Instrucciones para el usuario--------
print("Estos son los Pokémon iniciales consultables de la región de Galar:", poke1, poke2, poke3)
print("Teclea correctamente el nombre del Pokémon que deseas consultar:")

respuesta_usuario=str(input())
#--------------Condicionales------------------------
if respuesta_usuario == poke1:
    print("-Estas son sus características base de combate:\n",statspoke1)
    print("-Estos son los movimientos que puede aprender subiendo de nivel:\n",movpoke1)
    print("-Estas son sus pre-evoluciones:\n",evolpoke1)
elif respuesta_usuario == poke2:
    print("-Estas son sus características base de combate:\n",statspoke2)
    print("-Estos son los movimientos que puede aprender subiendo de nivel:\n",movpoke2)
    print("-Estas son sus pre-evoluciones:\n",evolpoke2)
elif respuesta_usuario == poke3:
    print("-Estas son sus características base de combate:\n",statspoke3)
    print("-Estos son los movimientos que puede aprender subiendo de nivel:\n",movpoke3)
    print("-Estas son sus pre-evoluciones:\n",evolpoke3)

else:
    print("No se encontró el Pokémon que buscas")
#---------------Funciones----------------------------
def puntos_vida(ps1, ps2, ps3):
    return max(ps1, ps2, ps3)
print("-Comparando puntos de vida, los más altos son: ", puntos_vida(100,80,70), "correspondientes a :", poke1)

def puntos_ataque(ataque1, ataque2, ataque3):
    return max(ataque1, ataque2, ataque3)
print("-Comparando puntos de ataque, los más altos son: ", puntos_ataque(125,116,85), "correspondientes a :", poke1)

def puntos_defensa(defensa1, defensa2, defensa3):
    return max(defensa1, defensa2, defensa3)
print("-Comparando puntos de defensa, los más altos son: ", puntos_defensa(90,75,65), "correspondientes a :", poke1)

def puntos_at_esp(at_esp1, at_esp2, at_esp3):
    return max(at_esp1, at_esp2, at_esp3)
print("-Comparando puntos de ataque especial, los más altos son: ", puntos_at_esp(60,65,125), "correspondientes a :", poke3)

def puntos_def_esp(def_esp1, def_esp2, def_esp3):
    return max(def_esp1, def_esp2, def_esp3)
print("-Comparando puntos de defensa especial, los más altos son: ", puntos_def_esp(70,75,65), "correspondientes a :", poke2)

def puntos_velocidad(velocidad1, velocidad2, velocidad3):
    return max(velocidad1, velocidad2, velocidad3)
print("-Comparando puntos de velocidad, los más altos son: ", puntos_velocidad(85,119,120), "correspondientes a :", poke3)

#EF
print("¡Gracias por consultar en la micro pokédex!")


    
