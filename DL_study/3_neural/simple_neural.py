import numpy as np

class activate_function():
  def step_function(x):
    y = x > 0
    return y.astype(np.int)

  def sigmoid(x):
    return 1 / (1 + np.exp(-x))

  def sigmoid_grad(self, x):
      return (1.0 - self.sigmoid(x)) * self.sigmoid(x)
    
  def relu(x):
    return np.maximum(0, x)

  def identity_function(x):
    return x
    
  def softmax(x):
    c = np.max(x)
    exp_a = np.exp(x - c) # 오버플로 방지
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

class simple_neural():
  def __init__(self):
    self.W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    self.B1 = np.array([0.1, 0.2, 0.3])

    self.W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    self.B2 = np.array([0.1, 0.2])

    self.W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
    self.B3 = np.array([0.1, 0.2])

  def forward(self, X):
    W1, W2, W3 = self.W1, self.W2, self.W3
    B1, B2, B3 = self.B1, self.B2, self.B3

    A1 = np.dot(X, W1) + B1
    Z1 = activate_function.sigmoid(A1)
    A2 = np.dot(Z1, W2) + B2
    Z2 = activate_function.sigmoid(A2)
    A3 = np.dot(Z2, W3) + B3
    Y = activate_function.identity_function(A3)
    return Y

  