import tensorflow as tf

a = tf.Variable(5)
b = tf.Variable(3)
c = tf.multiply(a, b)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
sess.run(c)
print(sess.run(c))
a = tf.Variable(10)
c = tf.multiply(a, b)
init = tf.global_variables_initializer()
sess.run(init)
sess.run(c)
print(sess.run(c))

