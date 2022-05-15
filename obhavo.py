import telebot
from telebot import types
import json
import requests
import time
import datetime


dt=datetime.datetime.today()

TOKEN = "BOT TOKEN"

bot=telebot.TeleBot(TOKEN)

markup = types.ReplyKeyboardMarkup(one_time_keyboard=True , resize_keyboard=True, row_width=2)
itembtn1 = types.KeyboardButton('Tashkent')
itembtn2 = types.KeyboardButton('Andijan')
itembtn3 = types.KeyboardButton('Khiva')
itembtn4 = types.KeyboardButton('Bukhara')
itembtn5 = types.KeyboardButton('Samarqand')
itembtn6 = types.KeyboardButton('Karakalpakstan')

itembtn7 = types.KeyboardButton('Fergana')
itembtn8 = types.KeyboardButton('Namangan')
itembtn9 = types.KeyboardButton('Jizzax')
itembtn10 = types.KeyboardButton('Qarshi')
itembtn11= types.KeyboardButton('Navoiy')
itembtn12= types.KeyboardButton('Nukus')
itembtn13= types.KeyboardButton('Sirdaryo')

markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10, itembtn11, itembtn12,itembtn13)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Assalom alaykum.🙋‍♂️' +message.from_user.first_name +'\nOb-havo telegram botiga hush kelibsiz 🌤⛅️')
    time.sleep(1)
    bot.send_message(message.chat.id,'Iltimos o\'z viloyatingizni tanlang 🔽',reply_markup=markup)



@bot.message_handler(commands=['about'])
def start(message):
    bot.send_message(message.chat.id, 'Assalom alaykum.🙋‍♂️' +message.from_user.first_name +'\n\nDasturchi👨🏻‍💻: https://firdavsdev.vercel.app \n ')

@bot.message_handler(content_types=['text'])
def obhavo(message):
    city=message.text
    api='https://api.openweathermap.org/data/2.5/weather'

    r=requests.post(url=api,params={'q':city, 'appid':'2b1a7a854d5f2d7836540ae70a2702cc','units':'metric'})

    #r=requests.post(url=api,params=pp)
    if r.status_code==200:

        response=json.loads(r.content)
        temp=str(response['main']['temp'])
        temp_max=str(response['main']['temp_max'])
        temp_min=str(response['main']['temp_min'])
        speed=str(response['wind']['speed'])

        xabar='Bugun,⌛️ '+ str(dt.day)+ ' April' '\n\n\n' 'Hozir '+str(city)+'da☀️:  +'+ str(temp) +' C°'+'\n\n'+'Eng yuqori harorat:☀️  +' + str(temp_max) +' C° \n\n'+'Past harorat☀️  +'+ str(temp_min) +' C°'+'\n\n'+'Shamol tezligi:🌪 '+speed+'.'
        bot.send_message(message.chat.id, xabar,reply_markup=markup)
    else:
        bot.send_message(message.chat.id,'Uzr viloyat yoki shaharingizni Ingliz tilida kiriting😇',reply_markup=markup)

bot.polling(none_stop=True)
