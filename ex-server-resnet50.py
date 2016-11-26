# ex-resnet50.py
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

model = ResNet50(weights='imagenet')

img_path = '/users/shravankumar/PyImageSearch/imagenet-example/images/beer.png'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
# print('Predicted:', decode_predictions(preds, top=1)[0])
pred = decode_predictions(preds, top=1)[0]

for x in pred:
	# print(x)
   	print("I think it's a :{} ".format(x[1])) 
   	print("Yeah, I'm {}% sure".format(x[2]*100))