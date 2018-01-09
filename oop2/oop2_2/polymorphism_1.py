class Animal:
    def eat(self):          #1
        print('eat something')

class Lion(Animal):
    def eat(self):          #2
        print('eat meat')

class Deer(Animal):
    def eat(self):          #3
        print('eat grass')

class Human(Animal):
    def eat(self):          #4
        print('eat meat and grass')

if __name__ == "__main__":
    animals = []           #5
    animals.append(Lion())
    animals.append(Deer())
    animals.append(Human())

    for animal in animals:
        animal.eat()        #6
