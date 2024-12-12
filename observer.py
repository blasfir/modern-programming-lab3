from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass
    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass
    @abstractmethod
    def inform(self) -> None:
        pass
class SubclassSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []
    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    def inform(self) -> None:
        print("Subject: Informing observers.")
        for observer in self._observers:
            observer.update(self)
    def some_business_logic(self) -> None:
        print("Subject: Realization business logic.")
        self._state = randrange(0, 10)
        print(f"Subject: My state has just changed to: {self._state}.")
        self.inform()
class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass
class SubclassObserver1(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state > 5:
            print("SubclassObserver1: Reacted to the event.")
class SubclassObserver2(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 3:
            print("SubclassObserver2: Reacted to the event.")
if __name__ == "__main__":
    subject = SubclassSubject()
    observer_1 = SubclassObserver1()
    subject.attach(observer_1)
    observer_2 = SubclassObserver2()
    subject.attach(observer_2)
    subject.some_business_logic()
    subject.some_business_logic()
    subject.detach(observer_1)
    subject.some_business_logic()

    
