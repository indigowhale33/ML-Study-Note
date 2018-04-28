# Reference from https://www.tensorflow.org and Deep Learning by Ian Goodfellow

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

# softmax function
softmax = tf.exp(logits) / tf.reduce_sum(tf.exp(logits), axis)
