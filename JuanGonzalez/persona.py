class persona:
    def __init__(self,nombre,apellidos,cedula,correo,telefono):
            self.nombre=nombre
            self.apellidos=apellidos
            self.cedula=cedula
            self.correo=correo
            self.telefono=telefono

          
    def obtenernombre(self):
        return f'mi nombre es {self.nombre}'
    
    def obtenerapellido(self):
         return f'mi apellido es {self.apellidos}'
    
    def obtenercedula(self):
         return f' mi cedula es{self.cedula}'
    
    def obtenercorreo(self):
         return f'mi correo es{self.correo}'
    
    def obtenertelefono(self):
         return f'mi telefono es {self.telefono}'
   
print("nombre","Juan","apellidos","Gonzalez","cedula","1050948304","correo","juangonzalesr9@gmail.com","telefono","3145330039")
    
    