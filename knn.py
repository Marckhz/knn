import numpy as np
import math
#import cv2

from PIL import Image

trainingdata = np.loadtxt("rsTrain.txt")
print(trainingdata)

#img1 = Image.fromarray(testdata)
#img1.show()

band1 = np.fromfile('band1.irs', dtype ='uint8')
band2 = np.fromfile('band2.irs', dtype='uint8')
band3 = np.fromfile('band3.irs', dtype='uint8')
band4 = np.fromfile('band4.irs', dtype='uint8')



print(band1)

print("shape", band1.shape)


x = trainingdata[:,0:4]




print(trainingdata.shape)



#print(distance)

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


band_1_to_test = x[:,0]
band_2_to_test = x[:,1]

#print(band_1_to_test)

#en esta parte estoy iterando
#por el la primer colimna del dataset de entrenamiento
#y esto sacando la distancia  del training set y el testset
#ahora necesito sacar los k vecinos.
#voy  a ordernar el array y tomar los k vecinos.
#despues de eso que?

distance = 0
#distancias con indices
index_and_distance = []
for point in band_1_to_test:
    distance += np.square(reshape_band1 - point)
    index_and_distance.append(distance)
    #print(distance)
square_distance = np.sqrt(index_and_distance)
sorted_distance  = np.sort(square_distance)
#print(sorted_distance)

#lets_sort_index_and_distance = sorted(index_and_distance)
print("\n \n \n ")
#print(lets_sort_index_and_distance)
k  = 1
neighbors = []
for x in range(k):
    #print(sorted_distance[])
    neighbors.append(sorted_distance[x])
#print(neighbors)
np_neighbors = np.array(neighbors)
var = np.reshape(np_neighbors, (512, 512) )
print(var.shape)
#print(var)
print(reshape_band1)
j=0
#for i in neighbors[0][0]:
#    print(i)
#    j+=1
#print(j)









#sorted_distance = np.sort(square_distance)

#print("sorted distance ", sorted_distance)
#print(sorted_distance.index)
k = 1
#neighbors = []

#for x in range(k):
 #  neighbors.append(sorted_distance[x][:,0])
#print(neighbors)


#img = Image.fromarray(reshape_band4)
#img.show()

"""





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
    distance = np.sqrt(np.square(reshape_band1[0] - cell) )
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
