import tensorflow as tf
import time

print('TensorFlow version: ', tf.__version__)

start_time = time.time()

print(tf.reduce_sum(tf.random.normal([1000, 1000])))

print(f"{(time.time() - start_time)} Compilation Time")
