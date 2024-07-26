import telebot
from telebot import types
import random

class Game:
    def __init__(self, bot):
        self.bot = bot
        self.games = {}
        self.register_handlers()

    def game_start(self, message):
        
        markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Камень')
        btn2 = types.KeyboardButton('Ножницы')
        btn3 = types.KeyboardButton('Бумага')
        markup.add(btn1, btn2, btn3)
        self.bot.send_message(
            message.chat.id,
            '<b><em>НАЧНЕМ ИГРУ "КАМЕНЬ НОЖНИЦЫ БУМАГА"</em></b>',
            reply_markup=markup,
            parse_mode='html'
        )

    def handle_choice(self, message):
        user_choice = message.text
        bot_choice = random.choice(['Камень', 'Ножницы', 'Бумага'])
        result = self.determine_winner(user_choice, bot_choice)
        self.bot.send_message(message.chat.id,f'Вы выбрали: {user_choice}\nБот выбрал: {bot_choice}\n\n{result}')

    def determine_winner(self, user, bot):
        if user == bot:
            return 'Ничья!'
        elif (user == 'Камень' and bot == 'Ножницы') or (user == 'Ножницы' and bot == 'Бумага') or (user == 'Бумага' and bot == 'Камень'):
            return 'Вы выиграли!'
        else:
            return 'Бот выиграл!'

    def register_handlers(self):
        @self.bot.message_handler(func=lambda message: message.text in ['Камень', 'Ножницы', 'Бумага'])
        def choice_handler(message):
            self.handle_choice(message)



   
       
    
    
        
        
    