class Human():
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def get_named(self):
        long_name = (self.name + str(self.age) + self.color)
        return long_name


human = Human('fanzhihcoa', 20, 'blue')
print(human.get_named())


class Woman(Human):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)


