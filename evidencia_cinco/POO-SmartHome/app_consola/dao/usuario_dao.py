from dao.interfaces.interface_usuario_dao import IDataAccessUsuarioDAO
from domain.entities.usuario import Usuario
from conn.db_conn import DBConn
from typing import List


class UsuarioDAO(IDataAccessUsuarioDAO):

    def get(self, correo: str) -> Usuario:
        with self.__connect_to_mysql() as conexion:
        
            if not conexion:
                return None
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM usuario WHERE correo = %s", (correo,))
                fila = cursor.fetchone()
                                
                if fila:
                    return Usuario(fila[0], fila[1], fila[2], fila[3])
                return None
            except Exception as e:
                print(f"[DAO] Error al obtener usuario: {e}")
                return None
     
    def get_all(self) -> List[Usuario]:
        with self.__connect_to_mysql() as conexion:
            if not conexion:
                return None
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM usuario")
                filas = cursor.fetchall()
                usuarios = [Usuario(correo=f[0], nombres=f[1], apellidos=f[2], contrasena=f[3]) for f in filas]
                return usuarios
            except Exception as e:
                print(f"[DAO] Error al obtener usuarios: {e}")
                return None

    def create(self, usuario: Usuario) -> bool:
        with self.__connect_to_mysql() as conexion:
            if not conexion:
                return False
            try:
                cursor = conexion.cursor()
                sql = "INSERT INTO usuario (correo, nombres, apellidos, contrasena) VALUES (%s, %s, %s, %s)"
                valores = (usuario.correo, usuario.nombres, usuario.apellidos, usuario.contrasena)
                cursor.execute(sql, valores)
                conexion.commit()
                return True
            except Exception as e:
                print(f"[DAO] Error al crear usuario: {e}")
                conexion.rollback()
                return False
        
    def update(self, usuario: Usuario) -> bool:
        with self.__connect_to_mysql() as conexion:
            if not conexion:
                return False
            try:
                cursor = conexion.cursor()
                
                # Pedimos nuevos valores
                nombres = input("Nuevo nombre/s (Enter para mantener): ").strip()
                apellidos = input("Nuevo apellido/s (Enter para mantener): ").strip()
                contrasena = input("Nueva contraseña (Enter para mantener): ").strip()

                # Si el usuario no escribió nada, se mantiene el valor anterior
                if nombres:
                    usuario.nombres = nombres
                if apellidos:
                    usuario.apellidos = apellidos
                if contrasena:
                    usuario.contrasena = contrasena

                sql = """
                    UPDATE usuario
                    SET nombres = %s, apellidos = %s, contrasena = %s
                    WHERE correo = %s
                """
                valores = (usuario.nombres, usuario.apellidos, usuario.contrasena, usuario.correo)
                cursor.execute(sql, valores)
                conexion.commit()
                return True

            except Exception as e:
                print(f"[DAO] Error al actualizar usuario: {e}")
                conexion.rollback()
                return False
 
    def delete(self, correo: str) -> bool:
        with self.__connect_to_mysql() as conexion:
            if not conexion:
                return False
            try:
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM usuario WHERE correo = %s", (correo,))
                conexion.commit()
                return True
            except Exception as e:
                print(f"[DAO] Error al eliminar usuario: {e}")
                conexion.rollback()
                return False
          
    def __connect_to_mysql(self):
# Conectar a una base de datos MySQL Server
        db = DBConn()
        connection = db.connect()  
        return connection