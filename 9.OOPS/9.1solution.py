class Characters():
    def __init__(self, name, type, helth, power ):
        self.name = name
        self.type = type
        self.helth = helth
        self.power = power
    def attack(self):
        print(f'{self.name} perform {self.type} attacks with power: {self.power}'.title())


p1 = Characters('Barbarians','Ground', 70, 25) 
p2 = Characters('Archers','Ground & Air', 60, 30)
p3 = Characters('Goblins','Ground', 40, 40)
p4 = Characters('Giant','Ground', 150, 50)
p5 = Characters('Balloons', 'Air', 120, 80)
p6 = Characters('Wizard','Ground & Air', 90, 60)

p1.attack()
p2.attack()
p3.attack()
p4.attack()
p5.attack()
p6.attack()