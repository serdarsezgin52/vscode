import numpy as np

# result = np.array([1,3,5,7,9])
# result = np.arange(1,10)
# result = np.arange(10,100,3)
# result = np.zeros(10)
# result = np.ones(10)
# result = np.linspace(0,100,5)
# result = np.linspace(0,5,5)
# result = np.random.randint(0,20)
# result = np.random.randint(20)
# result = np.random.randint(1,50,6)
# result = np.random.rand(5)
# result = np.random.randn(5)
# np_array = np.arange(50)
# np_multi = np_array.reshape(5,10)
# print(np_multi.sum(axis=1))
# print(np_multi.sum(axis=0))

# rndnum = np.random.randint(1,100,10)
# print(rndnum)
# result =rndnum.max()
# result =rndnum.min()
# result  = rndnum.mean()
# result = rndnum.argmax()
# result = rndnum.argmin()

# nums = np.array([0, 5, 10, 15, 20, 25, 50, 75])

# result = nums[5]
# result = nums[-1]
# result = nums[0:3]
# result = nums[:3]
# result = nums[3:]
# result = nums[::]
# result = nums[::-1]

# nums2 = np.array([[0, 5, 10], [15, 20, 25], [50, 75, 85]])

# result = nums2[0]
# result = nums2[2]
# result = nums2[0, 2]
# result = nums2[2, 1]
# result = nums2[:, 2]
# result = nums2[:, 0]
# result = nums2[:, 0:2]
# result = nums2[-1, :]
# result = nums2[:3, :1]

# arr1 = np.arange(0, 10)
# arr2 = arr1
# arr2[0] = 20
# # print(result)


# print(arr1)
# print(arr2)

nmr1 = np.random.randint(10,100,6)
nmr2 = np.random.randint(10,100,6)

print(nmr1)
print(nmr2)
result = nmr1 + nmr2
result = nmr1 + 10
result = nmr1 - nmr2
result = nmr1 - 10
result = nmr1 * nmr2
result = nmr1 * 10
result = nmr1 / nmr2
result = nmr1 / 10
result = np.sin(nmr1)
result = np.cos(nmr1)
result = np.sqrt(nmr1)
result = np.log(nmr1)
mnmr1 = nmr1.reshape(2,3)
mnmr2 = nmr2.reshape(2,3)

# print(mnmr1)
# print(mnmr2)

result = np.vstack((mnmr1,mnmr2))
result = np.hstack((mnmr1,mnmr2))

result = nmr1 >= 50
result = nmr1 %2 == 0

print(nmr1[result])
print(result)


