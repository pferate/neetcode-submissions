
class Pet:
    def __init__(self, name: str, species: str) -> None:
        self.name: str = name
        self.species: str = species



# Do not modify below this line
my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")
