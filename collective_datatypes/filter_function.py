from functools import reduce

number_list = [i for i in range(10)]
print(number_list)

evens = list(filter(lambda x: x % 2 == 0, number_list))
odds = list(filter(lambda x: x % 2 != 0, number_list))
print(evens)
print(odds)

sq_evens = list(map(lambda x: x ** 2, evens))
print(sq_evens)
reduced_sq_evens = reduce(lambda x, y: x + y, sq_evens)
print(reduced_sq_evens)

l = [10, 20, 30, 40, 50]
result = reduce(lambda x, y: x + y, l)
print(result)  # 150
