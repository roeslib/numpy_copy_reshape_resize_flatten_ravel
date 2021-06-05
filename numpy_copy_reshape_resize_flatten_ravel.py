#Using atribute View, copy, reshape, resize, flatten, ravel

import numpy as np

numbers = np.arange(1,6)

print(numbers)
print()

#atribute view
numbers2 = numbers.view()

print(numbers2)
print()

id(numbers)

id(numbers2)

#multiplicamos el elemento 1 de numbers por 10
numbers[1] *= 10

#imprimimos numbers2 y se observa que el valor 1 cambio
print(numbers2)
print()

#dividimos el valor 1 de numbers2 entre 10
numbers2[1] /= 10

#imprimimos numbers y vemos que el elemento 1 cambio su valor
print(numbers)
print()

print(numbers2)
print()

#se observa que con view todo cambio que se haga en un array
#se hará de igual manera en el otro array. Para realizar cambios
#que no alteren el otro array se debe hacer uso de copy

##################################

#to copy an array and then modified it without modifyieng the original we
#should use the function copy:

numbers = np.arange(1,6)

numbers2 = numbers.copy()

#multiply el elemento 1 de nubers por 10
numbers[1] *= 10

#numbers sufre alteracion el elemento 1
print(numbers)
print()

#numbers2 no sufere alteracion
print(numbers2)
print()

#######################################

#to change the dimension fo the original array there are reshape(which creates a view
#and do not reshape the original) and resize (which reshape the original)

grades = np.array([[87,96,70],[100,87,90]])

#reshape creates a view of the array
grades.reshape(1,6)

#resize alterate the original array
grades.resize(1,6)


#######################################

#to convert an array in one dimension we can use flatten (create a copy of
#the original and do not alterate it) and ravel (alterate the original array is
#a view of the original)

#flatten join the arrays and creates a copy of the original 
flattened = grades.flatten()

#ravel join the arrays and create a view of the original
raveled = grades.ravel()



