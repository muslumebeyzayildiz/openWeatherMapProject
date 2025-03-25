import requests
from tkinter import Tk, Label, Button, Entry, StringVar, PhotoImage
from datetime import datetime

API_KEY = 'buraya https://openweathermap.org/ dan alınan api key yazılmalı'

# Hava durumu alma fonksiyonu
def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr'
    #&units=metric sıcaklığın Celsius (°C) cinsinden olması içiin
    #& lang = tr API’den dönen açıklamaların Türkçe olması için
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()# JSON formatındaki cevabı al
        temp = data['main']['temp']# Sıcaklığı çek
        desc = data['weather'][0]['description'].capitalize()# Hava durumu açıklamasını al ve baş harfini büyüt
        icon_code = data['weather'][0]['icon']# İkon kodunu al
        icon_url = f'http://openweathermap.org/img/wn/{icon_code}@2x.png'# İkon URL'sini oluştur
        return temp, desc, icon_url
    else:
        return None

# Arama fonksiyonu
def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:# Hava durumu bilgisi döndüyse
        temp, desc, icon_url = weather# Dönen değerleri ayrı ayrı değişkenlere ata
        #current_time = datetime.now().strftime('%d %B %Y %A, %H:%M')  # Güncel tarih ve saati al
        lbl_result.config(text=f'{city.capitalize()}\n{temp}°C\n{desc}')  # Sonuçları ekrana yazdır


        icon_data = requests.get(icon_url).content # İkon verisini çek
        with open('temp_icon.png', 'wb') as icon_file:# İkonu kaydet
            icon_file.write(icon_data)
        icon_image.config(file='temp_icon.png')# icon'u  görüntüle
    else:
        lbl_result.config(text='Şehir bulunamadı.')

# Tkinter pencere oluşturma
app = Tk()
app.title('M.Beyza Yıldız')
app.geometry('300x350')
app["bg"]="white"
app.resizable(False, False)

# Kullanıcının şehir adı girdiği alan
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text, font=('Arial', 14), justify='center', bg='#b6dcfa')
city_entry.pack(pady=15)

# Ara butonu
search_btn = Button(app, text='Hava Durumunu Getir', command=search, font=('Arial', 12), bg='#3b83bd', fg='white')
search_btn.pack()

# Sonuçları göster
lbl_result = Label(app, text='', font=('Arial', 16),bg='white', pady=20)
lbl_result.pack()

# Hava durumu ikonunu göster
icon_image = PhotoImage()
icon_label = Label(app, image=icon_image,bg='white')
icon_label.pack()

app.mainloop()