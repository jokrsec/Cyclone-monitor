from tensorflow.keras.models import load_model
import numpy as np
from skimage.io import imshow,imread
from matplotlib import pyplot as plt
from skimage.transform import rescale, resize
m=load_model("disaster_classification_pkl.pkl")
# m.summary()
from skimage.io import imshow,imread

def output(arr):
    l=[arr]
    l=np.array(l)
    p=m.predict(l)
    prediction=np.argmax(p[0])
#     print(prediction)
    if prediction==0 and p[0][0]*100>90:
        return("cyclone"+str(p[0][0]*100)+"%")
    elif prediction==1 and p[0][1]*100>90:
        return("Earth quake"+str(p[0][1]*100)+"%")
    elif prediction==2 and p[0][2]*100>90:
        return("Flood"+str(p[0][2]*100)+"%")
    elif prediction==3 and p[0][3]*100>90:
        return("Wild Fire"+str(p[0][3]*100)+"%")
    else:
        return("none You are free from disaster")
    

import numpy as np
import cv2
def process():
    cap = cv2.VideoCapture('My Video.mp4')
    count=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        count+=20
        if(count%200==0):
            k=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            k=cv2.resize(k, (224, 224))
            text=output(k)
            print(text)
            font = 'FONT_HERSHEY_COMPLEX'
            cv2.putText(frame,text,(0,60), 4,1.7,(255,255,255),4,cv2.LINE_AA)
            (flag, encodedImage) = cv2.imencode(".jpg",frame)
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

    cap.release()
    cv2.destroyAllWindows()



def heatmap():
    cap = cv2.VideoCapture('My Video.mp4')
    count=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        count+=20
        if(count%200==0):
            x= imread(frame, plugin='matplotlib')
            x=np.array(x)
            x=resize(x,(224,224))
            x=x.reshape(1,224,224,3)
#####################################
            with tf.GradientTape() as tape:
                last_conv_layer = model.get_layer('conv5_block3_out')
                iterate = tf.keras.models.Model([model.inputs], [model.output, last_conv_layer.output])
                model_out, last_conv_layer = iterate(x)
                class_out = model_out[:, np.argmax(model_out[0])]
                grads = tape.gradient(class_out, last_conv_layer)
                pooled_grads = K.mean(grads, axis=(0, 1, 2))
            heatmap = tf.reduce_mean(tf.multiply(pooled_grads, last_conv_layer), axis=-1)
            heatmap = np.maximum(heatmap, 0)
            heatmap /= np.max(heatmap)
            heatmap = heatmap.reshape((7, 7))
            heat=heatmap
#for reading any new image
            img= imread(frame, plugin='matplotlib')
            INTENSITY = 0.5
            heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
            heatmap = cv2.applyColorMap(np.uint8(255*heatmap), cv2.COLORMAP_JET)

#img = (heatmap * INTENSITY )#+ img
            mod=((heatmap*-1)+img)
            mod_heat=heatmap
            imshow(heat)
            imshow(mod)
            imshow(mod_heat)
            (flag, encodedImage) = cv2.imencode(".jpg",heat)
            (flag1, encodedImage1) = cv2.imencode(".jpg",mod)
            (flag2, encodedImage2) = cv2.imencode(".jpg",mod_heat)
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage2) + b'\r\n')
            #,b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage1) + b'\r\n',b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage2) + b'\r\n'
    cap.release()
    cv2.destroyAllWindows()
