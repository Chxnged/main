import diser

bot = diser.App("TOKEN")

@bot.listen("message")
def ping(msg):

    if msg.text == "!ping":
        msg.answer("pong")

bot.start()
