class PlayerCharacter:
    membership = True # class object  attribute
    def __init__(self, name, age):
        self.name = name # attributes of the instantiation(?)
        self.age = age

    # class object method 
    @classmethod # used to call on this method without instantiation
    def adding_things(cls, num1, num2): # cls is for the class, same with self
        return num1 + num2
    
    @classmethod
    def create_class_with_age(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    def __str__(self):
        return str(f"Player Character with name: {self.name} and age: {self.age}.")


    @staticmethod # you don't access to the class; we don't care of the class state
    def adding_things2(num1, num2):
        return num1 + num2

# player3 = PlayerCharacter.create_class_with_age(3,1)
# print(player3)

#print(PlayerCharacter.adding_things(1,2))

print(PlayerCharacter.adding_things2(2,3))