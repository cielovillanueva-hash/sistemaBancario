# Sistema Bancario en Python

Este es un trabajo para el ramo de programación. La idea es hacer un sistema bancario simple usando los conceptos de programación orientada a objetos que vimos en clases: herencia, polimorfismo, encapsulamiento y clases abstractas.


## ¿Qué hace el programa?

Es un menú por consola donde uno puede:
1. Registrar clientes
2. Abrir cuentas (corriente o de ahorro)
3. Ver el listado de clientes con sus cuentas
4. Depositar dinero
5. Retirar dinero
6. Transferir entre cuentas
7. Aplicar interés a las cuentas de ahorro
0. Salir


## Cómo está organizado

- **Cuenta**: es una clase abstracta, no se puede crear directamente. Tiene los datos básicos como número, titular y saldo, además de los métodos para depositar.
- **CuentaCorriente**: hereda de Cuenta. Tiene sobregiro, o sea se puede retirar más plata de la que hay en la cuenta hasta cierto límite.
- **CuentaAhorros**: también hereda de Cuenta. Tiene una tasa de interés y un método para aplicar ese interés al saldo.
- **Cliente**: guarda los datos de la persona y la lista de cuentas que tiene.
- **Banco**: maneja todo, los clientes, las cuentas y las transferencias entre ellas.

Lo de retirar() es un ejemplo de polimorfismo, porque cada tipo de cuenta lo hace distinto (la corriente permite sobregiro y la de ahorro no).


## Cómo se ejecuta

Solo hay que tener Python instalado y correr:

```
python nombre_del_archivo.py
```
Después se va navegando por el menú escribiendo el número de la opción que se quiere usar.


## Ejemplo de uso

1. Primero hay que registrar un cliente (opción 1)
2. Después abrirle una cuenta con su RUT (opción 2)
3. Ahí ya se le puede depositar plata, retirar, transferir, etc.


## Cosas que se podrían mejorar

- Guardar los datos en un archivo para que no se pierdan al cerrar el programa
- Validar mejor el RUT
- Agregar más tipos de cuenta


## Autor
Trabajo hecho por Maickol Ibañez y Cielo Villanueva.
