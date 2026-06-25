class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes
print("Initial Attributes: Whiskers (cat) - Hunger: 6, Energy: 8")

# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
#  - Increase energy by 2
whiskers.hunger -= 3
whiskers.energy += 2

# TODO: Print Whiskers' modified attributes
print("Modified Attributes: Whiskers (cat) - Hunger: 3, Energy: 10")
