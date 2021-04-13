import tensorflow as tf
import numpy as np

def gray2rgb(gray_processed, pallet):
    
    pallet = tf.convert_to_tensor(pallet)
    w, h = gray_processed.shape
    gray = gray_processed[:,:,np.newaxis]
    gray = tf.image.grayscale_to_rgb((tf.convert_to_tensor(gray)))
    gray = tf.cast(gray, 'int32')
    unq = np.unique(gray_processed)
    rgb = tf.zeros_like(gray, dtype=tf.float64)
    
    for i in range(len(unq)):
        clr = pallet[:, int(unq[i]), :]
        clr = tf.expand_dims(clr, 0)
        rgb = tf.where(tf.not_equal(gray,unq[i]), rgb, tf.add(rgb,clr))
        
    if tf.executing_eagerly()==False:
        sess = tf.compat.v1.Session()
        rgb = sess.run(rgb)
    else:
        rgb = rgb.numpy()
    return rgb

