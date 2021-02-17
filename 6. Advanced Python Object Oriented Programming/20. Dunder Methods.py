class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name':'chavi',
            'has_pets':False

        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return "Unsa!?"

    # def __del__(self):
    #     return('deleted!')

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('Red', 0)
print(action_figure.__str__())
print(str(action_figure))
print()
print(len(action_figure))
print(action_figure.__len__())
print(action_figure())
# del action_figure
print(action_figure['name'])
print(action_figure['has_pets'])