

class UsuarioDao(object):
    
    def __init__(self, fachada):                
        self.db = fachada;        
    
    def validarUsuario(self,usuario):
        sql = "SELECT id, emailUsuario, nombreUsuario, apellidoUsuario, passwordUsuario, rolUsuario, telefonoUsuario, operadorUsuario FROM uv_music_usuario WHERE emailUsuario = '"+usuario.getEmail()+"' AND passwordUsuario = '"+usuario.getPassword()+"'"        
        self.db.conectar()
        resultado = self.db.consultar(sql)
        if resultado != None:
            usuario.setId(resultado[0])
            usuario.setNombre(resultado[1])
            usuario.setApellido(resultado[2])
            usuario.setPassword(resultado[3])
            usuario.setRol(resultado[4])
            usuario.setTelefono(resultado[5])
            usuario.setOperador(resultado[6])
            self.db.cerrarConexion()
            return usuario
        else:
            self.db.cerrarConexion()
            return None
       
    def buscarUsuario(self,email):
        sql = "SELECT id, emailUsuario, nombreUsuario, apellidoUsuario, passwordUsuario, rolUsuario, telefonoUsuario, operadorUsuario FROM uv_music_usuario WHERE emailUsuario = '"+email+"'"         
        self.db.conectar()
        resultado = self.db.consultar(sql)
        self.db.cerrarConexion()
        if resultado != None:            
            return "existe"
        else:            
            return ""
    
    def registrarUsuario(self,usuario):
        sql = "INSERT into uv_music_usuario(nombreUsuario, \
               apellidoUsuario,emailUsuario,passwordUsuario,telefonoUsuario,operadorUsuario,rolUsuario) \
               VALUES ('%s', '%s', '%s', '%s', '%s', '%s','%d')" % \
              (usuario.getNombre(),usuario.getApellido(),usuario.getEmail(),usuario.getPassword(),usuario.getTelefono(),usuario.getOperador(),False)         
        self.db.conectar()
        resultado = self.db.insertar(sql)
        self.db.cerrarConexion()
        if resultado != None:            
            return resultado
        else:            
            return "registrado"
