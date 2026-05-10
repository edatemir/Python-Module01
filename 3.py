class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 0.8

    def age_up(self):
        self.age += 1

    def show(self):
        print(
            f"{self.name}: "
            f"{round(self.height, 1)}cm, "
            f"{self.age} days old"
            )

if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    start_h = rose.height
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
       print(f"=== Day {day} ===")
       rose.grow()
       rose.age_up()
       rose.show()
    growth = rose.height - start_h
    print(f"Growth this week: {round(growth, 1)}cm")