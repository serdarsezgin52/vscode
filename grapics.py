import matplotlib.pyplot as plt
# Stack Plot
""" yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,10,12,7,9]
oyuncu2 = [7,21,5,15,21]
oyuncu3 = [18,20,22,25,19]

plt.plot([],[], color="y", label="oyuncu1")
plt.plot([],[], color="r", label="oyuncu2")
plt.plot([],[], color="b", label="oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors=["y","r","b"])

plt.title("Yıllara göre atılan goller")
plt.xlabel("Yıl")
plt.ylabel("Gol Sayısı")

plt.legend() """

# Pie Plot
""" goal_types = "Penaltı", "Kaleye Atılan Şut", "Serbest Vuruş"

goals = [12,35,7]
colors = ["y","r","b"]
plt.pie(goals,labels=goal_types, colors=colors, shadow=True, explode=(0.05,0.05,0.05), autopct="%1.1f%%") """


""" 
Bar Grafiği

plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW", width=.3)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="AUDI",width=.3)

plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe (km)")
plt.title("Araç Bilgileri") """

""" 
histogram Grafiği
yas = [22,34,45,34,65,43,235,65,32,12,14,26,27,38,45,53,62,112,23,99]
yas_gruplari =[10,20,30,40,50,60,70,80,90,100]

plt.hist(yas,yas_gruplari,histtype="bar",rwidth=.8)
plt.xlabel("Yaş grupları")
plt.ylabel("Kişi Sayısı")
plt.title("Histogram Grafiği")
plt.legend()
plt.show() """
