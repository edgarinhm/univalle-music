'''
Created on Oct 22, 2012

@author: edgar
'''
import MySQLdb

class FachadaDB(object):
    def __init__(self):
        self.conn=""
        self.cursor=""
        
#   Parametros internos usados para la comunicacion con la base de datos MySQL        
    def conectar(self):
        try:
            self.conn = MySQLdb.connect (
                  host = '127.0.0.1',
                  user = 'root',
                  passwd = 'poweredge',
                  db = 'uv_music'
                 ) 
            self.cursor = self.conn.cursor()
        except:        
            return "error al concectar a la db"
        
    def consultar(self, sql):
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchone()
            # Commit your changes in the database
            self.conn.commit()
            return resultado
        except:
            # Rollback in case there is any error
            self.conn.rollback()
            return "error"
    
    def consultarTodos(self, sql):
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            return resultado
        except:
            # Rollback in case there is any error
            self.conn.rollback()
            return "error"
    
    def insertar(self,sql):
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Commit your changes in the database
            self.conn.commit()            
        except:
            # Rollback in case there is any error
            self.conn.rollback()
            return "error"        
        
    def insertarMuchos(self,sql, prepared_query):
        try:
            # Execute the SQL command
            self.cursor.executemany(sql,prepared_query)
            # Commit your changes in the database
            self.conn.commit()            
        except MySQLdb.Error, e:
             
            # Rollback in case there is any error
            self.conn.rollback()
            print "An error has been passed. %s" %e
                  
        
    def cerrarConexion(self):
        self.cursor.close()
        self.conn.close()
        
        