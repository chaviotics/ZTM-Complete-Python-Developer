class User(object):
    def sign_in(self):
        return "Signed In"
    
    def attack(self):
        print("Do nothings")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        User.attack(self) # goes to user class and then calls attack
        print(f"Attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f"Attacking with arrows: Arrows left - {self.num_arrows}")

wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)

def player_attack(char): # Polymorphism Part
    char.attack()

# player_attack(wizard1)
# player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()