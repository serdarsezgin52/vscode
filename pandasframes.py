import pandas as pd

list = [["ahmet",50],["ali",60],["yağmur",70],["çınar",80]]
dict = {"Name":["Ahmet","Ali","Yağmur","Çınar"], "Grade": [50,60,70,80] }
dict_list = [
                {"Name":"Ahmet","Grade":"50"},
                {"Name":"Ali","Grade":"60"},
                {"Name":"Yağmur","Grade":"70"},
                {"Name":"Çınar","Grade":"80"}
]
# df = pd.DataFrame()

# df = pd.DataFrame([1,2,3,4])
# df = pd.DataFrame(data, index=[1,2,3,4], columns=["Name", "Grade"], dtype=float)
# df = pd.DataFrame(dict, dtype=float)
# df = pd.DataFrame(dict, index=["212","322","233","432"], dtype=float)

df = pd.DataFrame(dict_list, index=["212","232","236","456"])

print(df)





# s1 = pd.Series([3,2,1,0])
# s2 = pd.Series([0,3,7,2])
# data =dict(apples = s1 , orange = s2)

# df = pd.DataFrame(data)

# print(df)
