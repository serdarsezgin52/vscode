import tkinter as tk
import http.client
Height=500
Widh=600

def test_func(entry):
    print('Veri Girişi', entry)
# apikey 4uz5oLmATOn88LsqgxwNGP:2TqxvGyvIRnQAQUoQhGw4Z
#("GET", "api.collectapi.com/weather/getWeather ? data.lang=tr&data.city=ankara", headers=headers)"

def HavaDurumu(sehir):
    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
    'content-type': "application/json",
    'authorization': "apikey 4uz5oLmATOn88LsqgxwNGP:2TqxvGyvIRnQAQUoQhGw4Z",
    'city': "sehir",
    'degree':"derece"
    }

    # havaDurumu_key ='4uz5oLmATOn88LsqgxwNGP:2TqxvGyvIRnQAQUoQhGw4Z'
    # url = 'https://api.collectapi.com/weather/getWeather'
    # paramtr = {'authorization': havaDurumu_key, 'data.city':sehir, 'units':'degree'}
    response = conn.request("GET", "/weather/getWeather?data.lang=tr&data.city=city", headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


root = tk.Tk()

canvas = tk.Canvas(root, height=Height, width=Widh)
canvas.pack()

bg_img = tk.PhotoImage(file = './hava_drmu.png')
bg_label = tk.Label(root, image=bg_img)
bg_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=.75, relheight=.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=.65, relheight=1)

button = tk.Button(frame, text="Hava Durumu", font=40, command=lambda : HavaDurumu(entry.get()))
button.place(relx=0.7, relwidth=.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)



root.mainloop()

