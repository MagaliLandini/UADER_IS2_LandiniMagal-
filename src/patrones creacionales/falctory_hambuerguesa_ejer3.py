#!/usr/bin/python3.7
#*--------------------------------------------------
#* factory.py
#* excerpt from https://refactoring.guru/design-patterns/factory/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = product.operation()

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class CreatorEnvioPorDelivery(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def factory_method(self) -> Product:
        return EnvioPorDelivery()


class CreatorEntregadoPorMostrador(Creator):
    def factory_method(self) -> Product:
        return EntregadoPorMostrador()

class CreatorRetiradoPorCliente(Creator):
    def factory_method(self) -> Product:
        return RetiradoPorCliente()


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class EnvioPorDelivery(Product):
    def operation(self) -> str:
        return "envio por delivery"


class EntregadoPorMostrador(Product):
    def operation(self) -> str:
        return "Entregada por mostrador"


class RetiradoPorCliente(Product):
    def operation(self) -> str:
        return "Retirada por el cliente"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long ascreator.some_operation() the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

   # print(f"Yo soy un mero intermediario tipo FACTORY que no se que es lo que estoy creando, pero lo creo.\n"
        #  f"{creator.some_operation()}", end="")
    print(creator.some_operation())


if __name__ == "__main__":
    print("Creando una hambuerguesa")
    cliente1 = client_code(CreatorEnvioPorDelivery())
    print("\n")

    print("Creando una hambuerguesa")
    cliente2=client_code(CreatorEntregadoPorMostrador())
    print("\n")

    print("Creando una hambuerguesa")
    cliente3=client_code(CreatorRetiradoPorCliente())
