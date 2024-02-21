import time
import tkinter
import requests

from tkinter import *


def getWeather(event):
    try:
        city = textField.get()
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=9036b0259df683d94625d841023d526f"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise']))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset']))

        final_info = condition + "\n" + str(temp) + "°C"
        final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
            max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
            humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset

        label1.config(text=final_info)
        label2.config(text=final_data)

    except Exception:
        label1.config(text="О нет!")
        label2.config(text="Город не найден😔")
        image()


def image():
    canvas = Canvas(root, bg='white', height=300, width=311)
    canvas.pack()
    test = PhotoImage(file='pyimage1.png')
    canvas.create_image(0, 0, anchor=NW, image=test)
    root.mainloop()


def main():
    global root, textField, label1, label2
    root = tkinter.Tk()

    root.geometry("600x500")
    root.title("Weather App by Команда мечты КМПО")

    f = ("poppins", 15, "bold")
    t = ("poppins", 35, "bold")

    textField = tkinter.Entry(root, justify='center', width=20, font=t)
    textField.pack(pady=30)
    textField.focus()
    textField.bind('<Return>', getWeather)

    label1 = tkinter.Label(root, font=t)
    label1.pack()
    label2 = tkinter.Label(root, font=f)
    label2.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
