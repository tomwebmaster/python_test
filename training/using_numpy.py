import numpy as np

arr = np.array([100, 200, 300, 400])
print(arr[:1])

print(arr[1:3])
print('-------------------')

arr2 = np.array([[10, 20, 30], [1000, 2000, 3000]])
print('แถวที่ 1 คอลัมน์ที่ 1 :', arr2[0, 0])
print('แถวที่ 2 คอลัมน์ที่ 1 :', arr2[1, 0])
print('-------------------')
print('แถวที่ 1 คอลัมน์ที่ 2 :', arr2[0, 1])
print('แถวที่ 2 คอลัมน์ที่ 2 :', arr2[1, 1])
print('-------------------')
