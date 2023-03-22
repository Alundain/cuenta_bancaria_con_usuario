class CuentaBancaria:
    todas_las_ctas = []
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.todas_las_ctas.append(self)
    
    def hacer_deposito(self, monto):
        self.balance += monto
        return self
    
    def hacer_retiro(self, monto):
        if monto > self.balance:
            self.balance -= 5
            print ("Fondos insuficientes, se restarán $ 5")
        else: 
            self.balance -= monto
        return self

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.cuenta = CuentaBancaria(tasa_interes=0.02, balance=0)

    def hacer_deposito(self):
        self.cuenta.deposito(100)
        print(self.balance.cuenta)
        return self

    def hacer_retiro(self, monto):
        self.cuenta.retiro(50)
        print(self.balance.cuenta)
        return self

    def mostrar_balance(self):
        print(f"El cliente {self.nombre} tiene en su cuenta : $ {self.cuenta}")
        return self
        
usuario_1 = Usuario('Andrea', 'correo@correo.cl')
usuario_1.mostrar_balance()

