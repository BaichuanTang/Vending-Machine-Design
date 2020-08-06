import os
import sys
import cv2
import time
import logging
import json
#import tensorflow as tf
import numpy as np
import glob
import tqdm
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import warnings
warnings.filterwarnings("ignore")
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from src.trainer import model
from src.__init__ import *


config = tf.ConfigProto()
config.gpu_options.allow_growth = True


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


def inference(sess, gray_img_input,X,y_conv,keep_prob):
    
    img = gray_img_input.reshape(-1, 48, 48, 3).astype(float) / 255
    
    y_c = sess.run(y_conv, feed_dict={X:img, keep_prob:1.0})
    
    y_c = softmax(y_c)
    p = np.argmax(y_c, axis=1)
    score = np.max(y_c)
    return p[0], score
        

def from_cam(sess,X,y_conv,keep_prob):
    index_emo = {v: k for k, v in EMOTION_MAP.items()}
    index_item = {v: k for k, v in ITEM_MAP.items()}
    #face_cascade = cv2.CascadeClassifier(config_parser['OPEN_CV']['cascade_classifier_path'])

    cap = cv2.VideoCapture(0)

    font               = cv2.FONT_HERSHEY_SIMPLEX
    fontScale          = 1
    fontColor          = (255,255,255)
    lineType           = 2
    time_succ = 0
    sum_item = {k: 0 for k, v in ITEM_MAP.items()}
    suc_tag=0
    last_trial = -1
    cv2.startWindowThread()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        gray =frame
        w,h=(20,20)
        x,y=(10,10)
        bottomLeftCornerOfText = (30,30)

        face_img_gray = gray#[y:y+h, x:x+w]
        face_img_gray = cv2.resize(face_img_gray, (48, 48))
        s = time.time()
        p, confidence = inference(sess, face_img_gray,X,y_conv,keep_prob)
        if confidence > 0.999 and last_trial==p:
            time_succ+=1
            cv2.putText(frame,f'Moniter--Confidence: {round(confidence, 2)}'+'\ttimes: '+str(time_succ),
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)
        else:
            cv2.putText(frame,'Moniter--NEUTRAL',
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)
            #if last_trial!=p :
                #print('time succ:',time_succ)
            if time_succ > 25 and time_succ<50:
                print('留给崔凡，' + '商品' + str(index_item[p]))
                sum_item[index_item[p]] = sum_item[index_item[p]] + 1
                time.sleep(3)


            time_succ = 0
        # Display the resulting frame
        cv2.imshow('detect-item', gray)
        last_trial=p
        #cv2.imshow('faces', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('detect-item', cv2.WND_PROP_AUTOSIZE) < 1:
            cap.release()
            cv2.destroyAllWindows()
            break
    cap.release()
    cv2.destroyAllWindows()

    return sum_item

def mk_final_pred_item():
    CHECKPOINT_SAVE_PATH = os.path.join(os.path.dirname(__file__), os.pardir, 'model_checkpoints')
    tf.reset_default_graph()
    # used to map the output from the prediction to the emotion class
    X = tf.placeholder(
        tf.float32, shape=[None, 48, 48, 3]
    )
    keep_prob = tf.placeholder(tf.float32)
    y_conv = model(X, keep_prob)
    with tf.Session(config=config) as sess:
        saver = tf.train.Saver()
        saver.restore(sess, os.path.join(CHECKPOINT_SAVE_PATH, 'model.ckpt'))
        name_item = from_cam(sess,X,y_conv,keep_prob)
        print(name_item)
    return name_item

