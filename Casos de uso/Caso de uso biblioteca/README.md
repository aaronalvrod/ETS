# Casos de uso

## Tarea Casos de uso de una biblioteca

### Descripción

Desarrolla un diagrama de casos de uso para un sistema de biblioteca. Los actores pueden ser "Usuario" y "Bibliotecario". Algunos casos de uso podrían ser "Prestar Libro", "Devolver Libro", "Buscar Libro", etc.

Documenta la especificación en markdown, y súbelo a tu cuenta de github

## Caso de uso Biblioteca

Casos de Uso para Usuario:

#### Buscar Libro:

**Descripción**

- El usuario busca un libro en el sistema.

**Actores**
- Usuario

**Flujo Principal**

-El usuario ingresa términos de búsqueda en el sistema.
-El sistema muestra una lista de libros que coinciden con los términos de búsqueda.

**Flujo Alternativo**

Si no se encuentran resultados, el sistema muestra un mensaje indicando que no se encontraron libros.

#### Ver Información del Libro:

**Descripción**

- El usuario ve información detallada sobre un libro específico.

**Actores**

- Usuario

**Flujo Principal**

- El usuario selecciona un libro de la lista de resultados de búsqueda o del catálogo.
- El sistema muestra información detallada sobre el libro, como título, autor, sinopsis, etc.

#### Solicitar Préstamo

**Descripción**

- El usuario solicita el préstamo de un libro disponible.

**Actores**

- Usuario

**Flujo Principal**

- El usuario selecciona un libro disponible.
- El usuario solicita el préstamo del libro.
- El sistema registra el préstamo y actualiza el estado del libro a "prestado".

#### Devolver Libro:

**Descripción**

- El usuario devuelve un libro prestado.

**Actores**

- Usuario


**Flujo Principal**

- El usuario devuelve un libro prestado en la biblioteca.
- El bibliotecario registra la devolución del libro en el sistema.
- El sistema actualiza el estado del libro a "disponible".