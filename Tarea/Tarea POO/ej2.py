from clases import *

cuenta01 = Cuenta()
print(f"Saldo: {cuenta01.getSaldo()}")
cuenta01.deposito(2000)
print(f"Saldo: {cuenta01.getSaldo()}")
cuenta01.retiro(3000)
print(f"Saldo: {cuenta01.getSaldo()}")
cuenta01.retiro(1500)
print(f"Saldo: {cuenta01.getSaldo()}")