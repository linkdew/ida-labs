import matplotlib.pyplot as plt
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
    metrics = []

    print("Enter number of alternative models (n): ", end=" ")
    models_count = setIntValue(models_count)

    print("Enter number of quality metrics (m): ", end=" ")
    metrics_count = setIntValue(metrics_count)

    for i in range(metrics_count):
        metrics.append("metric " + str(i + 1))

    barsdata = generateNormalizedWeightsVector(metrics_count)
    x = np.arange(metrics_count)
    dotsmatrix = []
    for _ in range(models_count):
        dotsmatrix.append(generateNormalizedWeightsVector(metrics_count))

    figure, bars = plt.subplots()
    bars.set_ylabel("metrics weights, %")
    plt.ylim(0, 1)
    plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    plt.xlim(-0.25, len(metrics) - 0.15)
    plt.grid(True)
    plt.title("lab plot")

    bars.bar(metrics, barsdata, width=0.25, color="orange", edgecolor="grey", alpha=0.7)
    bars.tick_params(axis='y', labelcolor="purple")

    models = bars.twinx()

    models.set_ylabel("models weights, %")
    colors = ["w", "k", "g", "m", "c", "r"] * 10
    styles = ["8", "^", "v", "*", "s", "D"] * 10
    for i, color, marker in zip(range(models_count), colors, styles):
        models.plot(x, dotsmatrix[i], marker=marker, color=color)
        plt.text(metrics_count - 0.95, dotsmatrix[i][metrics_count - 1], f"model {i + 1}", fontsize=10)

    models.tick_params(axis='y', labelcolor="red")

    figure.tight_layout()
    bars.set_facecolor("grey")
    plt.show()


main()
