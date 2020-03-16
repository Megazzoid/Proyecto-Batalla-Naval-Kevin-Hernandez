#ingresar usuarios 


class Usuario:
    def __init__(self, username, nombre, edad, genero, puntos = 0,disparos_realizados = 0):
        self.username = username
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.puntos = puntos
        self.disparos_realizados = disparos_realizados

    def __str__(self):
        return 'Usuario: {}\nNombre completo: {}\nEdad: {}\nGenero: {}\n'.format(self.username, self.nombre, self.edad, self.genero)