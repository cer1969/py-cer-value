# CRISTIAN ECHEVERRÍA RABÍ

from cer.value import deco

#-----------------------------------------------------------------------------------------

class Tester(object):
    
    def __init__(self):
        self._name = "Sin nombre"
        self._age = 0
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    @deco.ge(0)
    @deco.le(80)
    def age(self, value):
        self._age = value


j = Tester()
j.name = "José"
j.age = 85

print(j.name)
print(j.age)
