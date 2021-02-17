class PlayerCharacter():
    def __init__(self, name, age):
        self.__name = name # private
        self.age = age

    def run(self):
        print("run")

    def name(self):
        return self.__name

    def __str__(self):
        return f'{self.__name} {self.age}'

player1 = PlayerCharacter("Chav", 20)
# print(player1.__name)
# print(player1.name())
# print(player1.age)

print(player1)