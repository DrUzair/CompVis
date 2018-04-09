import tensorflow as tf
tf.reset_default_graph()
# Create some variables.
W1 = tf.get_variable("W1", [4, 4, 3, 8], initializer=tf.contrib.layers.xavier_initializer(seed=0))
W2 = tf.get_variable("W2", [2, 2, 8, 16], initializer=tf.contrib.layers.xavier_initializer(seed=0))

saver = tf.train.Saver({"W1": W1, "W2": W2})

# Use the saver object normally after that.
with tf.Session() as sess:
  # Initialize v1 since the saver will not.
  W1.initializer.run()
  saver.restore(sess, "/tmp/model.ckpt")

  print("W1 : %s" % W1.eval())
  print("W2 : %s" % W2.eval())
