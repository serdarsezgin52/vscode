my_list = [('a', 232), 
           ('b', 343), 
           ('c', 543), 
           ('d', 23)]

for i in zip(*my_list):
    print(i)