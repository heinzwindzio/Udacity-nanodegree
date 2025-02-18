print("hey")

x1 = .4
x2 = .6

w1 = 2
w2 = 6
b = -2

p1 = w1 * x1 + w2 * x2 + b

p1_sigmoid = 1 / (1 + 2.71828 ** -p1)


print(p1_sigmoid)
    
w1 = 3
w2 = 5
b = -2.2

p2 = w1 * x1 + w2 * x2 + b


p2_sigmoid = 1 / (1 + 2.71828 ** -p2)
print(p2_sigmoid)


w1 = 5
w2 = 4
b = -3

p3 = w1 * x1 + w2 * x2 + b
p3_sigmoid = 1 / (1 + 2.71828 ** -p3)

print(p3_sigmoid)   
