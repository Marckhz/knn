import numpy as np
import math
#import cv2

from PIL import Image

testdata = np.loadtxt("rsTrain.txt")
print(testdata)

#img1 = Image.fromarray(testdata)
#img1.show()

band1 = np.fromfile('band1.irs', dtype ='uint8')
band2 = np.fromfile('band2.irs', dtype='uint8')
band3 = np.fromfile('band3.irs', dtype='uint8')
band4 = np.fromfile('band4.irs', dtype='uint8')



print(band1)

print("shape", band1.shape)


x = testdata[:,0:4]


print(testdata.shape)

"""
k = 1
vector = []
distance = 0
i = 0
for cell in np.nditer(band1, order = 'C'):
    distance = np.sqrt(np.square(x- cell) )
    #print(distance)
    #i+=1
    #if i == 50:
    #    break
print(type(distance) )
print("distancia sorted" )
sorted_distance = (np.sort(distance))
print(sorted_distance)
print("tamanio de sorted distance", len(sorted_distance))
new_band1 = sorted_distance
print("sorted_Band")
print(new_band1[:,0])
print("size of new band1",len(new_band1))
"""



#x2 = testdata[:,0]
#print(x2.shape)


reshape_band1  = np.reshape(band1, (512,512) )
reshape_band2 = np.reshape(band2, (512, 512) )
reshape_band3  = np.reshape(band3, (512, 512) )
reshape_band4 = np.reshape(band4, (512, 512) )

#img = Image.fromarray(reshape_band4)
#img.show()



#img1 = Image.fromarray(reshape_band1)
#img1.show()
#img2 = Image.fromarray(reshape_band2)
#img2.show()

#img3 = Image.fromarray(reshape_band3)
#img3.show()


img4 = Image.fromarray(reshape_band4)
#img4.show()


kolkata = reshape_band1 + reshape_band2 + reshape_band3 + reshape_band4
print(kolkata)
#img = Image.fromarray(kolkata)
#img.show()


k = 1
vector = []
distance = 0
i = 0
for cell in np.nditer(x, order = 'C'):
    distance = np.sqrt(np.square(kolkata - cell) )
    #print(distance)
    #i+=1
    #if i == 50:
    #    break
print(type(distance) )
print("distancia sorted" )
sorted_distance = (np.sort(distance))
print(sorted_distance)
print("tamanio de sorted distance", len(sorted_distance))
new_band1 = sorted_distance
print("sorted_Band")
print(new_band1)
print("size of new band1",len(new_band1))
print("size", new_band1.shape)

print(new_band1[:,0])

#neighbors = new_band1[]

#y = testdata[:,-1]
#print(y)




















"""
print("primer banda")
print(band1)
print(band1.shape)

print("segunda banda")
print(band2)
print(band2.shape)

print("tercer banda")
print(band3)
print(band3.shape)

print("cuarta banda")
print(band4.shape)
"""


#print("el dataset")
#print(dataset)
#print(dataset.shape)
