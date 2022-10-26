import numpy as np

class Perceptron():
    def __init__(self, inputs, bias=1.0):
        self.weights = (np.random.rand(inputs + 1) * 2) - 1
        self.bias = bias

    def setWeights(self, initial_weights):
        self.weights = np.array(initial_weights)

    def sigmoid(self, sum):
        return 1/(1 + np.exp(-sum))

    def run(self, x):
        sum = np.dot(np.append(x, self.bias), self.weights)
        return self.sigmoid(sum)


if __name__ == '__main__':
    model = Perceptron(2)
    model.setWeights([10, 10, -15])

    print("Gate:")
    print ("0 0 = {0:.10f}".format(model.run([0,0])))
    print ("0 1 = {0:.10f}".format(model.run([0,1])))
    print ("1 0 = {0:.10f}".format(model.run([1,0])))
    print ("1 1 = {0:.10f}".format(model.run([1,1])))