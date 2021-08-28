#EO
#-------------Variables------------------
poke1="Rillaboom"
poke2="Cinderace"
poke3="Inteleon"
ps1=100
ps2=80
ps3=70
ataque1=125
ataque2=116
ataque3=85
defensa1=90
defensa2=75
defensa3=65
at_esp1=60
at_esp2=65
at_esp3=125
def_esp1=70
def_esp2=75
def_esp3=65
velocidad1=85
velocidad2=119
velocidad3=120
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
    suma_puntos=ps1+ataque1+defensa1+at_esp1+def_esp1+velocidad1
    print("-Estas son sus características base de combate:\n",statspoke1)
    print("-Sus puntos de combate totales son:",suma_puntos)
    print("-Estos son los movimientos que puede aprender subiendo de nivel:\n",movpoke1)
    print("-Estas son sus pre-evoluciones:\n",evolpoke1)
elif respuesta_usuario == poke2:
    suma_puntos=ps2+ataque2+defensa2+at_esp2+def_esp2+velocidad2
    print("-Estas son sus características base de combate:\n",statspoke2)
    print("-Sus puntos de combate totales son:",suma_puntos)
    print("-Estos son los movimientos que puede aprender subiendo de nivel:\n",movpoke2)
    print("-Estas son sus pre-evoluciones:\n",evolpoke2)
elif respuesta_usuario == poke3:
    suma_puntos=ps3+ataque3+defensa3+at_esp3+def_esp3+velocidad3
    print("-Estas son sus características base de combate:\n",statspoke3)
    print("-Sus puntos de combate totales son:",suma_puntos)
    print("-Estos son los movimientos que puede aprender subiendo de nivel:\n",movpoke3)
    print("-Estas son sus pre-evoluciones:\n",evolpoke3)

else:
    print("No se encontró el Pokémon que buscas")

print("-Diferencia en Puntos de vida")
if ps1>ps2:
    dif_ps=ps1-ps2
    print(" La vida de",poke1,"es mayor que la de",poke2,"por la cantidad de:",dif_ps)
if ps1>ps3:
    dif_ps=ps1-ps3
    print(" La vida de",poke1,"es mayor que la de",poke3,"por la cantidad de:",dif_ps)
if ps2>ps3:
    dif_ps=ps2-ps3
    print(" La vida de",poke2,"es mayor que la de",poke3,"por la cantidad de:",dif_ps)
if ps1<ps2:
    dif_ps=ps2-ps1
    print(" La vida de",poke1,"es menor que la de",poke2,"por la cantidad de:",dif_ps)
if ps1<ps3:
    dif_ps=ps3-ps1
    print(" La vida de",poke1,"es menor que la de",poke3,"por la cantidad de:",dif_ps)
if ps2<ps3:
    dif_ps=ps3-ps2
    print(" La vida de",poke2,"es menor que la de",poke3,"por la cantidad de:",dif_ps)

print("-Diferencia en Puntos de ataque")
if ataque1>ataque2:
    dif_ataque=ataque1-ataque2
    print(" El ataque de",poke1,"es mayor que el de",poke2,"por la cantidad de:",dif_ataque)
if ataque1>ataque3:
    dif_ataque=ataque1-ataque3
    print(" El ataque de",poke1,"es mayor que el de",poke3,"por la cantidad de:",dif_ataque)
if ataque2>ataque3:
    dif_ataque=ataque2-ataque3
    print(" El ataque de",poke2,"es mayor que el de",poke3,"por la cantidad de:",dif_ataque)
if ataque1<ataque2:
    dif_ataque=ataque2-ataque1
    print(" El ataque de",poke1,"es menor que el de",poke2,"por la cantidad de:",dif_ataque)
if ataque1<ataque3:
    dif_ataque=ataque3-ataque1
    print(" El ataque de",poke1,"es menor que el de",poke3,"por la cantidad de:",dif_ataque)
if ataque2<ataque3:
    dif_ataque=ataque3-ataque2
    print(" El ataque de",poke2,"es menor que el de",poke3,"por la cantidad de:",dif_ataque)

print("-Diferencia en Puntos de defensa")
if defensa1>defensa2:
    dif_defensa=defensa1-defensa2
    print(" La defensa de",poke1,"es mayor que la de",poke2,"por la cantidad de:",dif_defensa)
if defensa1>defensa3:
    dif_defensa=defensa1-defensa3
    print(" La defensa de",poke1,"es mayor que la de",poke3,"por la cantidad de:",dif_defensa)
if defensa2>defensa3:
    dif_defensa=defensa2-defensa3
    print(" La defensa de",poke2,"es mayor que la de",poke3,"por la cantidad de:",dif_defensa)
if defensa1<defensa2:
    dif_defensa=defensa2-defensa1
    print(" La defensa de",poke1,"es menor que la de",poke2,"por la cantidad de:",dif_defensa)
if defensa1<defensa3:
    dif_defensa=defensa3-defensa1
    print(" La defensa de",poke1,"es menor que la de",poke3,"por la cantidad de:",dif_defensa)
if defensa2<defensa3:
    dif_defensa=defensa3-defensa2
    print(" La defensa de",poke2,"es menor que la de",poke3,"por la cantidad de:",dif_defensa)

print("-Diferencia en Puntos de ataque especial")
if at_esp1>at_esp2:
    dif_at_esp=at_esp1-at_esp2
    print(" El ataque especial de",poke1,"es mayor que el de",poke2,"por la cantidad de:",dif_at_esp)
if at_esp1>at_esp3:
    dif_at_esp=at_esp1-at_esp3
    print(" El ataque especial de",poke1,"es mayor que el de",poke3,"por la cantidad de:",dif_at_esp)
if at_esp2>at_esp3:
    dif_at_esp=at_esp2-at_esp3
    print(" El ataque especial de",poke2,"es mayor que el de",poke3,"por la cantidad de:",dif_at_esp)
if at_esp1<at_esp2:
    dif_at_esp=at_esp2-at_esp1
    print(" El ataque especial de",poke1,"es menor que el de",poke2,"por la cantidad de:",dif_at_esp)
if at_esp1<at_esp3:
    dif_at_esp=at_esp3-at_esp1
    print(" El ataque especial de",poke1,"es menor que el de",poke3,"por la cantidad de:",dif_at_esp)
if at_esp2<at_esp3:
    dif_at_esp=at_esp3-at_esp2
    print(" El ataque especial de",poke2,"es menor que el de",poke3,"por la cantidad de:",dif_at_esp)

print("-Diferencia en Puntos de defensa especial")
if def_esp1>def_esp2:
    dif_def_esp=def_esp1-def_esp2
    print(" La defensa especial de",poke1,"es mayor que la de",poke2,"por la cantidad de:",dif_def_esp)
if def_esp1>def_esp3:
    dif_def_esp=def_esp1-def_esp3
    print(" La defensa especial de",poke1,"es mayor que la de",poke3,"por la cantidad de:",dif_def_esp)
if def_esp2>def_esp3:
    dif_def_esp=def_esp2-def_esp3
    print(" La defensa especial de",poke2,"es mayor que la de",poke3,"por la cantidad de:",dif_def_esp)
if def_esp1<def_esp2:
    dif_def_esp=def_esp2-def_esp1
    print(" La defensa especial de",poke1,"es menor que la de",poke2,"por la cantidad de:",dif_def_esp)
if def_esp1<def_esp3:
    dif_def_esp=def_esp3-def_esp1
    print(" La defensa especial de",poke1,"es menor que la de",poke3,"por la cantidad de:",dif_def_esp)
if def_esp2<def_esp3:
    dif_def_esp=def_esp3-def_esp2
    print(" La defensa especial de",poke2,"es menor que la de",poke3,"por la cantidad de:",dif_def_esp)

print("-Diferencia en Puntos de Velocidad")
if velocidad1>velocidad2:
    dif_velocidad=velocidad1-velocidad2
    print(" La Velocidad de",poke1,"es mayor que la de",poke2,"por la cantidad de:",dif_velocidad)
if velocidad1>velocidad3:
    dif_velocidad=velocidad1-velocidad3
    print(" La Velocidad de",poke1,"es mayor que la de",poke3,"por la cantidad de:",dif_velocidad)
if velocidad2>velocidad3:
    dif_velocidad=velocidad2-velocidad3
    print(" La Velocidad de",poke2,"es mayor que la de",poke3,"por la cantidad de:",dif_velocidad)
if velocidad1<velocidad2:
    dif_velocidad=velocidad2-velocidad1
    print(" La Velocidad de",poke1,"es menor que la de",poke2,"por la cantidad de:",dif_velocidad)
if velocidad1<velocidad3:
    dif_velocidad=velocidad3-velocidad1
    print(" La Velocidad de",poke1,"es menor que la de",poke3,"por la cantidad de:",dif_velocidad)
if velocidad2<velocidad3:
    dif_velocidad=velocidad3-velocidad2
    print(" La Velocidad de",poke2,"es menor que la de",poke3,"por la cantidad de:",dif_velocidad)

#EF
print("Gracias por consultar en la micro pokédex")


    
