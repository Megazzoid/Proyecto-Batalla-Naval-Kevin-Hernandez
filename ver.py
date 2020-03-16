#Es la misma funcion de ver que esta en el main.py solo que la uso aqui para no tener errores usandola en el tablero

from Usuario import Usuario
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

       