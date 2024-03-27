# Diagrama de clases biblioteca

+-----------------------+            +------------------------+            +--------------------------+
|      Biblioteca       |            |         Libro          |            |         Usuario          |
+-----------------------+            +------------------------+            +--------------------------+
| - nombre: string      |            | - título: string       |            | - nombre: string         |
| - ubicación: string   |            | - autor: string        |            | - dirección: string      |
+-----------------------+            | - editorial: string    |            +--------------------------+
| + buscarLibro()       |<>----------| - año_publicación: int |<>----------| + buscarLibro()          |
| + prestarLibro()      |            | - disponibilidad: bool|            | + solicitarPrestamo()    |
| + devolverLibro()     |            +------------------------+            +--------------------------+
+-----------------------+                        |
        /\                                       |
         |                                       |
         |                 +----------------------v----------------------+
         |                 |                     Préstamo                |
         |                 +---------------------------------------------+
         |                 | - libro: Libro                               |
         |                 | - usuario: Usuario                           |
         |                 | - fecha_prestamo: DateTime                   |
         |                 | - fecha_devolucion: DateTime                 |
         |                 +---------------------------------------------+
         |
         |
         |
+-----------------------------+
|          Ejemplar           |
+-----------------------------+
| - libro: Libro              |
| - identificador: string     |
+-----------------------------+
