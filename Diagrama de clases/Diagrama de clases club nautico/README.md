# Diagrama de clases club nautico

+-----------------+          +-------------------+          +-----------------+
|    ClubNautico  |          |      Barco        |          |      Socio      |
+-----------------+          +-------------------+          +-----------------+
| - nombre: string|          | - nombre: string  |          | - nombre: string|
| - ubicación: string       | - eslora: float   |          | - apellido: string |
|                        | - manga: float    |          | - dirección: string|
|                        | - tipo: string     |          | - teléfono: string|
+-----------------+          |                   |          +-----------------+
| + reservarAmarre() |          |                   |          | + reservarAmarre()|
| + alquilarBarco()  |          |                   |          | + alquilarBarco() |
| + registrarSocio() |          |                   |          | + pagarCuota()    |
+-----------------+          +-------------------+          +-----------------+
        |                          /\                             /\
        |                           |                              |
        |            +--------------+-------------------+   +----------------------+
        |            |         Amarre             |   |   Alquiler               |
        |            +---------------------------+   +----------------------+
        |            | - barco: Barco            |   | - barco: Barco         |
        |            | - socio: Socio            |   | - socio: Socio         |
        |            | - fecha_inicio: Date      |   | - fecha_inicio: Date   |
        |            | - fecha_fin: Date         |   | - fecha_fin: Date      |
        |            +---------------------------+   | - precio: float        |
        |                                           +-------------------------+
        |
        |
        |
        |
        |
+-------------------------+
|         Cuota           |
+-------------------------+
| - socio: Socio          |
| - fecha_pago: Date      |
| - monto: float          |
+-------------------------+
