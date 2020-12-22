class Duck:
    def sound(self):
        print('Quack Quack')

class Cat:
    def sound(self):
        print('Meow Meow')

class Human:
    def sound(self):
        print('Hey hello')

class Test:
    def invoke(self, obj):
       obj.sound()

t = Test()
obj = Duck()
t.invoke(obj)

obj = Cat()
t.invoke(obj)

obj = Human()
t.invoke(obj)