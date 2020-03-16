import random 
import sys
from Barcos import BuqueMayor
from Barcos import BuqueMenor
from Barcos import Submarino
from Barcos import Submarino2            #se exportan de otros archivos todo las clases, funciones que vamos a necesitar 
from Barcos import Submarino3
from Barcos import Submarino4
from Usuario import Usuario 
from ver import ver

def Juego(): #Se crea la funcion Juego
  ver()       #se llama la funcion ver para enseñar los usuarios disponible y eligir cual usaremos
  usuarios = []
  with open("DatosDeLosUsuarios.txt", "r") as bd: #Se abre  los datos de los usuarios en el archivos txt
       datos = bd.readlines()
  for dato in datos:
       usuario = dato[:-1].split(',')
       usuarios.append(Usuario(usuario[0], usuario[1], usuario[2], usuario[3]))
  largo_usuarios = len(usuarios) 
  print("Porfavor Seleccione El siguiente Usuario:")
  bloqueo = True
  
  while bloqueo == True:          #Con este while vamos a seleccionar el usuario de forma seguro que el usuario no rompa el programa
      bloqueo9 = True
      while bloqueo9 == True:
          seleccion = input("Seleccione el usuario que desea usar (Porfavor introdusca el numero entero correspondido al usuario=")
          try:
            seleccion=int(seleccion)
            bloqueo9= False
            break
          except ValueError:
            print ("ERROR: ingrese numero entero correspondido al usuario")
      if seleccion > 0:
         if seleccion > largo_usuarios:
           print("Porfavor eliga el usuario con el numero correspondido") 
         else:
           bloqueo = False 
      else:
        print("Porfavor eliga el usario con el numero correspondido")  

  with open("DatosDeLosUsuarios.txt", 'r') as bd: 
        datos = bd.readlines()                                #Se guardan los datos del usuario para despues agregarlos en el top 10 y en las estadisticas
        usuario = datos[seleccion - 1][:-1].split(',')      

  Bloque1 = True
  Bloque2 = True
  Bloque3 = True
  Bloque4 = True          #variables que utilizemos mas adelante en el programa para la validacion 
  Bloque5 = True
  Bloque6 = True
  Bloque7 = True
  Bloque8 = True
  print("El juego ha comenzado , a continuacion incidique la fila y la columna donde desee atacar ")
  mesa1 = []
  Numeros_Usados = [[],[],[],[],[],[],[],[],[],[]]
  Numero = 1
                                   #Se crea las posicion donde se pondran los barcos
  DatosBuqueMenor = []
  DatosBuqueMenor.append((random.randrange(0,9),random.randrange(0,9),2))

  for x in range(0,10):              #Se crea el Tablero
    mesa1.append(["O"] * 10)
 
  # Poniendo Barco Buque Mayor  
  while Bloque1 == True:
    DatosBuqueMayor = []
    DatosBuqueMayor.append((random.randrange(0,9),random.randrange(0,9),3))
    DatosBuqueMayorx = DatosBuqueMayor[0][0]
    DatosBuqueMayorY = DatosBuqueMayor[0][1]
    dice1 = random.randrange(0, 2)  #para saber si el barco de pondra en posicion vertical o horizontal
    
    if dice1 == 0:    #Insertar el barco en posicion Horizontal
      dice2 = int(random.randrange(0,9))     #Se genera en que posicion se pondra 
      if dice2 < 7:
       Bloque1 = False
       Numeros_Usados[DatosBuqueMayorx].append(dice2)
       Numeros_Usados[DatosBuqueMayorx].append(dice2+1)  # Los numeros ya usados para no poner en la misma posicion otros barcos 
       Numeros_Usados[DatosBuqueMayorx].append(dice2+2)
       CoordenadasBuqueMayor = [[],[],[],[],[],[],[],[],[],[]]
       CoordenadasBuqueMayor[DatosBuqueMayorx].append(dice2)      #Coordenadas que usaremos mas adelante en el juego para saber si el usuario le pego a un barco
       CoordenadasBuqueMayor[DatosBuqueMayorx].append(dice2+1)
       CoordenadasBuqueMayor[DatosBuqueMayorx].append(dice2+2)
      else:  
        continue 
      
    else: #Insertar el barco en posicion Horizontal
      dice2 = int(random.randrange(0,9))  #Se genera en que posicion se pondra 
      if dice2 < 7:
        Bloque1 = False
        Numeros_Usados[DatosBuqueMayorY].append(dice2)
        Numeros_Usados[DatosBuqueMayorY-1].append(dice2) # Los numeros ya usados para no poner en la misma posicion otros barcos 
        Numeros_Usados[DatosBuqueMayorY-2].append(dice2)
        CoordenadasBuqueMayor = [[],[],[],[],[],[],[],[],[],[]]
        CoordenadasBuqueMayor[DatosBuqueMayorY].append(dice2)
        CoordenadasBuqueMayor[DatosBuqueMayorY-1].append(dice2+1)   #Coordenadas que usaremos mas adelante en el juego para saber si el usuario le pego a un barco
        CoordenadasBuqueMayor[DatosBuqueMayorY-2].append(dice2+2)
        
      else: 
        continue



  # Poniendo Barco Buque Menor
  while Bloque2 == True:
    DatosBuqueMenor = []
    DatosBuqueMenor.append((random.randrange(0,9),random.randrange(0,9),2))  #Generando datos del buque menor
    DatosBuqueMenorx = DatosBuqueMenor[0][0]
    DatosBuqueMenorY = DatosBuqueMenor[0][1]
    dice1 = random.randrange(0, 2)  #Generando para saber si se pone horizontal o vertical 
    
    if dice1 == 0: #Insertar el barco en posicion Horizontal
      dice2 = int(random.randrange(0,9)) #Se genera en que posicion se colocara 
      if dice2 < 8: 
        if dice2 in Numeros_Usados[DatosBuqueMayorx]: #se verifica que el numero no ha sido usado ya 
          continue
        else:
          dice2 = dice2 + 1
          if dice2 in Numeros_Usados[DatosBuqueMayorx]: #se verifica si el numero no ha sido usado ya
            continue
          else:
            Bloque2 = False
            Numeros_Usados[DatosBuqueMenorx].append(dice2) #Numeros para no repetir la posiciones de los barco 
            Numeros_Usados[DatosBuqueMenorx].append(dice2-1)
            CoordenadasBuqueMenor = [[],[],[],[],[],[],[],[],[],[]]
            CoordenadasBuqueMenor[DatosBuqueMenorx].append(dice2)   #Coordenadas para mas adelante en el juego
            CoordenadasBuqueMenor[DatosBuqueMenorx].append(dice2+1)
            
      else:  
        continue
    else: 
      dice2 = int(random.randrange(0,9)) #se genera en que posicion se usara 
      if dice2 < 8:
        if dice2 in Numeros_Usados[DatosBuqueMayorY]: #Se verifica que el numero no ha sido usado ya 
          continue
        else:
          dice2 = dice2 + 1
          if dice2 in Numeros_Usados[DatosBuqueMayorY]:
            continue
          else:  
            Bloque2 = False
            Numeros_Usados[DatosBuqueMenorY].append(dice2)  #Se agrega el numero para no repetir la posicion en el futuro
            Numeros_Usados[DatosBuqueMenorY].append(dice2-1)
            CoordenadasBuqueMenor = [[],[],[],[],[],[],[],[],[],[]]
            CoordenadasBuqueMenor[DatosBuqueMenorY].append(dice2)  #coordenadas para mas adelante en el juego 
            CoordenadasBuqueMenor[DatosBuqueMenorY-1].append(dice2+1)
      else: 
        continue
     
   # Poniendo Submarino 1
   
  while Bloque3 == True:
    DatosSubmarino1 = []
    DatosSubmarino1.append((random.randrange(0,9),random.randrange(0,9),2)) #Se generan los datos del submrino 1
    DatosSubmarino1X = DatosSubmarino1[0][0]
    DatosSubmarino1Y = DatosSubmarino1[0][1]
    dice1 = random.randrange(0, 2)
    
    if dice1 == 0: #Insertar el barco en posicion Horizontal
      dice2 = int(random.randrange(0,9)) #Se genera la posicion en que posicion se pondra 
      if dice2 < 9:
        if dice2 in Numeros_Usados[DatosSubmarino1X]: #se revisa si la posicion ya no ha sido usada 
          continue
        else:
          Bloque3 = False
          Numeros_Usados[DatosSubmarino1X].append(dice2) #Se agrega la posicion para que no se repita 
          CoordenadasSubmarino1 = [[],[],[],[],[],[],[],[],[],[]]     
          CoordenadasSubmarino1[DatosSubmarino1X].append(dice2)  #Coordenadas para mas adelante 
      else:  
        continue
    else: #insertar el barco en posicion vertical 
      dice2 = int(random.randrange(0,9)) #Se genera la posicion en que se pondra 
      if dice2 < 8:
        if dice2 in Numeros_Usados[DatosSubmarino1Y]: #Se revisa si la posicion no ha sido usada ya 
          continue
        else:
            Bloque3 = False
            Numeros_Usados[DatosSubmarino1Y].append(dice2) #se agrega la posicion para que no se repita 
            CoordenadasSubmarino1 = [[],[],[],[],[],[],[],[],[],[]]     #coordenadas para el futuro 
            CoordenadasSubmarino1[DatosSubmarino1Y].append(dice2)      
      else: 
        continue
   # Poniendo Submarino 2
  while Bloque4 == True:
    DatosSubmarino2 = []
    DatosSubmarino2.append((random.randrange(0,9),random.randrange(0,9),2)) #Se generan los datos 
    DatosSubmarino2X = DatosSubmarino2[0][0]
    DatosSubmarino2Y = DatosSubmarino2[0][1]
    dice1 = random.randrange(0, 2)
    
    if dice1 == 0: #Insertar el barco en posicion Horizontal
      dice2 = int(random.randrange(0,9)) #Se genera la posicion en donde se pondre 
      if dice2 < 9:
        if dice2 in Numeros_Usados[DatosSubmarino2X]: #Se revisa si la posicion no ha sido usada ya 
          continue
        else:
          Bloque4 = False
          Numeros_Usados[DatosSubmarino2X].append(dice2) #Se agrega la posicion para que no se repita denuevo 
          CoordenadasSubmarino2 = [[],[],[],[],[],[],[],[],[],[]]     
          CoordenadasSubmarino2[DatosSubmarino2X].append(dice2)  #Coordenadas para mas adelante 
      else:  
        continue
    else: 
      dice2 = int(random.randrange(0,9))
      if dice2 < 8:
        if dice2 in Numeros_Usados[DatosSubmarino2Y]:
          continue
        else:
            Bloque4 = False
            Numeros_Usados[DatosSubmarino2Y].append(dice2)
            CoordenadasSubmarino2 = [[],[],[],[],[],[],[],[],[],[]]     
            CoordenadasSubmarino2[DatosSubmarino2Y].append(dice2)     
      else: 
        continue  

   # Poniendo Submarino 3
  while Bloque5 == True:
    DatosSubmarino3 = []
    DatosSubmarino3.append((random.randrange(0,9),random.randrange(0,9),2))
    DatosSubmarino3X = DatosSubmarino3[0][0]
    DatosSubmarino3Y = DatosSubmarino3[0][1]
    dice1 = random.randrange(0, 2)
    
    if dice1 == 0: #Insertar el barco en posicion Horizontal
      dice2 = int(random.randrange(0,9))
      if dice2 < 9:
        if dice2 in Numeros_Usados[DatosSubmarino3X]:
          continue
        else:
          Bloque5 = False
          Numeros_Usados[DatosSubmarino3X].append(dice2)
          CoordenadasSubmarino3 = [[],[],[],[],[],[],[],[],[],[]]     
          CoordenadasSubmarino3[DatosSubmarino3X].append(dice2)
      else:  
        continue
    else: 
      dice2 = int(random.randrange(0,9))
      if dice2 < 8:
        if dice2 in Numeros_Usados[DatosSubmarino3Y]:
          continue
        else:
            Bloque5= False
            Numeros_Usados[DatosSubmarino3Y].append(dice2)
            CoordenadasSubmarino3 = [[],[],[],[],[],[],[],[],[],[]]     
            CoordenadasSubmarino3[DatosSubmarino3Y].append(dice2)       
      else: 
        continue

  # Poniendo Submarino 4
  while Bloque6 == True:
    DatosSubmarino4 = []
    DatosSubmarino4.append((random.randrange(0,9),random.randrange(0,9),2))
    DatosSubmarino4X = DatosSubmarino4[0][0]
    DatosSubmarino4Y = DatosSubmarino4[0][1]
    dice1 = random.randrange(0, 2)
    
    if dice1 == 0: #Insertar el barco en posicion Horizontal
      dice2 = int(random.randrange(0,9))
      if dice2 < 9:
        if dice2 in Numeros_Usados[DatosSubmarino4X]:
          continue
        else:
          Bloque6 = False
          Numeros_Usados[DatosSubmarino4X].append(dice2)  
          CoordenadasSubmarino4 = [[],[],[],[],[],[],[],[],[],[]]     
          CoordenadasSubmarino4[DatosSubmarino4X].append(dice2) 
      else:  
        continue
    else: 
      dice2 = int(random.randrange(0,9))
      if dice2 < 8:
        if dice2 in Numeros_Usados[DatosSubmarino4Y]:
          continue
        else:
            Bloque6= False
            Numeros_Usados[DatosSubmarino4Y].append(dice2) 
            CoordenadasSubmarino4 = [[],[],[],[],[],[],[],[],[],[]]     
            CoordenadasSubmarino4[DatosSubmarino4Y].append(dice2)     
      else: 
        continue

  for i in mesa1:
      print("Columna:",Numero,i)
      Numero = Numero + 1

   #-------------------------------------------------------Poniendo El Juego En marcha, Ya que estan colocados todas las piezas ------------------------------------------------------------

  Bloque7 = True
  Numeros_Repetidos = [[],[],[],[],[],[],[],[],[],[]]
  Disparo= 0
  Aciertos = 0                                         #Variables para poner las estadisticas 
  Numero = 1
  Puntos_Total = 0
  Disparo_Repetidos = 0


  while Bloque7 == True:          #Con este while el jugador va disparando y eligir donde disparar 
    
    bloque8 = True
 
    while bloque8 == True:                   #While para que el usuario no pueda rompar el programa 
          Pregunta1 = input("ingrese la columna donde desea disparar")
          Pregunta2 = input("Ingrese La fila donde desea disparar")
          try:
              Pregunta1=int(Pregunta1)
              try:
                  Pregunta2=int(Pregunta2)
                  bloque8 = False
                  break
              except ValueError:
                  print ("ERROR: ingrese numero entero del rango del 1 al 10")
          except ValueError:
              print ("ERROR: ingrese un numero entero del rango del 1 al 10")
                        
    if Pregunta1 > 10:            #Error si la fila y la columna que desea colocar el usuario  es mayor de 10
      print("ERROR: Ingrese un numero entero en el rango del 1 al 10")
    else:
      if Pregunta2 > 10:
        print("ERROR: ingrese un numero entero en el rango del 1 al 0")
      else:
       Pregunta1 = Pregunta1 - 1
       Pregunta2 = Pregunta2 - 1
       if Pregunta2 in Numeros_Repetidos[Pregunta1]:  #Si el usuario dispara el mismo lugar manda a repetir y se suma la puntacion de numeros repetidos 
         print("Ya disparaste en ese lugar, Porfavor dispare en otro lugar")
         Disparo_Repetidos = Disparo_Repetidos + 1
       else: 
        if Pregunta2 in Numeros_Usados[Pregunta1]:
          mesa1[Pregunta1][Pregunta2] = "F"
          print("Felicidades le diste un Barco de tipo!")
          Numeros_Repetidos[Pregunta1].append(Pregunta2)
          Aciertos = Aciertos + 1
          Disparo = Disparo + 1
          Puntos_Total = Puntos_Total + 10
          if Pregunta2 in CoordenadasBuqueMayor[Pregunta1]:        #se llama la clase y llama la habilidad del barco para darse una idea que barco le pego el usuario
            print("El barco que le pegaste tiene la habilidad de::")
            BuqueMayor.Habilidad(1)
          elif Pregunta2 in CoordenadasBuqueMenor[Pregunta1]:
            print("El Barco que le pegaste tiene la habilidad de:")  
            BuqueMenor.Habilidad(1)
          elif Pregunta2 in CoordenadasSubmarino1[Pregunta1]:
            print("El Barco que le pegaste tiene la habilidad de:")  
            Submarino.Habilidad(1) 
          elif Pregunta2 in CoordenadasSubmarino2[Pregunta1]:
            print("El Barco que le pegaste tiene la habilidad de:")  
            Submarino2.Habilidad(1)   
          elif Pregunta2 in CoordenadasSubmarino3[Pregunta1]:
            print("El Barco que le pegaste tiene la habilidad de:")  
            Submarino3.Habilidad(1)   
          elif Pregunta2 in CoordenadasSubmarino4[Pregunta1]:
            print("El Barco que le pegaste tiene la habilidad de:")  
            Submarino4.Habilidad(1)   
        else: 
            mesa1[Pregunta1][Pregunta2] = "X"                 #Si fallas el tiro 
            Numeros_Repetidos[Pregunta1].append(Pregunta2) 
            Disparo = Disparo + 1
            Puntos_Total = Puntos_Total - 2
            print("Fallaste El tiro") 
    for i in mesa1:
      print("Columna:",Numero,i)
      Numero = Numero + 1                     #Se enseña el mapa denuevo 
    Numero = 1  
    print("Disparos Total Hechos:",Disparo)   #Saber cuantos disparos ya has hecho 

    if Aciertos == 9:              #Terminado el juego dependiendo del desempeño te enseña los siguiente mensajes 
      print("Felicidades Terminaste el juego aqui le dejo un mensaje especial por su desempeño:")
      Bloque7 = False
      if Disparo == 9:
        print("¿Eres un robot? lo que acabas de hacer un poco probable")
        Bloque7 = False
      elif Disparo < 45:
        print("Excelente Estrategia") 
        Bloque7 = False
      elif Disparo > 45 and Disparo < 70:
        print("Buena estrategia, pero hay que mejorar") 
        Bloque7 = False
      elif Disparo > 75:
        print("Considerese Perdedor, tiene que mejorar notablemente")  
        Bloque7 = False

        #Se enseñan los datos del usuario por eso se guardo al principio del programa la variable usuario 

  print("Nombre de usuario Del jugador:",usuario[0])
  print("Cantidad de disparos realizados:",Disparo)
  print("Puntuaje total:",Puntos_Total)
  print("Cantidad de disparos repetidos:",Disparo_Repetidos)

  print("Tus datos ya fueron subidas a la Estadisticas, revisa si estas en el top 10 volviendo al menu")
  
#Se sube al archivo de top usarios los datos de esta partida 

  username = usuario[0]
  nombre = usuario[1]
  edad = usuario [2]
  genero = usuario [3]
  puntos = Puntos_Total
  with open("TopJugadores.txt", "a+") as bd: #Se abre la base de datos
        bd.write("{},{},{}\n".format(username,puntos,Disparo))

#Se suben a las estadisticas los datos obtenidos en esta partida 

  with open("Estadisticas.txt", "a+") as bd: #Se abre la base de datos
        bd.write("{},{},{},{}\n".format(edad,genero,puntos,Disparo))
        
  






  
  
  
   
  #Se colocaron todas las piezas ya 
