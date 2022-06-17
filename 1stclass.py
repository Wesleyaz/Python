class Animal:
    nbarks = 0 #attribute|instance
    name = ""
    def __init__(self, z): #Constructor executed is class is created
        self.name = z
        print(self.name, 'was created')

    def bark(self): #method, self passes the own class as a parameter
        self.nbarks = self.nbarks + 1
        print(self.name,"barked",self.nbarks,'x so far')

    def __del__(self): #Contructor executed when class is being erased
        print(self.name,'was destructed and barked', self.nbarks, 'x')

class Person(Animal): #Subclass(Inheritance): Receives everything from class Animal 
    nhold = 0
    def holds(self):
        self.nhold += 1
        self.bark()
        print(self.name, 'barked', self.nbarks, 'x and person holded', self.nhold, 'x')
        
x = Animal("Spikey")
x.bark()

y = Person("Leo")
y.holds()
y.bark()