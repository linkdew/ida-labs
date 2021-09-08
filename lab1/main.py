import matplotlib.pyplot as plt
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
        vector.append(np.random.uniform(0, 1 - norm_var))
        norm_var += vector[i]
    vector.append(1 - norm_var)
    np.random.shuffle(vector)
    return vector


def main():
    models_count = None
    metrics_count = None

    print("Enter number of alternative models (n): ", end=" ")
    models_count = setIntValue(models_count)

    print("Enter number of quality metrics (m): ", end=" ")
    metrics_count = setIntValue(metrics_count)

    print(models_count, metrics_count)
    metrics = []
    for i in range(metrics_count):
        metrics.append("metric " + str(i + 1))

    vec = generateNormalizedWeightsVector(metrics_count)
    dots = generateNormalizedWeightsVector(metrics_count)
    print(vec, sum(vec))

    x = np.arange(metrics_count)
    plt.plot(x, dots, 'b', color = "purple")
    plt.plot(x, dots, 'o', color = "purple")

    plt.grid(True)
    plt.bar(metrics, vec, width = 0.25, color = "orange", edgecolor = "grey", alpha = 0.7)
    plt.ylim(0, 1)
    plt.xlim(-0.25, len(metrics))
    plt.show()


main()

