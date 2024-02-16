# Casos de uso

## Tarea Casos de uso Reserva de Vuelos

### Descripción

Crea un diagrama de casos de uso para un sistema de reservas de vuelos. Los actores pueden ser "Pasajero" y "Agente de Reservas". Algunos casos de uso podrían ser "Buscar Vuelo", "Reservar Vuelo", "Cancelar Reserva", etc.

Documenta en Markdown y súbelo a github. El repositorio tendrá el nombre de Reserva de vuelos

## Caso de uso Reserva de Vuelos

Casos de Uso para Agente de Reservas:

---

### Buscar Vuelo

**Descripción**

- El agente de reservas busca vuelos disponibles en el sistema para ayudar a los pasajeros.

**Actores**

- Agente de Reservas

**Flujo Principal**

- El agente de reservas ingresa los detalles del viaje proporcionados por el pasajero.

- El sistema muestra una lista de vuelos disponibles que coinciden con los criterios de búsqueda del agente de reservas.

---

### Reservar Vuelo

**Descripción**

- El agente de reservas realiza una reserva en nombre de un pasajero.

**Actores**

- Agente de Reservas

**Flujo Principal**

- El agente de reservas selecciona un vuelo adecuado para el pasajero.

- El agente de reservas recopila la información necesaria del pasajero y realiza la reserva en el sistema.

- El sistema confirma la reserva y emite un número de reserva.

---

### Cancelar Reserva

**Descripción**

- El agente de reservas cancela una reserva existente en nombre de un pasajero.
Actores: Agente de Reservas

**Flujo Principal**

- El agente de reservas accede al sistema y busca la reserva del pasajero utilizando el número de reserva o la información proporcionada.

- El agente de reservas selecciona la reserva que se va a cancelar.

- El sistema confirma la cancelación de la reserva y actualiza el estado de la reserva.
Modificar Reserva:

**Descripción**

- El agente de reservas modifica una reserva existente en nombre de un pasajero.

**Actores**

- Agente de Reservas

**Flujo Principal**

- El agente de reservas accede al sistema y busca la reserva del pasajero utilizando el número de reserva o la información proporcionada.

- El agente de reservas realiza los cambios necesarios en la reserva, como cambiar la fecha o la hora del vuelo, actualizar los detalles del pasajero, etc.

- El sistema confirma los cambios y actualiza la reserva.