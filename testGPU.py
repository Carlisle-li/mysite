import tensorflow as tf
norm = tf.random_normal([2, 3], mean=-1, stddev=4)

c = tf.constant([[1, 2],
                 [3, 4],
                 [5, 6]])
shuff = tf.random_shuffle(c)

sess = tf.Session()
print(sess.run(norm))
print(sess.run(c))
print(sess.run(shuff))