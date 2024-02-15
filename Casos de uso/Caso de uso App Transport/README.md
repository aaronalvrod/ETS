# Casos de uso

## Tarea App Transport

### Descripción

Realiza la especificación de los casos de uso asociados al diagrama explicativo anteriormente. Edita todo utilizando markdown y súbelo a tu repositorio de la asignatura.

Documenta adecuadamente cada caso de uso y los actores

## Caso de uso App Transport

**Actores**

- Administrador
- Usuario
- Sistema de geoposicionamiento externoç

**Descripción**

Este caso de uso describe el proceso de gestión de viajes dentro de la aplicación de transporte.

**Flujo básico**

- El administrador define el medio de transporte.
- El administrador define el precio del transporte.
- El administrador gestiona el alta y baja de usuarios.
- El usuario se da de alta en la aplicación.
- El usuario inicia sesión en la aplicación.
- El usuario utiliza el sistema de geoposicionamiento para establecer su ubicación actual.
- El usuario define su destino.
- El usuario modifica la ruta si es necesario.
- El sistema de geoposicionamiento calcula la ruta óptima hasta el destino.
- El usuarui confirma la ruta.

**Extensiones**

- El usuario seleciiona "Sugerir Destinos Interesantes":
    - El sistema muestra una lista de destinos interesantes cercanos.
    - El usuario selecciona una de los destinos sugeridos.
    - El sistema calcula la ruta óptima hasta el destino seleccionado.
- El usuario selecciona "Mostrar Puntos de Interés en Ruta":
    - El sistema muestra los puntos de interés que se encuentran en la ruta.
    - El usuario visualiza los puntos de interes en el mapa.

**Precondiciones**

- El administrador tiene permisos para definir el medio de transporte y el precio.
- El usuario ha iniciado sesión en la aplicación.
- El sistema de geoposicionamiento externo está disponible.

**Postcondiciones**

- Se ha definido la ruta del viaje.
- El usuario a confirmado la ruta.