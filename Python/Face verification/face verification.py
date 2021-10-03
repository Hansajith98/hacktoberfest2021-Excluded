import numpy as np
from PIL import Image
from mtcnn.mtcnn import MTCNN
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_inputinput
import tensorflow as tf

tf.__version__
D = MTCNN()
model = VGGFace(model='resnet50',include_top=False,input_shape=(224,224,3),pooling='avg')

P1 = Image.open(r'C:\Users\lenovo\Desktop\ML\CNN\Data\FaceVerification\pos_1.jpg')
P2 = Image.open(r'C:\Users\lenovo\Desktop\ML\CNN\Data\FaceVerification\pos_2.jpg')
N1 = Image.open(r'C:\Users\lenovo\Desktop\ML\CNN\Data\FaceVerification\neg_1.jpg')
P1
P2
N1
P1 = np.asarray(P1)
P2 = np.asarray(P2)
N1 = np.asarray(N1)

def f_getFace(I):
    r = D.detect_faces(I)
    x1,y1,w,h = r[0]['box']
    x2,y2 = x1+w,y1+h
    face = I[y1:y2,x1:x2]
    return Image.fromarray(face)

f1 = f_getFace(P1)
f2 = f_getFace(P2)
f3 = f_getFace(N1)

f1 = f1.resize((224,224))
f2 = f2.resize((224,224))
f3 = f3.resize((224,224))
f1

f1 = np.asarray(f1,'float32')
f2 = np.asarray(f2,'float32')
f3 = np.asarray(f3,'float32')

f1.shape

PE1 = model.predict(f1[np.newaxis,...])
PE2 = model.predict(f2[np.newaxis,...])
NE3 = model.predict(f3[np.newaxis,...])


PE1.shape

distance_pos = np.sum((PE1-PE2)**2)**0.5
distance_neg = np.sum((PE1-NE3)**2)**0.5

print(distance_pos,distance_neg)