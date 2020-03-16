from Usuario import Usuario
def Estadisticas(edit = False): #Funcion para ver las estadisticas de los usaruis
    usuarios = []
    with open("Estadisticas.txt", "r") as bd: #Se abre  los datos de los usuarios en el archivos txt
        datos = bd.readlines()
    Edad5al18 = 0
    Edad19al45= 0
    Edad46al60= 0          #datos para usar mas adelante en la funcion
    Edad61al95= 0  
    Puntos_Masculios = 0
    Puntos_Femeninos = 0
    Disparos_totales = 0
    Promedio = 0
    for dato in datos:   #se usa for para ir agregando los datos a la variables ya creadas 
        Promedio = Promedio + 1
        usuario = dato[:-1].split(',') 
        Edad = int(usuario[0])
        if usuario[1] == "Femenino":
            Puntos_Femeninos = Puntos_Femeninos + int(usuario[2]) #Se agregan los puntos totales femeninos
        else:
            Puntos_Masculios = Puntos_Masculios + int(usuario[2]) #Se agregan los puntos totales Masculinos
        if Edad > 0 and Edad < 19:  
            Edad5al18 = Edad5al18+1
        elif Edad > 18 and Edad < 46:
            Edad19al45 = Edad19al45 + 1          #Se van agregando la cantidad de personas que haya por edades 
        elif Edad > 45 and Edad < 61:
            Edad46al60 = Edad46al60 + 1
        elif Edad > 61:
            Edad61al95 = Edad61al95 +1     
        Disparos_totales = Disparos_totales + int(usuario[3])  #se hace el promedio de disparos total

    print("Cantidad de jugadores con la edad de 5-18:",Edad5al18) 
    print("Cantidad de jugadores con la edad de 19-45:",Edad19al45) 
    print("Cantidad de jugadores con la edad de 46-60:",Edad46al60)    
    print("Cantidad de jugadores con la edad de 61-95:",Edad61al95)             #Se imprimen las estadisticas
    print("Puntos Totales por Jugadores Masculino:",Puntos_Masculios) 
    print("Puntos Totales por Jugadores Femeninos:",Puntos_Femeninos) 
    Promedio_disparos = Disparos_totales / Promedio
    print("Promedio de disparos para ganar:",Promedio_disparos)       


    

        