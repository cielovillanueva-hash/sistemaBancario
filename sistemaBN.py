from abc import ABC, abstractmethod




#clase abstracta
class Cuenta(ABC):
    def __init__(self, numero, titular, saldo=0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo




    def get_numero(self):    return self.__numero
    def get_titular(self):   return self.__titular
    def get_saldo(self):     return self.__saldo




    def depositar(self, monto):
        if monto <= 0: return " Monto inválido."
        self.__saldo += monto
        return f" Depósito de ${monto:,.0f}. Saldo: ${self.__saldo:,.0f}"




    def _descontar(self, monto): self.__saldo -= monto




    @abstractmethod
    def retirar(self, monto): pass  




    @abstractmethod
    def info(self): pass            








#herencia de cuenta corriente
class CuentaCorriente(Cuenta):
    def __init__(self, numero, titular, saldo=0, sobregiro=100000):
        super().__init__(numero, titular, saldo)
        self.__sobregiro = sobregiro




    def retirar(self, monto):   #polimorfismo
        if monto <= 0: return " Monto inválido."
        if monto > self.get_saldo() + self.__sobregiro:
            return f" Límite superado. Disponible: ${self.get_saldo() + self.__sobregiro:,.0f}"
        self._descontar(monto)
        return f" Retiro de ${monto:,.0f}. Saldo: ${self.get_saldo():,.0f}"




    def info(self):             #polimorfismo
        return (f"  Corriente | N°{self.get_numero()} | {self.get_titular()} "
                f"| Saldo: ${self.get_saldo():,.0f} | Sobregiro: ${self.__sobregiro:,.0f}")








 #herencia cuenta ahorros
class CuentaAhorros(Cuenta):
    def __init__(self, numero, titular, saldo=0, tasa=0.005):
        super().__init__(numero, titular, saldo)
        self.__tasa = tasa




    def retirar(self, monto):   #polimorfismo
        if monto <= 0: return " Monto inválido."
        if monto > self.get_saldo(): return f" Saldo insuficiente: ${self.get_saldo():,.0f}"
        self._descontar(monto)
        return f" Retiro de ${monto:,.0f}. Saldo: ${self.get_saldo():,.0f}"




    def aplicar_interes(self):
        interes = self.get_saldo() * self.__tasa
        self.depositar(interes)
        return f" Interés +${interes:,.0f} ({self.__tasa*100:.1f}%). Saldo: ${self.get_saldo():,.0f}"




    def info(self):             #polimorfismo
        return (f"  Ahorros   | N°{self.get_numero()} | {self.get_titular()} "
                f"| Saldo: ${self.get_saldo():,.0f} | Tasa: {self.__tasa*100:.1f}%")








#clase cliente
class Cliente:
    def __init__(self, rut, nombre):
        self.__rut = rut
        self.__nombre = nombre
        self.__cuentas = []




    def get_rut(self):     return self.__rut
    def get_nombre(self):  return self.__nombre
    def get_cuentas(self): return list(self.__cuentas)
    def agregar_cuenta(self, c): self.__cuentas.append(c)




    def resumen(self):
        total = sum(c.get_saldo() for c in self.__cuentas)
        cuentas_str = "\n".join(f"    {c.info()}" for c in self.__cuentas) or "    Sin cuentas"
        return (f"  RUT: {self.__rut} | {self.__nombre} | "
                f"Saldo total: ${total:,.0f}\n{cuentas_str}")








#clase banco
class Banco:
    def __init__(self):
        self.__clientes = {}   #rut cliente
        self.__cuentas  = {}   #numero cuenta
        self.__contador = 1




    def _nuevo_numero(self):
        n = f"CTA-{self.__contador:03d}"; self.__contador += 1; return n




    def registrar_cliente(self, rut, nombre):
        if rut in self.__clientes: return " RUT ya registrado."
        self.__clientes[rut] = Cliente(rut, nombre)
        return f" Cliente '{nombre}' registrado."




    def abrir_cuenta(self, rut, tipo, saldo=0):
        c = self.__clientes.get(rut)
        if not c: return " Cliente no encontrado."
        n = self._nuevo_numero()
        cuenta = (CuentaCorriente(n, c.get_nombre(), saldo) if tipo == "1"
                  else CuentaAhorros(n, c.get_nombre(), saldo) if tipo == "2"
                  else None)
        if not cuenta: return " Tipo inválido."
        c.agregar_cuenta(cuenta); self.__cuentas[n] = cuenta
        tipo_str = "Corriente" if tipo == "1" else "Ahorros"
        return f" Cuenta {tipo_str} {n} creada para {c.get_nombre()}."




    def get_cuenta(self, n): return self.__cuentas.get(n.upper())




    def transferir(self, origen, destino, monto):
        co, cd = self.get_cuenta(origen), self.get_cuenta(destino)
        if not co: return " Cuenta origen no encontrada."
        if not cd: return " Cuenta destino no encontrada."
        res = co.retirar(monto)
        if res.startswith(""): cd.depositar(monto); return f" Transferencia de ${monto:,.0f}: {origen} → {destino}"
        return res




    def listar_clientes(self):
        if not self.__clientes: return "  Sin clientes registrados."
        return "\n".join(c.resumen() for c in self.__clientes.values())








#menu principal
def num(msg):
    while True:
        try: return float(input(msg))
        except ValueError: print(" Ingresa un número.")




def main():
    b = Banco()
    menu = ["1. Registrar cliente", "2. Abrir cuenta", "3. Ver clientes",
            "4. Depositar", "5. Retirar", "6. Transferir",
            "7. Aplicar interés (ahorro)", "0. Salir"]
    while True:
        print("\n══════════════════════════════")
        print("       SISTEMA BANCARIO     ")
        print("══════════════════════════════")
        for m in menu: print(f"  {m}")
        print("══════════════════════════════")
        op = input("  Opción: ").strip()




        if op == "1":
            print(f"  {b.registrar_cliente(input('  RUT   : '), input('  Nombre: '))}")




        elif op == "2":
            print("  1. Corriente  2. Ahorros")
            print(f"  {b.abrir_cuenta(input('  RUT: '), input('  Tipo (1/2): '), num('  Saldo inicial: $'))}")




        elif op == "3":
            print("\n" + b.listar_clientes())




        elif op in ("4", "5"):
            n = input("  N° cuenta: "); c = b.get_cuenta(n)
            if c: print(f"  {c.depositar(num('  Monto: $')) if op=='4' else c.retirar(num('  Monto: $'))}")
            else: print("Cuenta no encontrada.")




        elif op == "6":
            print(f"  {b.transferir(input('  Origen : '), input('  Destino: '), num('  Monto  : $'))}")




        elif op == "7":
            c = b.get_cuenta(input("  N° cuenta de ahorros: "))
            if isinstance(c, CuentaAhorros): print(f"  {c.aplicar_interes()}")
            elif c: print("Solo aplica a cuentas de ahorros.")
            else: print("Cuenta no encontrada.")




        elif op == "0":
            print("\n¡Hasta pronto!\n"); break
        else:
            print("Opción inválida.")




if __name__ == "__main__":
    main()
