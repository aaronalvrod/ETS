+---------------------+          +----------------------+           +---------------------+
|    RedSocial        |          |      Usuario         |           |       Administrador |
+---------------------+          +----------------------+           +---------------------+
|                     |          | - nombre: string    |           | - nombre: string    |
|                     |          | - correo: string    |           | - correo: string    |
|                     |          | - fechaNacimiento:  |           +---------------------+
|                     |          |   Date             |           
| + publicarMensaje() |<>--------| + enviarMensaje()   |                      
| + conectarAmigos()  |          | + recibirMensaje()  |  
| + eliminarPublicacion()|       | + aceptarSolicitud()|   
+---------------------+          +----------------------+
        /\                                 |  
         |                                 |   
         |            +-------------------+-------------------+
         |            |             Amistad                  |
         |            +------------------------------------+
         |            | - usuario1: Usuario                |
         |            | - usuario2: Usuario                |
         |            +------------------------------------+
         |                        |
+-----------------------------+   |
|         Mensaje             |   |
+-----------------------------+   |
| - contenido: string         |   |
| - emisor: Usuario           |   |
| - receptor: Usuario         |   |
| - fecha: Date               |   |
+-----------------------------+   |
