import numpy as np
import random
import math

# Each row is a training example, each column is a feature  [X1, X2, X3]
x=np.array(([0,0,1],[0,1,1],[1,0,1],[1,1,1]), dtype=float)
y=np.array(([0],[1],[1],[0]), dtype=float)

# Define useful functions    

# Activation function
def sigmoid(t):
    return 1/(1+np.exp(-t))

# Derivative of sigmoid
def sigmoid_derivative(p):
    return p * (1 - p)



class NeuralNetwork:
  def __init__(self, x,y): # первоначальная установка
    self.input = x
    self.Weights = np.random.rand(self.input.shape[1],4)
    self.Weights2 = np.random.rand(4,1)

    self.y=y
    self.output = np.zeros(y.shape)

  def feedforward(self):
    self.layer1 = sigmoid(np.dot(self.input, self.Weights))
    self.output = sigmoid(np.dot(self.layer1, self.Weights2))
    return self.output

  def backprop (self):  #метод обратного распространения
    d_weights2= np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))

    d_weights1=np.dot(self.input.T, (np.dot(2*(self.y-self.output) * sigmoid_derivative(self.output), self.Weights2.T)* sigmoid_derivative(self.layer1)))

    self.Weights+=d_weights1
    self.Weights2+=d_weights2
  
  def train(self, x ,y):
    self.output=self.feedforward()
    self.backprop()


NN = NeuralNetwork(x,y)
for i in range(1500): # trains the NN 1,000 times
    if i % 100 ==0: 
        print ("for iteration # " + str(i) + "\n")
        print ("Input : \n" + str(x))
        print ("Actual Output: \n" + str(y))
        print ("Predicted Output: \n" + str(NN.feedforward()))
        print ("Loss: \n" + str(np.mean(np.square(y - NN.feedforward())))) # mean sum squared loss
        print ("\n")
  
    NN.train(x, y)



