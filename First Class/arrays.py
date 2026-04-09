"""
This file shows how to implement arrays and how to work with them
"""

array = [] # This declares an empty array
array.append(3) # append adds stuffs to the array
array.append(4) # [3, 4]
print(array) # [3, 4]

# Adding a different datatype to the array
array.append("python") # on a normal day, array's only accept one datatype
print(array)

ind = [34, 7, 45, 36, 5, 55] # 0, 1, 2, 3, 4, 5

a = ind[0] # a is 34
dd = ind[0:5] # [34, 7, 45, 36]
kk = ind[1:3] # [7, 45]
print("dd = ", dd)

# other python rules below


"""
TO create a virtual environment -> python3 - m venv venv

TO activate the virtual environmeent -> source venv/bin/activate

To install python libraries -> pip install 'name of the library'

To install requirements -> 'pip install -r requirements.txt'

TO gather all the stuffs that you have installed -> pip freeze > requirements.txt
"""
