# -*- utf-8 -*-
import telebot
import config


bot = telebot.TeleBot(config.TOKEN)
telebot.apihelper.proxy = config.PROXY
bot.get_chat(config.FROM_GROUP_ID)


@bot.message_handler(content_types=["text"])
def repost(message):
    if config.KEYWORD in message.text and str(message.chat.id) == config.FROM_GROUP_ID:
        bot.send_message(config.TO_GROUP_ID, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0, timeout=20)