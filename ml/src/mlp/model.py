import numpy as np
from package.utils import sigmoid, derivative_sigmoid


class MLP(object):
    def __init__(self, d_in=2, d_h=3, d_out=2):
        self.d_in = d_in 
        self.d_h = d_h
        self.d_out = d_out

        # weight and bias initialization
        self.wh = np.random.uniform(size=(d_in, d_h))
        self.bh = np.random.uniform(size=(1, d_h))
        self.wout = np.random.uniform(size=(d_h, d_out))
        self.bout = np.random.uniform(size=(1, d_out))

    def forward(self, X, y):

        h = sigmoid(X.dot(self.wh) + self.bh)
        y_pred = sigmoid(h.dot(self.wout) + self.bout)
        loss = (y_pred - y).sum()
        
        return loss, y_pred, h

    def backward(self, X, y, y_pred, h, learning_rate=0.1):

        # Backpropagation to compute gradients
        grad_y_pred = (y - y_pred) * derivative_sigmoid(y_pred)
        grad_wout = h.T.dot(grad_y_pred)
        grad_bout = np.sum(grad_y_pred, axis=0, keepdims=True)
        grad_h = grad_y_pred.dot(self.wout.T) * derivative_sigmoid(h)
        grad_wh = X.T.dot(grad_h)
        grad_bh = np.sum(grad_h, axis=0, keepdims=True)

        # Update weights and biases
        # hint:
        # you should update wout, bout, wh, bh with 
        # grad_wout, grad_bout, grad_wh, grad_bh multiplied by learning_rate
        self.wout += grad_wout * learning_rate
        self.bout += grad_bout * learning_rate
        self.wh += grad_wh * learning_rate
        self.bh += grad_bh * learning_rate
      
