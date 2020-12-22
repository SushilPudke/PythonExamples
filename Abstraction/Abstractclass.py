# Demo Abstract Class, Abstract Method
from abc import ABC, abstractmethod
class Parent(ABC):
    #common functionality
    def common(self):
       print('In common method of Parent')
    @abstractmethod
    def vary(self):
        pass

class Child1(Parent):
    def vary(self):
       print('In vary method of Child1')

class Child2(Parent):
    def vary(self):
       print('In vary method of Child2')

# object of Child1 class
obj = Child1()
obj.common()
obj.vary()
# object of Child2 class
obj = Child2()
obj.common()
obj.vary()