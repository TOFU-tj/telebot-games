import telebot
from config import API
from messages import Start
from game import Game
from number_guess_game import NumberGame
from main_page import MainPage


print('Start')

bot = telebot.TeleBot(API)

start_bot = Start(bot)
main = MainPage(bot)
game = Game(bot)
Number = NumberGame(bot)

if __name__ == '__main__':
    bot.infinity_polling()