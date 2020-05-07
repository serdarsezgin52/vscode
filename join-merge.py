import pandas as pd

# customers = {
#     "CustomerId":[1,2,3,4],
#     "FirstName" :["Ahmet","Ali","Hasan","Canan"],
#     "LastName"  :["Yılmaz","Korkmaz","Çelik","Toprak"]
# }

# orders = {
#     "OrderId" : [10,11,12,13],
#     "CustomerId" : [1,2,5,7],
#     "OrderDate" : ["2010.04.12","2010.05.14","2010.11.29","2011.08.03"]
    
# }

# df_customers = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
# df_orders = pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])

# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers,df_orders,how="inner")
# result = pd.merge(df_customers,df_orders,how="left")
# result = pd.merge(df_customers,df_orders,how="right")


customersA = {
    "CustomerId":[1,2,3,4],
    "FirstName" :["Ahmet","Ali","Hasan","Canan"],
    "LastName"  :["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    "CustomerId":[4,5,6,7],
    "FirstName" :["Yağmur","Çınar","Cengiz","Can"],
    "LastName"  :["Dişli","Sezgin","Yılmaz","Turan"]
}



df_customersA = pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])


result = pd.concat ([df_customersA,df_customersB])
result = pd.concat ([df_customersA,df_customersB],axis=1)

print(result)