print("Hello_World")

list1 = [3,2,8,4,5,10,11]

length = len(list1)

print("length of list is: ", length)

# Method 1 - Non OOP
total = 0
for item in list1:
    total += item

print("The sum is: ", total)

# Method 2 - Abstraction principle of OOP
print("The sum of list is: ", sum(list1))


class summer_fruits:
    print("Only available from june to august")

class mango(summer_fruit):
    print("Color is Yellow")

class water_melon(summer_fruits):
    print("Color is Red")



