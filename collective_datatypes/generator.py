def count_down(number):
    while number > 0:
        yield number
        number -= 1


input_number = int(input("Enter a number: "))
values = count_down(input_number)
for value in values:
    print(value)

l = [x * x for x in range(10000000000000000)]
print(l[0])

g = (x * x for x in range(10000000000000000))
print(next(g))
