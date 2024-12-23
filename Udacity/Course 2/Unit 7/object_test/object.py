class Shirt:
    def __init__(self, shirt_color, shirt_size):
        self.color = shirt_color
        self.size = shirt_size

    def change_color(self, new_color):
        self.color = new_color

    def shirt_combine(self, number):
        tag = ''
        for x in range(0, number):
            tag += self.color + ' ' + self.size + '\n'
        return tag

#instantiate the objects
blue_shirt = Shirt('red', 'medium')
green_shirt = Shirt('green', 'medium')
yellow_shirt = Shirt('yellow', 'large')

blue_shirt.change_color('blue')

combined = blue_shirt.shirt_combine(3)

shirt_collection = []
shirt_collection.append(blue_shirt)
shirt_collection.append(green_shirt)
shirt_collection.append(yellow_shirt)

for shirt in shirt_collection:
    print(shirt.color + ':', end='')


        