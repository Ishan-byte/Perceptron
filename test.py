import numpy as np

weights = ([10, 10, -15])
inputs = ([0, 0, 1])

sum = np.dot(weights, inputs)

result = 1/(1 + np.exp(-sum))

print("{0:.10f}".format(result))
