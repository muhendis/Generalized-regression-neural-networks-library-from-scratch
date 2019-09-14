# Generalized Regression Neural Networks (GRNN)

   Generalized regression neural network (GRNN) is a variation to radial basis neural networks. GRNN was suggested by D.F. Specht in 1991.GRNN can be used for regression, prediction, and classification. GRNN can also be a good solution for online dynamical systems. GRNN represents an improved technique in the neural networks based on the nonparametric regression. The idea is that every training sample will represent a mean to a radial basis neuron.[1]

   GRNN is a feed forward ANN model consisting of four layers: input layer, pattern layer, summation layer and output layer. Unlike backpropagation ANNs, iterative training is not required. Each layer in the structure consists of different numbers of neurons and the layers are connected to the next layer in turn. [2] 

   * In the first layer, **the input layer**, the number of neurons is equal to the number of properties of the data.[3]
   
   * In **the pattern layer**, the number of neurons is equal to the number of data in the training set. In the neurons in this layer, the distances between the training data and the test data are calculated and the results are passed through the radial based function (activation function) with the σ value and the weight values are obtained.[3]
   
   * **The summation layer** has two subparts one is Numerator part and another one is Denominator part. Numerator part contains summation of the multiplication of training output data and  activation function output (weight values). Denominator is the summation of all weight values. This layer feeds both the Numerator & Denominator to the next output layer.[3]
   
   * **The output layer** contains one neuron which calculate the output by dividing the numerator part of the Summation layer by the denominator part.[3]

![Algorithm-Graph](https://github.com/muhendis/Design-of-Generalized-regression-neural-networks-library-from-scratch/blob/master/img/algo-graph.jpg)

                                                   
                                                   The general structure of GRNN [3]
                                                   
## Training Procedure

Training procedure is to find out the optimum value of σ. Best practice is that find the position where the MSE (Mean Squared Error) is minimum. First divide the whole training sample into two parts. Training sample and test sample. Apply GRNN on the test data based on training data and find out the MSE for different σ. Now find the minimum MSE and corresponding value of σ. [3]
 
## Advantages of GRNN 

   * The main advantage of GRNN is to speed up the training process which helps the network to be trained faster.

   * The network is able to learning from the training data by “1-pass” training in a fraction of the time it takes to train standard feed forward networks.

   * The spread, Sigma (σ), is the only free parameter in the network, which often can be identified by the V-fold or Split-Sample cross validation.

   * Unlike standard feed forward networks, GRNN estimation is always able to converge to a global solution and won’t be trapped by a local minimum. [3]

## Disadvantages of GRNN 

   * Its size can be huge, which would make it computationally expensive. [4]
   
## Example
   
![Example](https://github.com/muhendis/Design-of-Generalized-regression-neural-networks-library-from-scratch/blob/master/img/example.PNG)

                                                  

### Resources

[1] https://www.wikizeroo.org/index.php?q=aHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvR2VuZXJhbF9yZWdyZXNzaW9uX25ldXJhbF9uZXR3b3Jr

[2] https://www.journalagent.com/pajes/pdfs/PAJES_24_5_857_863.pdf

[3] https://easyneuralnetwork.blogspot.com/2013/07/grnn-generalized-regression-neural.html
