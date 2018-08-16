"""
x = 2
y = 3
def add_nums():
    x = 5
    y = 6
    return x + y

print(add_nums())
"""
from shutil import move

"""
def say_hi():
    return 'hi!'


i = 789


class MyClass(object):
    i = 5

    def prepare(self):
        i = 10
        self.i = 123
        print(i)

    def say_hi(self):
        return 'Hi there!'

    def say_something(self):
        print(say_hi())

    def say_something_else(self):
        print(self.say_hi())


a = MyClass()

a.say_something()
# hi!

a.say_something_else()
# Hi there!
a.prepare()
"""

from clases import *
from menu import *

listSimbl = ['♥', '♦', '♣', '♠']

print(listSimbl.pop())
print(listSimbl)
x = listSimbl.pop()
print(x)
print(listSimbl)
y = '♦' in listSimbl
print(y)

nombre = Presentar_Menu()

jugador1 = Jugador(nombre[0])

print(jugador1.nombre)

Mostrar_Carta(listCartas)
