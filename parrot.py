class Parrot:

    species = 'Bird'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
blue = Parrot('blue',15)
woo = Parrot('woo', 10)

print(f"Blue is a {blue.species}")
print(f"Woo is also a {woo.species}")

print(f"{blue.name} is {blue.age} years old")
print(f"{woo.name} is {woo.age} years old")
