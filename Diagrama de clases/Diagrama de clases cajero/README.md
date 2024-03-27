# Diagrama de clases cajero automatico

+-----------------------------------------+
|              CajeroAutomatico           |
+-----------------------------------------+
| -usuarios: List<Usuario>                |
| -administrador: Administrador          |
+-----------------------------------------+
| +agregarUsuario(usuario: Usuario): void |
| +eliminarUsuario(usuario: Usuario): void|
| +ingresarUsuario(usuario: Usuario): void|
| +retirarUsuario(usuario: Usuario): void |
| +realizarTransferencia(                  |
|    usuarioOrigen: Usuario,              |
|    usuarioDestino: Usuario,             |
|    monto: double): boolean              |
| +ingresarDinero(usuario: Usuario,       |
|    monto: double): boolean              |
| +retirarDinero(usuario: Usuario,        |
|    monto: double): boolean              |
| +consultarSaldo(usuario: Usuario): double|
+-----------------------------------------+

+-----------------------------------------+
|                 Usuario                 |
+-----------------------------------------+
| -idUsuario: int                         |
| -pin: string                            |
| -saldo: double                         |
+-----------------------------------------+
| +getIdUsuario(): int                    |
| +getPin(): string                       |
| +getSaldo(): double                     |
| +setIdUsuario(idUsuario: int): void     |
| +setPin(pin: string): void              |
| +setSaldo(saldo: double): void          |
+-----------------------------------------+

+-----------------------------------------+
|            Administrador               |
+-----------------------------------------+
| -idAdmin: int                          |
| -pin: string                           |
+-----------------------------------------+
| +getIdAdmin(): int                     |
| +getPin(): string                      |
| +setIdAdmin(idAdmin: int): void        |
| +setPin(pin: string): void             |
+-----------------------------------------+


