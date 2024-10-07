import os
import telebot
import requests
import uuid
from datetime import datetime

BOT_TOKEN = '7454502111:AAGegQ-ckH1j9i0xPXSuZ-cqwhbJ_ej7--8'  # Replace with your bot token

if __name__ == '__main__':
    bot = telebot.TeleBot(BOT_TOKEN)

    links = {}
    users = {}
    old_info = {}
    user_coins = {}
    admins = ['6329796205']  # Replace with your admin ID

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
    def see_old_info(message):
        if message.chat.id in old_info:
            bot.send_message(message.chat.id, "Here is your old information:")
            for info in old_info[message.chat.id]:
                bot.send_message(message.chat.id, info)
        else:
            bot.send_message(message.chat.id, "You don't have any old information.")

    @bot.message_handler(commands=['generate_link'])
    def generate_link(message):
        if message.chat.id in user_coins and user_coins[message.chat.id] >= 20:
            user_coins[message.chat.id] -= 20
            link = str(uuid.uuid4())
            links[link] = message.chat.id
            bot.send_message(message.chat.id, "Here is your link: https://t.me/your_bot_username?start=" + link)
        else:
            bot.send_message(message.chat.id, "You don't have enough coins to generate a link.")

    @bot.message_handler(commands=['add_coins'])
    def add_coins(message):
        if message.chat.id in admins:
            bot.send_message(message.chat.id, "Enter the user ID and the number of coins to add:")
            @bot.message_handler(content_types=['text'])
            def add_coins_text(message):
                try:
                    user_id, coins = message.text.split()
                    user_id = int(user_id)
                    coins = int(coins)
                    if user_id in user_coins:
                        user_coins[user_id] += coins
                        bot.send_message(message.chat.id, "Coins added successfully.")
                        bot.send_message(user_id, "You received " + str(coins) + " coins.")
                    else:
                        bot.send_message(message.chat.id, "User  not found.")
                except ValueError:
                    bot.send_message(message.chat.id, "Invalid input.")
        else:
            bot.send_message(message.chat.id, "You are not an admin.")

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        if message.text.startswith("/"):
            bot.send_message(message.chat.id, "Invalid command.")
        else:
            if message.chat.id in links.values():
                for link, user_id in links.items():
                    if user_id == message.chat.id:
                        if message.chat.id not in old_info:
                            old_info[message.chat.id] = []
                        old_info[message.chat.id].append(message.text)
                        bot.send_message(message.chat.id, "Information received.")
                        break
            else:
                bot.send_message(message.chat.id, "You are not authorized to send information.")