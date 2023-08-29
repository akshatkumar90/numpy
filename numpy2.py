#NumPy is used to work with arrays. The array object in NumPy is called ndarray.
#We can create a NumPy ndarray object by using the array() function.
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr)
print(type(arr))   #output >> class 'numpy.ndarray


#Use a tuple to create a NumPy array:
import numpy as np
arr=np.array((11,12,13,14,15,16,17,18))
print(arr)

#use a set and create a Numpy array
import numpy as np
arr=np.array({11,12,13,14,15,16,17,18})
print(arr)