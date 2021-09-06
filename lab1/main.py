# import matplotlib as plt
import numpy as np


def randomArray(array, length):
    for i in range(length):
        array.append(np.random.rand())
    return array


def main():
    array = []
    print(randomArray(array, 10))


main()
