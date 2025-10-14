from dao.interfaces.interface_usuario_dao import IDataAccessUsuarioDAO
from domain.entities.usuario import Usuario
from conn.db_conn import DBConn
from typing import List


class UsuarioDAO(IDataAccessUsuarioDAO):
    """Implementa las operaciones CRUD para la entidad Usuario."""
    def get(self, correo: str, contrasena: str) -> Usuario:
        """Obtiene un usuario por su correo y contraseña."""
        with self.__connect_to_mysql() as conexion:
        
            if not conexion:
                return None
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM usuario WHERE correo = %s AND contrasena = %s", (correo, contrasena))
                fila = cursor.fetchone()        
                if fila:
                    return Usuario(fila[0], fila[1], fila[2], fila[3])
                return None
            except Exception as e:
                print(f"[DAO] Error al obtener usuario: {e}")
                return None
     
    def get_all(self) -> List[Usuario]:
        """Obtiene todos los usuarios de la base de datos."""
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
        """Crea un nuevo usuario en la base de datos."""
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
        """Actualiza los datos de un usuario existente.
        Permite actualizar nombres, apellidos y contraseña.
        Si el usuario no ingresa un nuevo valor, se mantiene el anterior.
        """
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
        """Elimina un usuario dado su correo."""
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
            
    def cambio_rol(self, correo: str, nuevo_rol: str) -> bool:
        """Cambia el rol de un usuario dado su correo."""
        with self.__connect_to_mysql() as conexion:
            if not conexion:
                return False
            try:
                cursor = conexion.cursor()
                sql = "UPDATE usuario_vivienda SET rol = %s WHERE correo = %s"
                valores = (nuevo_rol, correo)
                res = cursor.execute(sql, valores)
                if res == 0:
                    print("[DAO] No se encontró el usuario para cambiar el rol.")
                    return False
                conexion.commit()
                return True
            except Exception as e:
                print(f"[DAO] Error al cambiar rol de usuario: {e}")
                conexion.rollback()
                return False
          
    def __connect_to_mysql(self):
        """Establece una conexión con la base de datos MySQL."""
        db = DBConn()
        connection = db.connect()  
        return connection