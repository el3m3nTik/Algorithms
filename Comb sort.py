#Сортировка прочесыванием n(o^2)
array = [1, 3, -4, 10, 12, 9, 18]
n = len(array)
step = n

while step > 1 or q:
   if step > 1:
       step -= 3
   q, i = False, 0
   while i + step < n:
      if array[i] > array[i + step]:
          array[i], array[i + step] = array[i + step], array[i]
          q = True
      i += step
print(array)