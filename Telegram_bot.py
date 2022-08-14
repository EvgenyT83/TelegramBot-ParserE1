import telebot
from settings import token
from request import req

def main():
    # Создаем экземпляр бота
    bot = telebot.TeleBot(token)

    # Функция, обрабатывающая команду /start
    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
    # Получение сообщений от юзера
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == "Привет":
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Напиши е1 для новостей")
        elif message.text == "е1" or message.text == "e1":
            bot.send_message(message.from_user.id, "Последние 10 новостей с сайта Е1:")
            all_news = req()
            for news in all_news[:10]:
                bot.send_message(message.from_user.id, news)
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

    # Запускаем бота
    bot.polling(none_stop=True, interval=0)