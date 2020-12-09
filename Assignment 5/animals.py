
class Animals:
    def __init__(self,legs=4,eyes=2):
       self.legs=legs
       self.eyes=eyes

class domestic_animals(Animals):
    def place(self):
        print("Area habitated by Human Beings")

class cow(domestic_animals):
    def speak(self):
        print("Moo")
    def color(self):
        print("White,Black,Brown,etc")

class dog(domestic_animals):
    def speak(self):
        print("Bark")
    def color(self):
        print("White, Black, Brown, etc")

class goat(domestic_animals):
    def speak(self):
        print("Maa")
    def color(self):
        print("White, Black, Brown, etc")

class horse(domestic_animals):
    def speak(self):
        print("Whinny")
    def color(self):
        print("White, Black, Brown, etc")

class sheep(domestic_animals):
    def speak(self):
        print("Baa")
    def color(self):
        print("White")

class wild_animals(Animals):
    def place(self):
        print("Jungle")

class herbivores(wild_animals):
    def food(self):
        print("Plants")

class deer(herbivores):
    def speak(self):
        print("bellow")
    def color(self):
        print("reddish brown, grayish brown")

class elephant(herbivores):
    def speak(self):
        print("trumpet")
    def color(self):
        print("grayish black")

class giraffe(herbivores):
    def speak(self):
        print("bleat")
    def colour(self):
        print("dark brown, orange, stc")
class carnivores(wild_animals):
    def food(self):
        print("meat, flesh")

class lion(carnivores):
    def speak(self):
        print("roar")
    def color(self):
        print("white, tawny yellow, ash brown, ochre, deep orange-brown")

class tiger(carnivores):
    def speak(self):
        print("roar")
    def color(self):
        print("dark brown, grey to black")

class wolf(carnivores):
    def speak(self):
        print("howl")
    def color(self):
        print("white, grizzled with browns, greys, black")


sheru = goat()
sheru.speak()
sheru.place()
sheru.color()

print(sheru.legs)
print(sheru.eyes)

#l = lion()
#l.speak()

