import matplotlib as plt
import random
import numpy as np


def sum(array):
    result = 0
    for i in range(len(array)):
        result += array[i]
    return result


def setIntValue(value):
    while not isinstance(value, int):
        try:
            value = int(input())
        except ValueError:
            print("Enter integer value: ", end=" ")
        else:
            # print(value)
            break
    return value


def generateNormalizedWeightsVector(dim):
    vector = []
    norm_var = 0
    for i in range(dim - 1):
        vector.append(random.uniform(0, 1 - norm_var))
        norm_var += vector[i]
    vector.append(1 - norm_var)
    return vector


def main():
    models_count = None
    metrics_count = None

    print("Enter number of alternative models (n): ", end=" ")
    models_count = setIntValue(models_count)

    print("Enter number of quality metrics (m): ", end=" ")
    metrics_count = setIntValue(metrics_count)

    print(models_count, metrics_count)

    vec = generateNormalizedWeightsVector(metrics_count)
    print(vec, sum(vec))


main()
