import telebot

class Start:
    def __init__(self, bot):
        self.bot = bot
        self.register_handlers()

    def info_start(self, message):
        self.bot.send_message(
            message.chat.id,
            '<b>ИНФОРМАЦИЯ:</b> Этот бот создан для мини-игр, таких как "Угадай число" или "Камень, ножницы, бумага".',
            parse_mode='html'
        )

    def register_handlers(self):
        @self.bot.message_handler(commands=['info'])
        def info_handler(message):
            self.info_start(message)

        @self.bot.message_handler(func=lambda message: message.text.lower() == 'привет')
        def handle_hello(message):
            self.info_start(message)