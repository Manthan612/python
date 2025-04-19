class Car():
    def set_details(self, brand, colour):
        self.brand = brand
        self.colour = colour
    def show_details(self):        
        print(f'This is {self.brand} With {self.colour} Colour')

c1 = Car()
c2 = Car()

c1.set_details('Lamborghini','Cyan')
c2.set_details('BMW','Black')
c1.show_details()
c2.show_details()
