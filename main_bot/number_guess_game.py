import telebot
from telebot import types
import random

class NumberGame:
    def __init__(self, bot):
        self.bot = bot
        self.games = {}  # Словарь для хранения текущих игр по идентификаторам чата
        self.register_handlers()
        
    def start(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=3)
        buttons = [
            types.KeyboardButton('1'),
            types.KeyboardButton('2'),
            types.KeyboardButton('3'),
            types.KeyboardButton('4'),
            types.KeyboardButton('5'),
            types.KeyboardButton('6'),
            types.KeyboardButton('7'),
            types.KeyboardButton('8'),
            types.KeyboardButton('9')
        ]
        markup.add(*buttons)
        self.bot.send_message(message.chat.id, '<b><em>НАЧНЕМ ИГРУ "УГАДАЙ ЧИСЛО"</em></b>', reply_markup=markup, parse_mode='html')
        self.games[message.chat.id] = {'number': random.randint(1, 9), 'attempts': 3}
        
    def handle_choice(self, message):
        game_data = self.games.get(message.chat.id)
        if not game_data:
            self.bot.send_message(message.chat.id, 'Для начала игры введите /number_game')
            return
        
        user_choice = int(message.text)
        correct_number = game_data['number']
        
        if user_choice == correct_number:
            result = 'Вы угадали!'
            self.games.pop(message.chat.id, None)
        elif user_choice < correct_number:
            result = f'Вы не угадали! Загаданное число <b>БОЛЬШЕ</b>. Осталось попыток: {game_data["attempts"]}.'
        else:
            result = f'Вы не угадали! Загаданное число <b>МЕНЬШЕ</b>. Осталось попыток: {game_data["attempts"]}.'

        game_data['attempts'] -= 1
        
        if game_data['attempts'] <= 0:
            result += f'\nПравильный ответ был: {correct_number}.'
            self.games.pop(message.chat.id, None)
        
        self.bot.send_message(message.chat.id, f'Вы выбрали: {user_choice}\n\n{result}',  parse_mode='html')

    def register_handlers(self):
        @self.bot.message_handler(commands=['number_game'])
        def start_handler(message):
            self.start(message)

        @self.bot.message_handler(func=lambda message: message.text.isdigit() and int(message.text) in range(1, 10))
        def choice_handler(message):
            self.handle_choice(message)

