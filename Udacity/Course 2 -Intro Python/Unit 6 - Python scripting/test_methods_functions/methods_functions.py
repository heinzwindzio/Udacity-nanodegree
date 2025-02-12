
#object
class Dog:
    #method
    def __init__(self, name):
        self.name = name

    #method
    def bark(self):
        print(f"{self.name} barks!")

my_dog = Dog("Buddy")
my_dog.bark()


#method
def add_numbers(a, b):
 return a + b

print('Here''s 2+3:', add_numbers(2, 3))
