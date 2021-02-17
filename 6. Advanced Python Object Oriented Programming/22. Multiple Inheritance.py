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
        # User.attack(self) # goes to user class and then calls attack
        print(f"Attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f"Attacking with arrows: Arrows left - {self.num_arrows}")

    def check_arrows(self):
        print(f'{self.num_arrows} remaining')

    def run(self):
        print('ran really fast')

class HybridBorg(Wizard, Archer): # inherit from Wizard first, then Archer
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)

wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)

hb1 = HybridBorg('Borg', 50, 100)
hb1.run()
print(hb1.check_arrows())
print(hb1.attack())

