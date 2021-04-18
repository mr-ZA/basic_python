from matplotlib import pyplot as plt
from collections import Counter

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias = variance[::-1]
total_error = [x + y for x, y in zip(variance, bias)]
xs = range(len(bias))
plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias, 'b-.', label='bias')
plt.plot(xs, total_error, 'r:', label='error')
plt.legend(loc=9)
plt.title('оглавление')
plt.show()
