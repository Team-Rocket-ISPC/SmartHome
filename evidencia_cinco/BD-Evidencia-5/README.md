SmartHomeDB - Scripts SQL

Este proyecto contiene los scripts SQL necesarios para crear la base de datos SmartHomeDB, pensada como ejemplo de un sistema de casa inteligente (SmartHome).

---

Archivos incluidos

scriptDDL.sql: contiene todas las sentencias para crear la base de datos y sus tablas principales (usuarios, viviendas, dispositivos, etc.), con sus claves primarias y foráneas.

scriptDML.sql: inserta más de 30 registros de ejemplo y ejecuta consultas básicas a cada tabla.

onecompiler.txt: Contiene el script adaptado para correr dentro de One Compiler.

README.md: este archivo de documentación, donde se explican los pasos para usar los scripts.


---

¿Cómo ejecutar los scripts?, dentro de un compilador online como One compiler (https://onecompiler.com/mysql), copiar el código disponible en onecompiler.txt y pegar en la página indicada.


1. Abrir One Compiler

EntIngresar a One Compiler.

Seleccioná MySQL como lenguaje de base de datos.

2. Abrir un archivo .sql (En caso de utilizar un motor de base de datos) o pegar el código disponible dentro de onecompiler.txt.

copiá todo el contenido del archivo (Ctrl+C y luego Ctrl+V).

3. Pegar el script en One Compiler

En One Compiler, pegá todo el contenido copiado en el área de código.

4. Ejecutar el script

Hacé clic en el botón Run o Execute.

One Compiler ejecutará todas las sentencias:

scriptDDL.sql: crea la base de datos y las tablas.

scriptDML.sql: inserta los registros de ejemplo y ejecuta consultas básicas.

5. Verificar los resultados

Los resultados de las consultas se mostrarán en la sección Output.


---

Nota: Los scripts originales fueron creados para SQL Server, pero se adaptaron para MySQL, que es compatible con One Compiler. Por eso pueden existir pequeñas diferencias en la sintaxis.


 En caso de ejecutarse en un motor de base de datos, es importante ejecutar primero el DDL y después el DML, ya que si las tablas no existen, los INSERT fallarán.



