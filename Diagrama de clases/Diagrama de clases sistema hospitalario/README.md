# Diagrama de clases sistema hospitalario

+-------------------+          +-----------------------+         +-------------------+
|      Hospital     |          |        Paciente       |         |       Doctor      |
+-------------------+          +-----------------------+         +-------------------+
| - nombre: string  |          | - nombre: string      |         | - nombre: string  |
| - dirección: string|          | - fecha_nacimiento:  |         | - especialidad:   |
| - teléfono: string|          |   fecha              |         |                   |
|                   |          +-----------------------+         |                   |
| + registrarPaciente()|       | + registrarPaciente()|         | + atenderPaciente()|
| + registrarDoctor() |       | + reservarCita()      |         | + recetarMedicina()|
| + programarCirugía()|       |                       |         +-------------------+
+-------------------+          +-----------------------+
         |                             |       /\
         |                             |        |
         |              +--------------+--------+-------------+
         |              |                                     |
         |        +------------+                      +---------------+
         |        |   Enfermera|                      |     Cita      |
         |        +------------+                      +---------------+
         |        | - nombre: string                 | - fecha: Date  |
         |        | - fecha_nacimiento: fecha        | - hora: Time   |
         |        |                                  | - paciente: Paciente |
         |        |                                  | - doctor: Doctor |
         |        +----------------------------------+ - enfermera: Enfermera|
         |                                            +---------------+
         |
         |
         |          +-------------------+
         |          |     Cirugía       |
         |          +-------------------+
         |          | - fecha: Date     |
         |          | - hora: Time      |
         |          | - tipo: string    |
         |          | - paciente: Paciente |
         |          | - doctor: Doctor  |
         |          | - enfermera: Enfermera|
         |          +-------------------+
         |
         |
         |
         |
         |
         |
         |
         |
+---------------------------+
|          Medicina         |
+---------------------------+
| - nombre: string          |
| - descripción: string     |
| - fabricante: string      |
| - precio: double          |
+---------------------------+

