# create the list of fruits
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
fruits1 = ["apple", "banana", "orange", "grape", "kiwi"]


print(fruits[0])
print(fruits[-0])
print(len(fruits))

for fruit in fruits:
    print(fruit)

# take the list as input from the user
# list  = eval(input("Enter the list:"))
# print(list)
# print(type(list))
    
# comparing the list
print(fruits == fruits1)
print(id(fruits))
print(id(fruits1))