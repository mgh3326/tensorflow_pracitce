import tensorflow as tf

mathScore = [85, 99, 84, 97, 92]
englishScore = [59, 80, 84, 68, 77]
a = tf.placeholder(dtype=tf.float32)
b = tf.placeholder(dtype=tf.float32)
y = (a + b) / 2
sess = tf.Session()

print(sess.run(y, feed_dict={a: mathScore, b: englishScore}))
