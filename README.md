# ML-Study-Note

To satisfy my lack of knowledge but full of passion..

Reference: https://www.tensorflow.org and Deep Learning by Ian Goodfellow


## Deep Feedforward Networks

#### Why not Mean Squared Error for the cost function?:

Suppose we have a linear model with ![theta](https://latex.codecogs.com/gif.latex?%5Ctheta) consisting of w and b,
![linear model eq](https://latex.codecogs.com/gif.latex?f%28x%3Bw%2Cb%29%3Dx%5E%7BT%7Dw&plus;b).

The MSE loss function would be like:

![first equation](https://latex.codecogs.com/gif.latex?J%28%5Ctheta%20%29%20%3D%20%5Csum_%7Bx%20%5Cin%20X%7D%20%7B%28f*%28x%29%20-%20f%28x%3B%5Ctheta%29%29%5E2%29%7D)

Then a feedforward network with one hidden layer containing a vector of hidden units **h** would be like **h**= ![hidden layer1](https://latex.codecogs.com/gif.latex?f%5E%7B%281%29%7D%28x%3BW%2Cc%29) and y=![output layer](https://latex.codecogs.com/gif.latex?f%5E%7B%282%29%7D%28h%3Bw%2Cb%29).

The complete model is ![exModel](https://latex.codecogs.com/gif.latex?f%28x%3BW%2Cc%2Cw%2Cb%29%3Df%5E%7B%282%29%7D%28f%5E%7B%281%29%7D%28x%29%29)

But if ![f^1](https://latex.codecogs.com/gif.latex?f%5E%7B%281%29%7D) is linear, the feedforward network as a whole would be a linear. Suppose ![f1eq](https://latex.codecogs.com/gif.latex?f%5E%7B%281%29%7D%3DW%5ETx) and ![f2eq](https://latex.codecogs.com/gif.latex?f%5E%7B%282%29%7D%3Dh%5ETw), then ![reseq1](https://latex.codecogs.com/gif.latex?f%28x%29%3Dw%5ETW%5ETx) = ![reseq2](https://latex.codecogs.com/gif.latex?x%5Etw%27).

To avoid this, modern neural networks use **sigmoid**, **rectified linear unit** or **ReLU** or any other activation functions.

For instance, with ReLU which is defined by ![ReLU](https://latex.codecogs.com/gif.latex?g%28z%29%3Dmax%7B%280%2Cz%29%7D), we can write the above neural network as ![nnwithReLU](https://latex.codecogs.com/gif.latex?f%28x%3BW%2Cc%2Cw%2Cb%29%3Dw%5ETmax%7B%5C%7B0%2CW%5ETx&plus;c%5C%7D&plus;b%7D), and be able to solve nonlinear problems.

#### Why log-likelihood objective functions are very recommended to use than other objective functions for Softmax function?

First, softmax function is given by:

![softmaxeq](https://latex.codecogs.com/gif.latex?softmax%28z%29_%7Bi%7D%3D%5Cfrac%7Bexp%28z_i%29%7D%7B%5Csum_j%20exp%28z_j%29%7D)

Objective functions without logarithm does not cancel out the exponential of the softmax function, and highly likely to face the gradient to vanish at the extreme positive or negative.

The Sigmoid function also has this problem as
