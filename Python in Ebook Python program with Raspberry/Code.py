# 01 Keywords

import keyword
def Keyword():
    print(keyword.kwlist)
    
    
#Keyword()    


# 02 type 
def type_val():
    age= 3
    print(type(age))
#type_val()


# 03 Math
# import math
# print( math.factorial(7))
# print((math.pi))


# 04 NumPy Arrays

# import numpy as np
# a= np.array( ( [1,2,3], [4,5,6] ) )
# b= np.array( ( [7,8,9], [10,11,12] ))
# print(a*b)    

def checkInput():
    inp= input("Enter the input: \n")
    print(type(inp))
    if( str(inp).isdigit() ):
        print("This is a number")
    else:
        print("It not a number")
   
#checkInput()