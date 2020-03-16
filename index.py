#Parte 1 Modulo de creacion del usuario 

from Usuario import Usuario   #Se importa la clase Usuario

bloqueador_2 = True
continuar = 0

print("Bienvenido a batalla naval extreme porfavor eliga una de las siguientes opciones:")  #El menu principal del juego y seleccionar la opcion para continuar

def buscar_usuario(username):  
    with open("DatosDeLosUsuarios.txt", "r") as bd: 
        datos = bd.readlines()
    for dato in datos:   
        usuario = dato[:-1].split(',')
        if usuario == username:    
            return Usuario(usuario[0], usuario[1], usuario[2], usuario[3])

#------------------------------------------------------------------------------------Otra Funcion -------------------------------------------------------------

def Revisar_username_existe(username):
    try:
        all_users = open('DatosDeLosUsuarios.txt', 'r').readlines()
        for user in all_users:
            usuario = user[:-1].split(',')
            if usuario[0] == username:
                return True
        return False
    except FileNotFoundError:
        print('No se ha registrado ningun usuario todavia')
        return False

#------------------------------------------------------------------------------------Otra Funcion -------------------------------------------------------------

def registrar():  #Registrarmos aqui el Usuario
    Bloqueador1 = True 
    print("Ingrese los siguientes datos para completar el registro")
    while Bloqueador1 == True:

        username = input("Ingrese su nombre de usuario") # Registro de nombre de usuario 
        

        username = username.lower() #Convertimos todo en mininuscula 

        username = username.replace(' ', '') # Se quitan los espacios del Nombre del usario

        if len(username) > 30:                                            #Se verifica Si el Usuario tiene menos de 30 caracteres 
            print("Porfavor ingrese un Usuario menor de 30 Caracteres") 
        else:
            if Revisar_username_existe(username) == True: # Se revisa si el Usuario si ya existe , si existe se repite el proceso de while hasta terminar
                print('El usuario ya existe, Porfavor Ingrese un usuario que no exista')
            else:
                Bloqueador1 = False   #Se sale del while 
        
    nombre = input("Ingrese Su nombre Completo")  #Se ingresa el nombre completo del usuario

    
    bloqueo10 = True   #Creamos aqui un while para poner que el usuario ingrese una edad que sea solo entera, si envia un numero que no es entero o otro simbolo dara error
    while bloqueo10 == True:
        bloqueo9 = True
        while bloqueo9 == True:
            edad= input("Porfavor diga su edad (no menor de 5 años o mayor de 95")
            try:
                edad=int(edad)                                   #Se verifica si es entero
                bloqueo9= False
                break
            except ValueError:
                 print ("Porfavor introdusca una edad valida")
        if edad < 5:                                             #Se verifica que es mayor de 5 años
            print("Su edad no puede ser menor de 5 años")
        else:
            if edad > 95:                                        # Se verifica que es menor de 95 años
                print("su Edad no puede ser mayor de 95 años")
            else:
                bloqueo10 = False    

    #Ahora atraves de un while y atraves de un input vamos ingresar el genero

    Bloqueo_genero = True
    while Bloqueo_genero == True:
       Seleccion_Sexo = input("Ingrese m si es Masculino y f si es Femenino") 
       if Seleccion_Sexo == "m":
           genero = "Masculino" # Se sale del while y ponemos que el genero es masculino
           Bloqueo_genero = False 
       elif Seleccion_Sexo == "f":
           genero = "Femenino" # Se sale del while y ponemos que el genero es Femenino
           Bloqueo_genero = False
       else:
           print("Porfavor Ingrese una opcion Valida")   #El usuario no escribio m o f se repite el proceso while hasta lograrlo      

    #Vamos a ignresar todos los datos obtenidos en el archivo txt
    usuario = Usuario(username, nombre, edad, genero)
    with open("DatosDeLosUsuarios.txt", "a+") as bd: #Se abre la base de datos
        bd.write("{},{},{},{}\n".format(username, nombre, edad, genero))
    print('\tUsuario: ', usuario.username, 'El usuario fue registrado exitosamente')
    return Usuario             #Se enseña al usuario todos los datos que el escribio 




    #Variable y luego con un if para saber si quiere salir el usuario o volver al menu

    Opcion_Salida = input('''                      
    Desea salir o volver al menu?
    Presione 1 para Salir
    Presione otra cualquier tecla para volver al menu
    ''') 

    if Opcion_Salida == 1:
        bloqueador_2 = False
    else:
        bloqueador_2 = True
 #------------------------------------------------------------------------------------Otra Funcion -------------------------------------------------------------          

def ver(edit = False): #Funcion para ver los Usuarios Actualmente Registrados
    
    print("Esto son los usarios registrados actualmente")
    usuarios = []
    with open("DatosDeLosUsuarios.txt", "r") as bd: #Se abre  los datos de los usuarios en el archivos txt
        datos = bd.readlines()
    for dato in datos:
        usuario = dato[:-1].split(',') 
        usuarios.append(Usuario(usuario[0], usuario[1], usuario[2], usuario[3]))
    if not edit:
        usuarios.sort(key= lambda user: user.username)
    for i, user in enumerate(usuarios):
        print('-'*5, i+1, '-'*5)
        print(user)
        

    #Se enseñan todos los usuarios registrados



#------------------------------------------------------------------------------------Otra Funcion -------------------------------------------------------------        
 #funcion para enseñar el top 10 de las puntaciones de los jugadores que ya han jugado

def top():
    usuarios = []
    with open("Topjugadores.txt", "r") as bd: #Se abre  los datos de los usuarios en el archivos txt
        datos = bd.readlines()
    Lista1 = []
    Lista2 = [] 
    Lista3 = []
    i = 0
    for dato in datos:
        usuario = dato[:-1].split(',') # [:-1] para quitar el salto de linea
        Lista1.append(usuario[0])
        Lista2.append(usuario[1])
        Lista3.append(usuario[2])
        i = i + 1
        i = int(i)

    Lista4 = sorted(Lista2,reverse=True)              #No logre poner bien aqui el orden 
    for y in range(len(Lista1)):
        print(Lista1[y],"/ Puntos:",Lista4[y],"/ Disparos:",Lista3[0])    

    


    
#------------------------------------------------------------------------------------Otra Funcion -------------------------------------------------------------         
         
          
def actualizar(seleccion):
    
    # Funcion que permite modificar datos de los usuarios registrados 
    

    print('''
    ¿Qué atributo desea modificar? Presione:
     1-Username  
     2-Nombre
     3-Edad
     4-Género
    ''')
    selec  = int(input("Seleccione una opción" ))   #Eligimos el dato que queremos modificar

    with open("DatosDeLosUsuarios.txt", 'r') as bd:
        datos = bd.readlines()
        usuario = datos[seleccion - 1][:-1].split(',')
    usuario[seleccion - 1] = input("Ingrese el nuevo valor:")
    nuevo_valor = ''
    for i in range(len(usuario)):
        if i != len(usuario) -1:
            nuevo_valor += usuario[i] + ','
        else:
            nuevo_valor += usuario[i] + '\n'
    datos[seleccion - 1] = nuevo_valor
    with open("DatosDeLosUsuarios.txt,","w") as bd:
        bd.writelines(datos)   
#--------------------------------------------------------------- Otra funcion ---------------------------------------------------------------------------------------

#Funcion para eliminar usuarios de la base de datos

def eliminar(seleccion):
    with open("DatosDeLosUsuarios.txt", "r") as bd:
        lineas = bd.readlines()
        borrar = lineas[seleccion-1]
    with open("DatosDeLosUsuarios.txt", "w") as bd:
        for line in lineas:
            if line != borrar:
                bd.write(line)
    print("El usuario Se ha eliminado con exito")  

#---------------------------------------------------------Otra funcion ----------------------------------------------------------------------------------------------

# Funcion principal que llamara las otras funciones por eso el nombre index 

def index():
    print("Top 10 Jugadores")   #Se enseña el top 10
    top()  

    print('''                                          
    ¿Qué operación desea realizar?
    1 - Registrar un usuario
    2 - Ver un usuario
    3 - Modificar un usuario
    4 - Eliminar un usario
    5 - Ver Estadisticas 
    6 - Comenzar juego nuevo 
    ''')

    seleccion = int(input('''     
    Seleccione una opción: (1/2/3/4/5/6) \n
    '''))
     
    #Dependiendo de la seleccion se eligira el siguiente instruccion del juego 

    if seleccion == 1:   #Si es 1 llamamos la funcion registrar
        usuario = registrar()
        print(usuario)
    elif seleccion == 2: #si es 2 llamaos la funcion ver para ver los usuarios 
        ver()
    elif seleccion == 3: #si es 3 llamamos la funcion actualizar para actualizar un dato del usuario 
        ver(edit = True)
        bloqueo = True
        while bloqueo == True: 
             #Seleccionamos el usuario que vamos a querer actualizar y lo hacemso atraves un while para que el usuario eliga la opcion correcta  
            bloqueo9 = True
            while bloqueo9 == True:
                seleccion = input("Seleccione el usuario que desea actualizar (Porfavor introdusca el numero entero correspondido al usuario=") 
                
                try:
                    seleccion=int(seleccion)
                    bloqueo9= False
                    break
                except ValueError:
                    print ("ERROR: ingrese numero entero correspondido al usuario que desea actualizar")
            if seleccion > 0:
                bloqueo = False
            else: 
                print("Error:Porfavor introdusca el usuario con el numero correspondido")    
        actualizar(seleccion)
    elif seleccion == 4: #si es 4 llamamos la funcion de eliminar un usuario 
        ver()
        bloqueo = True
        while bloqueo == True:
            #Seleccionamos el uusario que vamos a querer eliminar y lo hacemso atraves un while para que el usuario eliga la opcion correcta 
            bloqueo9 = True
            while bloqueo9 == True:
                seleccion = input("Seleccione el usuario que desea eliminar (Porfavor introdusca el numero entero correspondido al usuario=")
                try:
                    seleccion=int(seleccion)
                    bloqueo9= False
                    break
                except ValueError:
                    print ("ERROR: ingrese numero entero correspondido al usuario que desea eliminar")
            if seleccion > 0:
                bloqueo = False
            else: 
                print("Error: Porfavor introdusca el usuario con el numero correspondido")  
        eliminar(seleccion)

    elif seleccion == 5: #Funcion para ver las estadisticas
        from Estadistica import Estadisticas
        Estadisticas()
        
    elif seleccion == 6: #Funcion para comenzar el juego 
        from Juego import Juego
        Juego()
         
       
    else:
        print("No eligio una opcion Valida") #El usuario eligio una opcion equivocado se le pregunntara si quiere salir o volver al menu

     
while bloqueador_2 == True:  #este while es para saber si el usuario quiere seguir usando el programa atraves volviendo al menu o saliendo de una ves
    
    index()
    
    bloqueo9 = True
    while bloqueo9 == True:
        Fin= input("Porfavor introdusca 2 si desea salir y 1 para volver al menu") #se pide un numero del 1 al 2  y se verifica que sea entero
        try:
            Fin=int(Fin)
            bloqueo9 = False
            break
        except ValueError:
                print ("Escriba un numero Entero entre que sea 2 para salir y 1 para volver al menu")
    if Fin == 2: #si es 2 nos salimos
        print("Adios!")
        bloqueador_2 = False
        break
    if Fin == 1: #si es 1 volvemos al menu
        continue
    else: #si no es 2 o 1 salimos por default en el programa 
        print("Como no pusiste una opcion correcta apagaremos el programa por default Adios!") 
        bloqueador_2 = False                   





