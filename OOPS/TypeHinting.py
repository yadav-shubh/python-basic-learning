import logging

logging.basicConfig(filename="TypeHinting.log", level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - '
                                                                           '%(message)s')


def sumOfList(values: list) -> float:
    logging.debug(f"Sum of list: {sum(values)}")
    return sum(values)


values_list = [1, 2, 3, 4]
# values_list = 1
print(sumOfList(values_list))
