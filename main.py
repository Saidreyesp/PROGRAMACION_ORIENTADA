from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, cantidad):
        pass

class TarjetaCredito(MetodoPago):
    def procesar_pago(self, cantidad):
        return f"Pago de {cantidad}€ procesado con tarjeta de crédito."

class PayPal(MetodoPago):
    def procesar_pago(self, cantidad):
        return f"Pago de {cantidad}€ procesado con PayPal."

class TransferenciaBancaria(MetodoPago):
    def procesar_pago(self, cantidad):
        return f"Pago de {cantidad}€ procesado mediante transferencia bancaria."

if __name__ == "__main__":
    metodos = [TarjetaCredito(), PayPal(), TransferenciaBancaria()]
    for metodo in metodos:
        print(metodo.procesar_pago(100))
