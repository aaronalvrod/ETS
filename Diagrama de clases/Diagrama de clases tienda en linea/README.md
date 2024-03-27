# Diagrama de clases tienda en linea

+-----------------------+          +-----------------------+           +-----------------------+
|       TiendaOnline    |          |        Producto       |           |         Cliente       |
+-----------------------+          +-----------------------+           +-----------------------+
|                       |          |                       |           |                       |
|                       |          | - id: int             |           | - id: int             |
|                       |          | - nombre: string      |           | - nombre: string      |
|                       |          | - descripción: string |           | - apellido: string    |
|                       |          | - precio: float       |           | - email: string       |
|                       |          | - stock: int          |           | - dirección: string   |
|                       |          |                       |           |                       |
| + buscarProducto()    |          |                       |           |                       |
| + comprarProducto()   |          |                       |           |                       |
| + verCarrito()        |          |                       |           |                       |
+-----------^-----------+          +-----------^-----------+           +-----------^-----------+
            |                                  |                                   |
            |                                  |                                   |
            |                                  |                                   |
+-----------^-----------+          +-----------^-----------+           +-----------^-----------+
|       Carrito         |          |         Pago         |           |       Envío          |
+-----------------------+          +-----------------------+           +-----------------------+
| - productos: Producto[]|          | - total: float       |           | - cliente: Cliente    |
| - cliente: Cliente    |          | - métodoPago: string |           | - dirección: string   |
+-----------------------+          |                       |           | - estado: string      |
| + agregarProducto()   |          |                       |           | - fechaEnvio: Date    |
| + quitarProducto()    |          |                       |           | - fechaEntrega: Date  |
| + vaciarCarrito()     |          |                       |           +-----------------------+
| + realizarPago()      |          +-----------------------+
+-----------------------+
