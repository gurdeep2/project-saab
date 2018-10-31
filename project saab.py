# import requests
# from pprint import pprint
#
# api_address="http://api.openweathermap.org/data/2.5/forecast?units=metric&appid=fb3388900d1941a46519ededdedf7336&q="
# city=input("enter the name of city: ")
# url=api_address+city
# json_data=requests.get(url).json()
# print(json_data)
# temp=json_data['list'][0]['main']['temp']
# temp_max=json_data['list'][0]['main']['temp_max']
# temp_min=json_data['list'][0]['main']['temp_min']
# pressure=json_data['list'][0]['main']['pressure']
# humidity=json_data['list'][0]['main']['humidity']
# wind_speed=json_data['list'][0]['wind']['speed']
# wind_direction=json_data['list'][0]['wind']['deg']
# cloudiness=json_data['list'][0]['clouds']['all']
# rain=json_data['list'][0]['rain']
#
# print('Temperature: {} degree celcius'.format(temp))
# print('Maximum Temperature: {} degree celcius'.format(temp_max))
# print('Minimum Temperature: {} degree celcius'.format(temp_min))
# print('Pressure: {} hPa'.format(pressure))
# print('Humidity: {} %'.format(humidity))
# print('Wind_speed: {} m/s'.format(wind_speed))
# print('Wind_direction: {} degrees'.format(wind_direction))
# print('Cloudiness: {} %'.format(cloudiness))
# print('Rain: {} mm'.format(rain))

from tkinter import *
import requests
def weather():
    api_address="http://api.openweathermap.org/data/2.5/weather?units=metric&appid=fb3388900d1941a46519ededdedf7336&q="
    city=str(entry_1.get())
    url=api_address+city
    json_data=requests.get(url).json()
    #pprint(json_data)
    temp=json_data['main']['temp']
    temp_max=json_data['main']['temp_max']
    temp_min=json_data['main']['temp_min']
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind_speed=json_data['wind']['speed']
    wind_direction=json_data['wind']['deg']
    cloudiness=json_data['clouds']['all']


    label_temp.config(text="{} degree celcius".format(temp))
    label_maxtemp.config(text="{} degree celcius".format(temp_max))
    label_mintemp.config(text="{} degree celcius".format(temp_min))
    label_pressure.config(text="{} hPa".format(pressure))
    label_humidity.config(text="{} %".format(humidity))
    label_WindSpeed.config(text="{} m/s".format(wind_speed))
    label_WindDirection.config(text="{} degrees".format(wind_direction))
    label_Cloudiness.config(text="{} %".format(cloudiness))

def location():
    x = entry_2.get()
    y = entry_3.get()
    api_address = (
        "http://api.openweathermap.org/data/2.5/weather?units=metric&appid=fb3388900d1941a46519ededdedf7336&lon={}&lat={}").format(
        x, y)
    # longitude = str(entry_2.get())
    # latitude = str(entry_3.get())

    url = api_address

    json_data = requests.get(url).json()
    # pprint(json_data)

    lon = json_data['coord']['lon']
    lat = json_data['coord']['lat']

    label_Longitude.config(text="{} ".format(lon))
    label_Latitude.config(text="{} ".format(lat))


root=Tk()
root.title("kalsia weather app")
root.geometry('500x700')

root.iconbitmap('Sun.ico')

bg_image=PhotoImage(file="C:\\Users\\user\\PycharmProjects\\Python\\waethergonewiild_1280.gif")
bg_label=Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

city=Label(root,text="Enter City Name",font=("Bold ",17))
city.place(x=100,y=50)

entry_1=Entry(root,width=30)
print(entry_1.get())
entry_1.place(x=400,y=50,height=35)


Longitude = Label(root,text = "Enter Longitude..: ",font=("Bold",15))
Longitude.place(x=100,y=100)

entry_2 = Entry(root,width=30)
print(entry_2.get())
entry_2.place(x=400,y=100,height=35)

Latitude = Label(root,text = "Enter Latitude..... ",font=("Bold",15))
Latitude.place(x=100,y=150)

entry_3 = Entry(root,width=30)
print(entry_3.get())
entry_3.place(x=400,y=150,height=35)


b1=Button(root,text="show weather",command=weather,bg="red",fg="white")
b1.place(x=600,y=50)

b2= Button(root, text= "Show Lan & Lat",command=location,bg="red",fg="white")
b2.place(x=600,y=130)

Label_1=Label(root, width=30,height=2, text="Temperature")
Label_1.place(x=100,y=200)

Label_2=Label(root, width=30,height=2, text="Max_Temp")
Label_2.place(x=100,y=250)

Label_3=Label(root, width=30,height=2, text="Min_Temp")
Label_3.place(x=100,y=300)

Label_4=Label(root, width=30,height=2, text="Pressure")
Label_4.place(x=100,y=350)

Label_5=Label(root, width=30,height=2, text="Humidity")
Label_5.place(x=100,y=400)

Label_6=Label(root, width=30,height=2, text="Wind speed")
Label_6.place(x=100,y=450)

Label_7=Label(root, width=30,height=2, text="Wind Direction")
Label_7.place(x=100,y=500)

Label_8=Label(root, width=30,height=2, text="Cloudiness")
Label_8.place(x=100,y=550)

Label_9=Label(root,width=30,height=2,text="Longitude")
Label_9.place(x=100,y=600)

Label_10=Label(root,width=30,height=2,text="Latitude")
Label_10.place(x=100,y=650)

label_temp=Label(root,width=25)
label_temp.place(x=400,y=200)

label_maxtemp=Label(root,width=25)
label_maxtemp.place(x=400,y=250)

label_mintemp=Label(root,width=25)
label_mintemp.place(x=400,y=300)

label_pressure=Label(root,width=25)
label_pressure.place(x=400,y=350)

label_humidity=Label(root,width=25)
label_humidity.place(x=400,y=400)

label_WindSpeed=Label(root,width=25)
label_WindSpeed.place(x=400,y=450)

label_WindDirection=Label(root,width=25)
label_WindDirection.place(x=400,y=500)

label_Cloudiness=Label(root,width=25)
label_Cloudiness.place(x=400,y=550)

label_Longitude=Label(root,width=25)
label_Longitude.place(x=400,y=600)

label_Latitude=Label(root,width=25)
label_Latitude.place(x=400,y=656)

root.mainloop()






