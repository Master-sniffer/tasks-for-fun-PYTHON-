from numpy import exp, array, random, dot

class NeuralNetwork:
  def __init__(self): # таким образом мы будем генерить одни и те же числа(измените сид для других чисел)
    random.seed(1)

    # Нейронка состоит из 3 входов и одного выхода. Матрица будет в размере 3X1 с числами от -1 до 1

    self.synaptic_weights=2*random.random((3,1))-1

  
  # Дальше мы пишем sigmoid функцию, которая будет получать значения. Нормализация проходит между 0 и 1
  def __sigmoid(self, x):
    return 1 / (1 + exp(-x))
  
  # Сейчас будет градиент гладкой сигмойд функции
  def __sigmoid_derivative(self, x):
    return x * (1 - x)

  # Мы треним нейронку методом проб и ошибок, добавляя весы каждый размере

  def train (self, training_set_inputs, training_set_outputs, number_of_training_iterations):
    for integration in range (number_of_training_iterations):
      # Пропускаем один нейрон каждый раз
      output=self.think(training_set_inputs)

      # считаем ошибки (что мы ожидаем и что мы получаем)
      error=training_set_inputs- output

      # Умножаем кол-во ошибок на вход (input) и по градиенту функции сигмойд
      # Это означает, что входы, равные 0, не имеют никакой вес
      adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

      # Добавляем вес
      self.synaptic_weights = self.synaptic_weights + adjustment
  

  def think (self, inputs):
    # Пропускаем нейронны по одному
    return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__=="__main__":
  NN = NeuralNetwork() # Создаем нейронку

  print ("random starting synaptics weights")

  # У нас есть тренир набор, который состоит из 3 входных значений и 1 выходного
  training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
  training_set_outputs = array([[0, 1, 1, 0]]).T # Выход

  # Треним нашу нейронку с помощью трениров набора
  # Делаем так 10 000 раз и каждый раз прибавляем небольшое кол-во 
  NN.train(training_set_inputs, training_set_outputs, 10000)

  print ("Новый синапсос после трени")
  print (NN.synaptic_weights)

  # Проверка нейронки с новой ситуацией
  print ("Considering new situation [1, 0, 0] -> ?: ")
  arr = array([1, 0, 0])
  print (NN.think(arr))
  

