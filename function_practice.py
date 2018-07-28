import tensorflow as tf  # 텐서플로우 라이브러리 불러오기

a = tf.constant(17)
b = tf.constant(5)
# 덧셈 함수 사용하기
c = tf.add(a, 5)
sess = tf.Session()
sess.run(c)
# 뺄셈 함수 사용하기
c = tf.subtract(a, 5)
sess.run(c)
# 곱셈 함수 사용하기
c = tf.multiply(a, 5)
sess.run(c)
# 나눗셈 함수 사용하기
c = tf.truediv(a, 5)
sess.run(c)
# 나머지 함수 사용하기
c = tf.mod(a, 5)
sess.run(c)
# 절댓값 함수 사용하기
c = tf.abs(-a)

print(sess.run(c))
