import numpy as np
import cv2

def gray2rgb(gray_processed, pallet, backend='np'):
    
    if backend == 'tf':
        
        import tensorflow as tf
        
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
            
    elif backend == 'np':
        gray = gray_processed
        w, h = gray.shape
        gray = gray[:,:,np.newaxis]
        gray = cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
        
        unq = np.unique(gray)
        rgb = np.zeros((w,h,3))
        
        for i in range(len(unq)):
            clr = pallet[:,unq[i],:]
            rgb = np.where(gray!=unq[i], rgb, np.add(rgb,clr))
            
    return rgb
