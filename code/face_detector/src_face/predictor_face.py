import os
import sys
import cv2
import time
import logging
import json
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import glob
import tqdm
import os
#path=os.path.join(os.getcwd())
#os.chdir(path)
#print(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from src_face.trainer_face import model
from src_face.__init__ import *
import platform

config = tf.ConfigProto()
config.gpu_options.allow_growth = True


index_faces = {v: k for k, v in ITEM_MAP.items()}


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


def inference(sess, gray_img_input,X,y_conv,keep_prob):
    
    img = gray_img_input.reshape(1, 48, 48, 1).astype(float) / 255
    
    y_c = sess.run(y_conv, feed_dict={X:img, keep_prob:1.0})
    
    y_c = softmax(y_c)
    #print(y_c)
    p = np.argmax(y_c, axis=1)
    score = np.max(y_c)
    return p[0], score
        

def from_cam(sess,X,y_conv,keep_prob):
    
    face_cascade = cv2.CascadeClassifier(config_parser['OPEN_CV']['cascade_classifier_path'])
    cap = cv2.VideoCapture(0)

    font               = cv2.FONT_HERSHEY_SIMPLEX
    fontScale          = 1
    fontColor          = (255,255,255)
    lineType           = 2

    last_trial = -1
    p=-2
    num_faces = {v: 0 for k, v in ITEM_MAP.items()}
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Operations on the frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect the faces, bounding boxes
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # draw the rectangle (bounding-boxes)
        #for (x,y,w,h) in faces:
        if len(faces)!=0:
            (x, y, w, h)=faces[0]
            cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
            bottomLeftCornerOfText = (x + 10, y + h + 10)

            face_img_gray = gray[y:y + h, x:x + w]
            face_img_gray = cv2.resize(face_img_gray, (48, 48))
            p, confidence = inference(sess, face_img_gray,X,y_conv,keep_prob)
            # logger.critical('model inference time: {}'.format(time.time() - s))

            if confidence > 0.9:
                if last_trial == p:
                    cv2.putText(frame, str(index_faces[p]) + f' E Confidence: {round(confidence, 2)}',
                                bottomLeftCornerOfText,
                                font,
                                fontScale,
                                fontColor,
                                lineType)

                    print(p, 'logined')
                    last_trial = p
                    num_faces[p] += 1
                    if max(num_faces.values()) > 30:
                        id = max(num_faces, key=num_faces.get)
                        name = index_faces[id]
                        print((name + ' successfully logined'))
                        break
                else:
                    cv2.putText(frame, f'new t Confidence: {round(confidence, 2)}',
                                bottomLeftCornerOfText,
                                font,
                                fontScale,
                                fontColor,
                                lineType)
                    last_trial = p
            else:
                cv2.putText(frame, str(index_faces[p]) + f'not E Confidence: {round(confidence, 2)}',
                            bottomLeftCornerOfText,
                            font,
                            fontScale,
                            fontColor,
                            lineType)
                last_trial = -1
                # break


        else:
            print('face not detected')
        #cv2.imshow('gray-scale', gray)
        cv2.imshow('faces', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            name = -100
            break
    cap.release()
    cv2.destroyAllWindows()

    return name

def mk_final_pred_face():
    CHECKPOINT_SAVE_PATH = os.path.join(os.path.dirname(__file__), os.pardir, 'model_checkpoints')
    tf.reset_default_graph()
    index_emo = {v: k for k, v in EMOTION_MAP.items()}
    X = tf.placeholder(
        tf.float32, shape=[None, 48, 48, 1]
    )

    keep_prob = tf.placeholder(tf.float32)
    y_conv = model(X, keep_prob)
    with tf.Session(config=config) as sess:
        saver = tf.train.Saver()
        saver.restore(sess, os.path.join(CHECKPOINT_SAVE_PATH, 'model.ckpt'))
        name_user = from_cam(sess,X,y_conv,keep_prob)
        print(name_user)
    return name_user




