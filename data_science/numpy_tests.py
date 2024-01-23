import numpy as np

def test_one_dimension_array(array1):
    
    # create the numpy array
    a = np.array(array1)
    
    typeElements = a.dtype
    
    print(typeElements)
    
    
array1 = ['a', 1, 'b']
test_one_dimension_array(array1)   

array1 = [2, 4, 2000]
test_one_dimension_array(array1)   
