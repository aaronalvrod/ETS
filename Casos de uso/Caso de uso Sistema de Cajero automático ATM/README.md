# Casos de uso

## Tarea Casos de uso Sistema de Cajero automático ATM

### Descripción

Crea un diagrama de casos de uso para un sistema de CAJERO. Los actores pueden ser "Administrador" y "Cliente bancario". Algunos casos de uso podrían ser "Hacer lógin", "Realizar transferencia", "Ingresar dinero", "ver saldo", "poner dinero al móvil",etc.

Documenta en Markdown y súbelo a github. El repositorio tendrá el nombre de Gestión de Cajero

## Caso de uso Sistema de Cajero automático ATM

#### Caso de uso para cliente bancario

---

#### Hacer Login

**Descripción**

- El cliente bancario inicia sesión en el sistema del cajero automático para acceder a sus servicios.

**Actores**

- Cliente Bancario

**Flujo Principal**

- El cliente introduce su tarjeta bancaria en el lector de tarjetas del cajero automático.

- El sistema solicita al cliente que ingrese su PIN (Número de Identificación Personal).

- El cliente introduce su PIN usando el teclado numérico.

- El sistema verifica el PIN ingresado.

- Si el PIN es válido, el sistema permite al cliente acceder a las funciones del cajero automático.

---

#### Realizar Transferencia

**Descripción**

- El cliente bancario transfiere dinero entre cuentas bancarias.

**Actores**

- Cliente Bancario

**Flujo Principal**

- El cliente selecciona la opción de transferencia de dinero en el menú del cajero automático.

- El cliente elige entre transferencia entre cuentas propias o a terceros.

- El cliente ingresa el número de cuenta de destino y el monto a transferir.

- El sistema verifica la información ingresada por el cliente.

- Si la información es válida, el sistema realiza la transferencia y actualiza los saldos de las cuentas involucradas.

---

#### Ingresar Dinero

**Descripción**

- El cliente bancario ingresa dinero en efectivo a su cuenta bancaria.

**Actores**

- Cliente Bancario

**Flujo Principal**

- El cliente selecciona la opción de ingreso de dinero en el menú del cajero automático.

- El cliente introduce el efectivo en el alimentador de billetes del cajero automático.

- El sistema cuenta y verifica el dinero ingresado.

- El sistema actualiza el saldo de la cuenta bancaria del cliente con el monto ingresado.

---

#### Ver Saldo

**Descripción**

- El cliente bancario consulta el saldo disponible en su cuenta bancaria.

**Actores**

- Cliente Bancario

**Flujo Principal**

- El cliente selecciona la opción de consulta de saldo en el menú del cajero automático.

- El sistema solicita al cliente que seleccione la cuenta de la cual desea consultar el saldo.

- El cliente elige la cuenta deseada.

- El sistema muestra el saldo disponible en la cuenta seleccionada.

---

#### Poner Dinero al Móvil

**Descripción**

- El cliente bancario recarga su teléfono móvil con saldo utilizando el cajero automático.

**Actores**

- Cliente Bancario

**Flujo Principal**

- El cliente selecciona la opción de recarga de saldo para móvil en el menú del cajero automático.

- El cliente introduce el número de teléfono móvil al que desea recargar saldo.

- El cliente selecciona el monto de la recarga.

- El sistema verifica la información ingresada.

- El sistema realiza la recarga de saldo en el teléfono móvil especificado.