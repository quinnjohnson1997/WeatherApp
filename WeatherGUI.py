import tkinter as tk
import requests

HEIGHT = 450
WIDTH = 600


#def test_function(entry):
#    print("This is the entry:", entry)

#b66d9ea0677eb4568662b51b3884d9e8
#pro.openweathermap.org/data/2.5/forecast/hourly?q={city name}&appid={your api key}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
    except:
        final_str = 'Are You Stupid? Thats Not A Place'
    return final_str


def get_weather(city):
    weather_key = 'b66d9ea0677eb4568662b51b3884d9e8'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


def onReturn(event):
    return get_weather(entry.get())

root = tk.Tk()

root.title("Quinn's Weather App")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='WeatherAppBkg.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#6683AB', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.bind("<Return>", onReturn)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#6683AB', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
