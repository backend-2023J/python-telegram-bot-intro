import telegram
import os 

TOKEN=os.environ['TOKEN']

bot = telegram.Bot(token=TOKEN)

update = bot.getUpdates()

chat_id = update[-1].message.chat.id
text = update[-1].message.text
print(chat_id, text)

bot.sendMessage(chat_id=chat_id, text=text)