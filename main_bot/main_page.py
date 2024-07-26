import telebot
from telebot import types
from game import Game
from number_guess_game import NumberGame

class MainPage:
    def __init__(self, bot):
        self.bot = bot
        self.register_handlers()

    def start(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        btn1 = types.KeyboardButton('КАМЕНЬ НОЖНИЦЫ БУМАГА')
        btn2 = types.KeyboardButton('УГАДАЙ ЧИСЛО')
        markup.add(btn1, btn2)
        self.bot.send_message(message.chat.id,f'Привет <b>{message.from_user.first_name}</b>, выбери игру',reply_markup=markup,parse_mode='html')

    def handle_choice(self, message):
        user_choice = message.text
        if user_choice == 'КАМЕНЬ НОЖНИЦЫ БУМАГА':
            game = Game(self.bot)
            game.game_start(message)
        elif user_choice == 'УГАДАЙ ЧИСЛО':
            number_game = NumberGame(self.bot)
            number_game.start(message)
        else:
            self.bot.send_message(message.chat.id, "Пожалуйста, выбери одну из предложенных игр.")

    def register_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def start_handler(message):
            self.start(message)

        @self.bot.message_handler(func=lambda message: message.text in ['КАМЕНЬ НОЖНИЦЫ БУМАГА', 'УГАДАЙ ЧИСЛО'])
        def choice_handler(message):
            self.handle_choice(message)
