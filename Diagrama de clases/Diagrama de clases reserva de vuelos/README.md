# Diagrama de clases reserva de vuelos

+---------------------+          +-----------------------+          +------------------------+
|       Vuelo         |          |       Pasajero        |          |       AgenteReservas   |
+---------------------+          +-----------------------+          +------------------------+
| - númeroVuelo: int  |          | - nombre: string      |          | - nombre: string        |
| - aerolinea: string |          | - apellido: string    |          | - apellido: string      |
| - origen: string    |          | - númeroPasaporte: string |       | - identificación: string|
| - destino: string   |          +-----------------------+          +------------------------+
| - fecha: Fecha      |                  /\                              /\                      |
| - hora: Hora        |                  |                               |                       |
+---------------------+                  |                               |                       |
       |                                 |                               |                       |
       |                                 |                               |                       |
       |                                 |                               |                       |
       |                                 |                               |                       |
+------v----------------+                 |                               |                       |
|      Reserva         |                 |                               |                       |
+----------------------+                 |                               |                       |
| - vuelo: Vuelo       |                 |                               |                       |
| - pasajero: Pasajero |                 |                               |                       |
| - fechaReserva: Fecha|                 |                               |                       |
| - asiento: string    |                 |                               |                       |
+----------------------+                 |                               |                       |
                                          |                               |                       |
+-----------------------------------------+-------------------------------+                       |
|                                                                                                    |
|                                           Aeropuerto                                               |
|                                                                                                    |
+-----------------------------------------+------------------------------------------------------+
| - código: string                        |                                                       |
| - nombre: string                        |                                                       |
| - ciudad: string                        |                                                       |
| - país: string                          |                                                       |
| - listaVuelos: Lista<Vuelo>             |                                                       |
+-----------------------------------------+------------------------------------------------------+
