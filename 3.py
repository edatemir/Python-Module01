class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, height):
        self.height += 0.8

    def age(self, age):
        self.age += 1

    def show(self):
        print(
            f"{self.name}: "
            f"{self.height}cm, "
            f"{self.age} days old"
            )

if 