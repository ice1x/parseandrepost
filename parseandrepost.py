# -*- utf-8 -*-
import telebot
import config


bot = telebot.TeleBot(config.TOKEN)
telebot.apihelper.proxy = config.PROXY


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    # Название функции не играет никакой роли, в принципе
    if config.KEYWORD in message.text:
        bot.send_message(config.TO_GROUP_ID, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0, timeout=20)