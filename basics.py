numbers = [1, 2, 3, 4, 5, 6]

first = 1

π = 3.141592653589793
print(π)

help("keywords")

int(10.78)

int("2")

## not posible, error
##int(complex(1,2))

10.5.is_integer()

print((100).bit_length())
print(len("happy pythoning!"))

print(" ".join(["happy", "python", "learning"]))
print("real python".upper(), "LEARN".lower())

##formatting
name ="John Doe"
age = 23
print(f"My name is {name} and I'm {age} years old")

##slicing
welcome ="Welcome to Real Python!"
print(welcome[0:7], welcome[11:22])

## list are mutable sequences in python
mixed_types = ["Hello World", [4, 5, 6,], False]
print(mixed_types)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[5])

new_list = numbers[0:4]
print(new_list)

fruits = ["apples", "grapes", "oranges", "bananas"]
vegetables = ["onions", "spinach", "mushrooms"]
grocery_list = fruits + vegetables
print(grocery_list)
print("Total items to buy", len(grocery_list))

## list.append() takes and object as an argument and adds it to the end the list
vegetables.append("pumpkins")
print(vegetables)

fruits.sort()
print(fruits)

#removing position 5 in numbers list wich value is 6
numbers.pop(5)
print(numbers)

##tuples are similar list but they're immutable sequences
employees = ("Maria", "Luna", 31, "Software Developer"), ("Juan", "Lopez", 22, "Assistant")
print(employees[0])

first_tuple = (1, 2)
second_tuple = (3, 4)
thrid_tuple = first_tuple + second_tuple
print(thrid_tuple)

len(thrid_tuple)




