#!/usr/python
#*--------------------------------------------------
#* singleton.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
#    def some_business_logic(self):
#        """
#        Finally, any singleton should define some business logic, which can be
#        executed on its instance.
#        """
#
#
    #función que calcula el factorial
    def getfactorial(self, num): 
        if num < 0: 
            print("Factorial de un número negativo no existe")

        elif num == 0: 
            return 1
            
        else: 
            fact = 1
            while(num >= 1): 
                fact *= num 
                num -= 1
            return(fact)



if __name__ == "__main__":
    # The client code.
    num=int(input('ingrese un numero para calcular el factorial: '))
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
        print("\n")
        print("Factorial de ", num, "es ", s1.getfactorial(num))
    else:
        print("Singleton failed, variables contain different instances.")

