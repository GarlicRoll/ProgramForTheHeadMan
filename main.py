import telebot
import os
import websiteconfig

def init_bot(): # инициализация бота
    print("Bot_init")
    '''
    with open("program_for_the_headman\\bot_token.txt", "r") as file:
        telegram_token = file.readline()
        global bot
        bot = telebot.TeleBot(telegram_token)
    '''

    telegram_token = os.environ.get('TOKEN')
    global bot
    bot = telebot.TeleBot(telegram_token)

if __name__ == "__main__":
    bot = None
    init_bot()
    print("Start")

@bot.message_handler(commands=['test', 'start', 'location'])
def statistic_command(message): # запрос местоположения
    Geo = telebot.types.ReplyKeyboardMarkup(True, True)
    button_geo = telebot.types.KeyboardButton("Отметиться на паре", request_location=True)
    Geo.add(button_geo) # добавление кнопки
    # создаём объект закрытия кастомной клавиатуры
    Geo_close = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'Поделитесь местоположением или введите адрес', reply_markup=Geo )

@bot.message_handler(content_types=['location'])
def handle_loc(message):
    message_buffer_id = 100
    file_buffer_id = 110
    longitude = message.location.longitude
    latitude = message.location.latitude
    # создание файла
    with open("data.txt", "r+") as file:
        #file.write(str(longitude) + " " + str(latitude))
        file.write('test text')
        bot.edit_message_media(chat_id=message.chat.id, message_id=message_buffer_id, media=file_buffer_id)
        #print(bot.send_document(message.chat.id, file).id)
    #print(message.id)
    # проверка местоположения
    if round(longitude, 3) == 30.297 and round(latitude, 3) == 59.972: #59.97168732680863, 30.296766628835186
        text = "Молодец, " + str(message.from_user.first_name) + ", ходи на пары в 6 корпус дальше!"
    elif round(longitude, 3) == 30.323 and round(latitude, 3) == 59.972: #59.97225610894957, 30.322730700399283
        text = "Молодец, " + str(message.from_user.first_name) + ", ходи на пары дальше!"
    else:
        text = "ААА, " + str(message.from_user.first_name) + "!!! ТЫ НЕ В ЛЭТИ!!!"
    bot.send_message(message.chat.id, text)

bot.polling()