# Diagrama de clases red social

+---------------------+          +------------------------+         +-------------------+
|     Red Social      |          |        Usuario         |         |      Publicación  |
+---------------------+          +------------------------+         +-------------------+
| - nombre: string    |          | - nombre_usuario: string |         | - contenido: string|
| - descripcion: string|         | - correo: string         |         | - fecha: date      |
+---------------------+          | - contraseña: string    |         | - meGusta: int     |
| + agregarUsuario() |           | - fecha_nacimiento: date |         +-------------------+
| + eliminarUsuario()|           | - amigos: List<Usuario>  |
+---------------------+          +------------------------+
         |                                  |       /\
         |                                  |        |
         |                      +-----------+--------+-------------+
         |                      |                                     |
         |                +------------+                      +---------------+
         |                |   Foto     |                      |  Comentario   |
         |                +------------+                      +---------------+
         |                | - imagen: string                 | - contenido: string|
         |                | - fecha: date                    | - fecha: date      |
         |                | - usuario: Usuario               | - usuario: Usuario |
         |                +----------------------------------+ - publicacion: Publicacion|
         |                                                      +---------------+
         |
         |
         |
         |
+---------------------------+
|          Mensaje          |
+---------------------------+
| - contenido: string       |
| - fecha: date              |
| - remitente: Usuario      |
| - destinatario: Usuario   |
+---------------------------+
