import numpy as np

def sum_squares_error(y, t):
  return 0.5 * np.sum((y - t) ** 2)

def cross_entropy_error(y, t):
  if y.ndim == 1:
    t = t.reshape(1, t.size)
    y = y.reshape(1, y.size)

  batch_size = y.shape[0]
  delta = 1e-7 # log값이 마이너스가 되지 않게 하기 위함
  return -np.sum(t * np.log(y + delta)) / batch_size


def cross_entropy_onehot_error(y, t):
  if y.ndim == 1:
    t = t.reshape(1, t.size)
    y = y.reshape(1, y.size)

  batch_size = y.shape[0]
  delta = 1e-7 # log값이 마이너스가 되지 않게 하기 위함
  return -np.sum(np.log(y[np.arange(batch_size), t] + delta)) / batch_size
  # y[np.arange(batch_size), t] + delta) : 
