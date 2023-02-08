# pip install python-telegram-bot
from telegram.ext import *
import connectChatGPT

token = "5889124096:AAGMzQMAtbNCS64lxO1Ni5IYAkJQzGF77J4"
print('Starting up bot...')


# Lets us use the /start command
def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot that config by Le Minh Tri. To show more commands, please type "/help"')


# Lets us use the /help command/start
def help_command(update, context):
    update.message.reply_text('/start Start your own chat bot\n/startChatGPT Start chatGPT \n/closeChatGPT Disconnect to chatGPT\n/about Show more infors about author ')

# Lets us use the /about command
def about_command(update, context):
    update.message.reply_text('I am a highly motivated and detail-oriented software developer with a passion for creating innovative and efficient solutions. With 2 in the industry. My experience ranges from building scalable web applications to developing custom software for clients. I am confident in my ability to take on any challenge and consistently deliver high-quality results. When I am not coding, I enjoy staying up to date with the latest technology trends and attending local meetups.')

# Lets us use the /about command
def startchatgpt_command(update, context):
    context.user_data['isStart'] = True
    update.message.reply_text('Start ChatGPT, you can ask any question: ')


# Lets us use the /about command
def closechatgpt_command(update, context):
    context.user_data['isStart'] = False
    update.message.reply_text('Disconnect to ChatGPT')


def handle_response(text) -> str:
    # Create your own response logic

    return connectChatGPT.generate_text(text)


def handle_message(update, context):
    # Get basic info of the incoming message
    if context.user_data['isStart']:
        message_type = update.message.chat.type
        text = str(update.message.text).lower()
        response = ''

        # Print a log for debugging
        print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

        # React to group messages only if users mention the bot directly
        if message_type == 'group':
            # Replace with your bot username
            if '@bot19292bot' in text:
                new_text = text.replace('@bot19292bot', '').strip()
                response = handle_response(new_text)
        response = handle_response(text)

        # Reply normal if the message is in private
        update.message.reply_text(response)
    else:
        update.message.reply_text("Please type '/startChatGPT' first'")

# Log errors
def error(update, context):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('about', about_command))
    dp.add_handler(CommandHandler('startChatGPT', startchatgpt_command))
    dp.add_handler(CommandHandler('closeChatGPT', closechatgpt_command))
    

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()