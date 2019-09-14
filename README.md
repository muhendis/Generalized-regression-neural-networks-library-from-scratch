# Generalized Regression Neural Networks (GRNN)

GRNN is a feed forward ANN model consisting of four layers: input layer, pattern layer, summation layer and output layer. Unlike backpropagation ANNs, iterative training is not required. Each layer in the structure consists of different numbers of neurons and the layers are connected to the next layer in turn [1]. 

   * In the first layer, **the input layer**, the number of neurons is equal to the number of properties of the data.
   
   * In **the pattern layer**, the number of neurons is equal to the number of data in the training set. In the neurons in this layer, the distances between the training data and the test data are calculated and the results are passed through the radial based function with the σ value and the weight values are obtained.
   
   * **The summation layer** has two subparts one is Numerator part and another one is Denominator part. Numerator part contains summation of the multiplication of training output data and  activation function. Denominator is the summation of all activation function. This layer feeds both the Numerator & Denominator to the next output layer.

   
   * **The output layer** contains one neuron which calculate the output by dividing the numerator part of the Summation layer by the denominator part.

