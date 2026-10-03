import numpy as np 
#print (np.__version__)

#my_list=[1,2,3,4]
# my_list=my_lis*2
# print(my_list)
#duplicate the numbers in the list 


# my_list=np.array([1,2,3,4,5])
# my_list=my_list*2
# print(my_list)
# print(type(my_list)) 

#1d array 
# array=np.array(['A']) 
# print(array.ndim)

# 2D array
# array =np.array([['A','B'],['C','D']])
# print(array.ndim)

# array =np.array([[['A','B'],['C','D']],
#                  [['E','F'],['G','H']],
#                  [['I','J'],['K','L']]])
# print(array.ndim)
# print(array.shape)

#multidiemnsional indexing
#print(array[0,0,0]) #first 0 is layer second one is row no. and third one is col no. 
#making word with mulitdimensional indexing
# word=array[0,0,0]+array[2,0,0]+array[2,1,1]
# print(word)


#slicing using numpy 

# #array=np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [9,10,11,12],
#                 [13,14,15,16]])
 
#array[start:end:step] ending index is exclusive 
# print(array[0:4:2]) #thats for row selection 

#for col selection

#print(array[:,3]) # last is col no  and before : is row no empty means all 

#print(array[:,0:3:2])  # values after , are like this array[start:end:step]
   
#combine row and col selection in slicing 

#print(array[0:2,0:2]) # it is like this one array[row(start:end:step),col(start:end:step)]
    
#### arithmetic 

#scalar arithmetic 


# array=np.array([1,2,3,4])

# print(array+1)
# print(array-1)
# print(array*1)
# print(array/10)
# print(array**5)

#vectorize math functions 

# array=np.array([1.01,2.2,3.34,4.123])
# print(np.sqrt(array))
# print(np.round(array))
# print(np.pi)

#exercise 
# radii=np.array([1,2,3])
# print(np.pi*radii**2)

#element wise arithmetic 

# array1=np.array([1,2,3,4])
# array2=np.array([5,6,7,8])

# print(array1+array2)
# print(array1-array2)
# print(array1*array2)
# print(array1/array2)


#comparison operators == != >= <= < > 
  
# array1=np.array([10,32,53,74])
# array2=np.array([15,96,76,83])

# print (array1>50)


###Broadcasting
#   this allows arrays to perform operatoions with different shapes

# array1=np.array([[1,2,3,4]]) # 1 row 4 col 

# array2=np.array([[1],
#                  [5],
#                  [2],
#                  [3]]) # 4 rows one col

# print(array1.shape)
# print(array2.shape)
#arrays are broadcasting compatible only when any of the dimensions are matching or any one of then are 1 
#(1, 4)
# (4, 1)
# [[ 1  2  3  4]
#  [ 5 10 15 20]
#  [ 2  4  6  8]
#  [ 3  6  9 12]]    this is one example 


#print(array1*array2)

#aggregate functions

# array=np.array([[1,2,3,4],[6,7,8,9]])

# print(np.sum(array))


# print(np.std(array))
# print(np.mean(array))
# print(np.var(array))
# print(np.median(array))
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array))
# print(np.argmax(array))
# print(np.sum(array,axis=0)) #axis zero means all columns axis =1 means all rows


#filtering

# ages=np.array([[21,12,94,35,17],
#                [23,14,73,12,34]])

# teenage=ages[ages<18]
# print(teenage)

# adults=ages[(ages>=18) & (ages<65)]
# print(adults)


# random numbers

rng =np.random.default_rng(seed=1)#used to get same no again

print(rng.integers(1,100,(3,2)))


print(np.random.uniform(-1,1))# floating point random numbers

#shuffling array randomly
array=np.array([1,2,3,4,5,6])
rng.shuffle(array)
print(array)





