+---------------------+          +---------------------+           +---------------------+
|    ClubNautico      |          |      Barco          |           |       Socio         |
+---------------------+          +---------------------+           +---------------------+
|                     |          | - nombre: string    |           | - nombre: string    |
|                     |          | - eslora: float     |           | - apellido: string  |
|                     |          | - manga: float      |           | - dirección: string|
|                     |          +---------------------+           | - teléfono: string  |
| + reservarAmarre() |<>--------| + asignarAmarre()   |           +---------------------+
| + alquilarBarco()   |          +---------------------+
| + registrarSocio()  |                    |
+---------------------+                    |
        /\                                 |
         |                                 |
         |            +-------------------+-------------------+
         |            |             Amarre                  |
         |            +------------------------------------+
         |            | - número: int                      |
         |            | - ocupado: boolean                 |
         |            +------------------------------------+
         |                        |
+-----------------------------+   |
|           Alquiler          |   |
+-----------------------------+   |
| - socio: Socio              |   |
| - barco: Barco              |   |
| - fecha_inicio: Date        |   |
| - fecha_fin: Date           |   |
+-----------------------------+   |
