from PIL import Image
import numpy as np

im3 = Image.open('34027692.jpg')
im2 = im3.resize((96, 96))

im = np.array(im2)

print(type(im))
# <class 'numpy.ndarray'>

print(im.dtype)
# uint8

print(im.shape)

im2.save("test.jpg")