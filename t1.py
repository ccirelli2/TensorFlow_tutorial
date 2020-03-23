# DOCUMENTATION
'''
    Purpose:    DataCamp tutorial for Tensorflow
    Url:        https://www.datacamp.com/community/tutorials/tensorflow-tutorial
'''


# IMPORT LIBRARY
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Initialize two constants
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

# Initialize Interactive Session
'Necessary to generate calculation'
sess = tf.Session()

# Multiply 
result = tf.multiply(x1,x2)

# Print Result
print(sess.run(result))

sess.close()
