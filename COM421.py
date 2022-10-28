class cat:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        self.weight += 1
    def walk(self):
        if self.weight <= 1:
            print("Error! Cat weight too low, may starve.")
        else:
            self.weight -= 1

cat1 = cat("Binnie", 4, 4)
cat2 = cat("Clyde", 1, 2)
cat3 = cat("Old Tom", 10, 6)

cat1.eat()
cat2.eat()
cat3.eat()

cat1.walk()
cat2.walk()
cat3.walk()

print(cat1.weight)
print(cat2.weight)
print(cat2.weight)
