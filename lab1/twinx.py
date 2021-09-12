import numpy as np
import matplotlib.pyplot as plt

# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t) * 2
data2 = np.sin(2 * np.pi * t)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

    #plt.plot(x, dots, 'b', color = "")
    #plt.plot(x, dots, 'o', color = "purple")

    #
    #plt.bar(metrics, vec, width = 0.25, color = "orange", edgecolor = "grey", alpha = 0.7)
    #plt.ylim(0, 1)
    #plt.xlim(-0.25, len(metrics))
    #plt.show()
# Create some mock data