from telebot import TeleBot
bot = TeleBot("8039241842:AAHRu6QftAcv9y5z_JaracW3PXYgxibAL7I")

@bot.message_handler(commands=["start"])
def first(message):
    bot.send_message(message.chat.id,"про какие времена хочешь узнать?",parse_mode="Markdown")
    
@bot.message_handler(commands=["command1"])
def second(message):
    bot.send_message(message.chat.id, "*Present Continious*\n(действия,происходящие в даный момент)\nto be + doing\nI am working.\n\n*Present Simple*\n(повторяющееся действие)\ndo/don't + do; does/doesn't + do\nHe works.\n\n*Perfect*\n(действие закончилось к данному моменту)\nhave/has + V+ed\\nI have worked.\n\n*Perfect Continious*\n(действие,начавшееся в определенный момент и совершается до указанного момента)\nhave/has + been V+ing\nI have been working since 8AM", parse_mode="Markdown")
    
@bot.message_handler(commands=["command2"])
def third(message):
    bot.send_message(message.chat.id, "*Continious*\n(действия,происходящие в даный момент)\nwas/were + V+ing\n\n*Present Simple*\n(повторяющееся действие)\nV+ed\n\n*Perfect*\n(действие закончилось к данному моменту)\nhad + V+ed\n\n*Perfect Continious*\n(действие,начавшееся в определенный момент и совершается до указанного момента)\nhad been V+ing", parse_mode="Markdown")

@bot.message_handler(commands=["command3"])
def fourth(message):
    bot.send_message(message.chat.id,"*Continious*\n(действия,происходящие в даный момент)\nwill V+ing\n\n*Present Simple*\n(повторяющееся действие)\nwill + V\n\n*Perfect*\n(действие закончилось к данному моменту)\nwill + by the time have V+ed\n\n*Perfect Continious*\n(действие,начавшееся в определенный момент и совершается до указанного момента)\nwill + have been V+ing", parse_mode="Markdown")
    
@bot.message_handler(commands=["command4"])
def fifth(message):
    bot.send_message(message.chat.id, "Общая [таблица](https://mulino58.ru/wp-content/uploads/4/9/8/4986dc3fc3cbc91d28230e5f9f77f817.jpe) по всем временам английского языка", parse_mode="Markdown")

bot.infinity_polling()
