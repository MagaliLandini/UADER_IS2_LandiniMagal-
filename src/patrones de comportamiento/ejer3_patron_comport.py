from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject:notificando a observadores...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self,id) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: estoy haciendo algo importante.")
        self._state = id

        print(f"Subject:My id cambio a: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 'a3n1':
            print("Suscripcion 1 : reacciono al evento")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 'y6j3':
            print("Suscripcion 2 : reacciono al evento")
class ConcreteObserverC(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 'p2l3':
            print("Suscripcion 3 : reacciono al evento")
class ConcreteObserverD(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 'y4d1':
            print("Suscripcion 4 : reacciono al evento")

if __name__ == "__main__":
    # The client code.
    id1='a3n1'
    id2='poj3'
    id3='p2l3'
    id4='y687'
    id5='y6j3'
    id6='ply7'
    id7='y4d1'
    id8='98ik'
    
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)
    
    observer_c = ConcreteObserverC()
    subject.attach(observer_c)
    
    observer_d = ConcreteObserverD()
    subject.attach(observer_d)
    
    subject.some_business_logic(id1)
    subject.some_business_logic(id2)
    subject.some_business_logic(id3)
    subject.some_business_logic(id4)
    subject.some_business_logic(id5)
    subject.some_business_logic(id6)
    subject.some_business_logic(id7)
    subject.some_business_logic(id8)

    subject.detach(observer_a)
