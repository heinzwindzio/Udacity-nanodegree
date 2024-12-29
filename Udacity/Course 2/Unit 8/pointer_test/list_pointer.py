def dog_died(pets):
	pets.pop(0)

my_dogs = ['Carson', 'Bonzo']

print("Here are my dogs: ", my_dogs)

dog_died(my_dogs)

#notice how I still retain the pointer to the list, which has been modified
print("Here are my current dogs: ", my_dogs)