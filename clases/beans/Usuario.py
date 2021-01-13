    
class Usuario(object):
    
    def __init__(self, emailUsuario,passwordUsuario ):
        self.nombre = ""
        self.apellido = ""
        self.rol = ""
        self.email = ""
        self.password = ""
        self.telefono = ""
        self.operador = ""                        
        self.email = emailUsuario
        self.password = passwordUsuario
        self.id = ""


#    Setters

    def setEmail(self,x):
        self.email = x

    def setNombre(self,x):
        self.nombre = x

    def setApellido(self,x): 
        self.apellido = x
    
    def setPassword(self,x):
        self.password = x    

    def setRol(self,x): 
        self.rol = x
    
    def setTelefono(self,x):
        self.telefono = x
    
    def setOperador(self,x):
        self.operador = x
       
    def setId(self,x):
        self.id = x
    
#    Getters

    def getEmail(self):
        return self.email    

    def getNombre(self):
        return self.nombre    

    def getApellido(self):
        return self.apellido
    
    def getPassword(self):
        return self.password
    
    def getRol(self):
        return self.rol

    def getTelefono(self):
        return self.telefono

    def getOperador(self):
        return self.operador
    
    def getId(self):
        return self.id  