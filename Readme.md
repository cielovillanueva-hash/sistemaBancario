# Sistema Bancario en Python


## 1. Nombre del proyecto


**Sistema Bancario POO** - Programa de consola para gestionar clientes y cuentas bancarias.


## 2. Descripción del sistema


### ¿Qué problema resuelve?
El sistema simula las operaciones básicas que se hacen en un banco, como abrir cuentas, depositar, retirar y transferir dinero. La idea es manejar toda esa información de forma ordenada usando código orientado a objetos, en vez de tener todo suelto en variables sin estructura.


### ¿A qué tipo de usuario está dirigido?
Está pensado para un encargado de banco (o cajero) que use el sistema desde la consola para registrar clientes y manejar sus cuentas. No es para que el cliente lo use directamente, sino para alguien que administra la información.


### Funcionalidades principales
- Registrar clientes nuevos con su RUT y nombre.
- Abrir cuentas corrientes o de ahorro para un cliente.
- Ver el listado completo de clientes con sus cuentas y saldos.
- Depositar dinero en una cuenta.
- Retirar dinero de una cuenta (respetando las reglas de cada tipo).
- Transferir dinero entre dos cuentas.
- Aplicar interés a las cuentas de ahorro.


## 3. Conceptos de POO utilizados


### Encapsulamiento
Los atributos de las clases (como `__numero`, `__titular`, `__saldo`, `__tasa`, `__sobregiro`) son privados, tienen doble guion bajo adelante. No se pueden acceder directamente desde afuera, solo a través de métodos como `get_saldo()`, `get_numero()`, etc. Así se protege la información y se controla cómo se modifica (por ejemplo, `depositar()` valida que el monto sea positivo antes de cambiar el saldo).


### Herencia
La clase `Cuenta` es la clase base, y de ahí heredan `CuentaCorriente` y `CuentaAhorros`. Ambas usan `super().__init__()` para reutilizar el constructor de `Cuenta` y no repetir código (número, titular, saldo se inicializan igual en las dos).


### Abstracción
`Cuenta` es una clase abstracta (hereda de `ABC` y tiene métodos con `@abstractmethod`). No se puede crear un objeto `Cuenta` directamente, solo sirve como modelo para que las subclases implementen `retirar()` e `info()` a su manera. Esto obliga a que toda cuenta tenga esos métodos, pero no dice cómo deben funcionar exactamente.


### Polimorfismo
El método `retirar()` se comporta distinto según el tipo de cuenta:
- En `CuentaCorriente` permite que el saldo quede negativo hasta el límite del sobregiro.
- En `CuentaAhorros` no deja que el saldo quede negativo.


Lo mismo pasa con `info()`, cada clase muestra su información de forma distinta (la corriente muestra el sobregiro, la de ahorro muestra la tasa de interés). Aunque se llama igual el método, cada clase lo ejecuta diferente.


## 4. Criterios de aceptación


1. El sistema debe permitir registrar un cliente nuevo solo si su RUT no está registrado previamente.
2. El sistema debe permitir abrir una cuenta (corriente o de ahorro) únicamente para un cliente ya registrado.
3. El sistema debe rechazar depósitos o retiros con montos menores o iguales a 0, mostrando un mensaje de error.
4. En una cuenta corriente, el sistema debe permitir retirar dinero aunque el saldo quede negativo, siempre que no se supere el límite de sobregiro.
5. En una cuenta de ahorro, el sistema debe impedir retiros que superen el saldo disponible.
6. El sistema debe permitir transferir dinero entre dos cuentas existentes, descontando el monto de la cuenta origen y sumándolo a la cuenta destino.
7. El sistema debe permitir aplicar interés únicamente a cuentas de ahorro, mostrando un mensaje si se intenta aplicar a otro tipo de cuenta.
8. El sistema debe mostrar el listado de clientes con el saldo total y el detalle de cada una de sus cuentas.


## 5. Pruebas de usuario


### Prueba 1: Registrar un cliente nuevo
- **Acción realizada:** Se selecciona la opción 1, se ingresa el RUT "11111111-1" y el nombre "Juan Pérez".
- **Resultado esperado:** El sistema confirma que el cliente "Juan Pérez" fue registrado correctamente.
- **Resultado obtenido:** El sistema mostró el mensaje "Cliente 'Juan Pérez' registrado."
- **Cumple:** Sí


### Prueba 2: Abrir una cuenta corriente
- **Acción realizada:** Se selecciona la opción 2, se ingresa el RUT "11111111-1", tipo "1" (corriente) y saldo inicial "50000".
- **Resultado esperado:** El sistema crea una cuenta corriente asociada al cliente con el saldo ingresado.
- **Resultado obtenido:** El sistema mostró "Cuenta Corriente CTA-001 creada para Juan Pérez."
- **Cumple:** Sí


### Prueba 3: Retirar más dinero del que hay en una cuenta de ahorro
- **Acción realizada:** Se abre una cuenta de ahorro con saldo $10.000 y se intenta retirar $20.000.
- **Resultado esperado:** El sistema no permite el retiro y muestra un mensaje indicando que el saldo es insuficiente.
- **Resultado obtenido:** El sistema mostró "Saldo insuficiente: $10,000" y no modificó el saldo.
- **Cumple:** Sí


### Prueba 4: Transferencia entre cuentas
- **Acción realizada:** Se transfieren $5.000 desde la cuenta CTA-001 (saldo $50.000) hacia la cuenta CTA-002 (saldo $10.000).
- **Resultado esperado:** La cuenta origen queda con $45.000 y la cuenta destino con $15.000.
- **Resultado obtenido:** La cuenta CTA-001 quedó con $45.000 y la CTA-002 con $15.000, mostrando el mensaje de transferencia exitosa.
- **Cumple:** Sí


## Cómo se ejecuta


Solo hay que tener Python instalado y correr:


```
python nombre_del_archivo.py
```


Después se va navegando por el menú escribiendo el número de la opción que se quiere usar.


## Cosas que se podrían mejorar


- Guardar los datos en un archivo para que no se pierdan al cerrar el programa.
- Validar mejor el formato del RUT.
- Agregar más tipos de cuenta.


## Autor


Trabajo hecho por Maickol Ibañez y Cielo Villanueva.
