class VehiculoMarino():           #Se crea la clase principal

    def __init__(self,posicionX, posicionY):           #se le dan las caracteristicas de la clase
         self.posicionX = posicionX
         self.posicionY = posicionY

    def Habilidad(self):
        print("Este es un vehiculo que puede navegar en el mar")          #Se crea la habilidad del barco


class BuqueMayor(VehiculoMarino):                    #Se hace la herencia de la clase principal

    def __init__(self,posicionX, posicionY,largo):
        VehiculoMarino.__init__(self,posicionX, posicionY) #se le agregan caracteristicas adicionales ademas de la herencia de la principal
        self.largo = 3


    def Habilidad(self):
        print("Tiene la capacidad de “aterrizar helicópteros en él para el transporte de tropas") 
        #Se modifica la habilidad ya que es un esta herencia tendra una habiliad diferente
        

class BuqueMenor(VehiculoMarino): #Se hace la herencia de la clase principal

     def __init__(self,posicionX, posicionY,largo):
        VehiculoMarino.__init__(self,posicionX, posicionY) #se le agregan caracteristicas adicionales ademas de la herencia de la principal
        self.largo = 2

     def Habilidad(self):
        print("Tiene la capacidad de comunicarse con tierray los otros miembros de la flota")  
        #Se modifica la habilidad ya que es un esta herencia tendra una habiliad diferente     

    
    
class Submarino(VehiculoMarino): #Se hace la herencia de la clase principal
     def __init__(self,posicionX, posicionY,largo):
        VehiculoMarino.__init__(self,posicionX, posicionY) #se le agregan caracteristicas adicionales ademas de la herencia de la principal
        self.largo = 1

     def Habilidad(self):
        print("Tiene la capacidad de podersumergirse y emerger del agua*.") 
        #Se modifica la habilidad ya que es un esta herencia tendra una habiliad diferente     




 
class Submarino2(VehiculoMarino): #Se hace la herencia de la clase principal
     def __init__(self,posicionX, posicionY,largo):
        VehiculoMarino.__init__(self,posicionX, posicionY) #se le agregan caracteristicas adicionales ademas de la herencia de la principal
        self.largo = 1

     def Habilidad(self):
        print("Tiene la capacidad de podersumergirse y emerger del agua*.")
        #Se modifica la habilidad ya que es un esta herencia tendra una habiliad diferente



 
class Submarino3(VehiculoMarino): #Se hace la herencia de la clase principal
     def __init__(self,posicionX, posicionY,largo):
        VehiculoMarino.__init__(self,posicionX, posicionY) #se le agregan caracteristicas adicionales ademas de la herencia de la principal
        self.largo = 1

     def Habilidad(self):
        print("Tiene la capacidad de podersumergirse y emerger del agua*.")   
        #Se modifica la habilidad ya que es un esta herencia tendra una habiliad diferente






class Submarino4(VehiculoMarino): #Se hace la herencia de la clase principal
     def __init__(self,posicionX, posicionY,largo):
        VehiculoMarino.__init__(self,posicionX, posicionY) #se le agregan caracteristicas adicionales ademas de la herencia de la principal
        self.largo = 1

     def Habilidad(self):
        print("Tiene la capacidad de podersumergirse y emerger del agua*.") 
        #Se modifica la habilidad ya que es un esta herencia tendra una habiliad diferente      
    
           
               
    
       
    
       

