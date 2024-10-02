class Dog:
    species = "Dog"
    def __init__(self,name,colour,breed,anger):
        self.name = name
        self.colour = colour
        self.breed = breed
        self.anger = anger

hunter = Dog('Jeremy','Black','PITBULL','10')
bluwr = Dog('Lanner','White', 'Golden retriever', '1')

print(f"Hunters name is {hunter.name}, He is {hunter.colour} and his breed is {hunter.breed}. His scary rating is {hunter.anger}")
print(f"Bluwrs name is {bluwr.name}, He is {bluwr.colour} and his breed is {bluwr.breed}. His scary rating is {bluwr.anger}")