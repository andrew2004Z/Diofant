from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import telebot

bot = telebot.TeleBot("1611301127:AAGcAcctuNEmotkvsuiNJxriQX3AegJcpuU", parse_mode=None)
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
browser.get('https://planetcalc.ru/3303/')
print('Бот готов к работе!')
@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    bot.send_message(message.chat.id, f'Для решения диофантового уравнения, введите три числа в формате "1 2 3", без кавычек.')


@bot.message_handler(content_types=['text'])
def send_text(message):
    sp_c = message.text.split()
    bot.send_message(message.chat.id, 'Пожалуйста, подождите!')
    cof_a = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/input')
    cof_b = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div[3]/div[1]/input')
    cof_c = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div[4]/div[1]/input')
    button = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div[5]/div/button')
    cof_a.clear()
    cof_b.clear()
    cof_c.clear()
    try:
        cof_a.send_keys(sp_c[0])
        cof_b.send_keys(sp_c[1])
        cof_c.send_keys(sp_c[2])
        button.click()
        x = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div[11]/div[2]').text
        y = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div[12]/div[2]').text
        if x == '':
            bot.send_message(message.chat.id, 'Решений нет!')
        else:
            bot.send_message(message.chat.id, f'x = {x}')
            bot.send_message(message.chat.id, f'y = {y}')   
            if int(sp_c[1]) < 0:
                bot.send_message(message.chat.id, f'x = {x} - {abs(int(sp_c[1]))}k')
            else:
                bot.send_message(message.chat.id, f'x = {x} + {abs(int(sp_c[1]))}k')
            if int(sp_c[0]) < 0:
                bot.send_message(message.chat.id, f'y = {y} + {abs(int(sp_c[0]))}k')
            else:
                bot.send_message(message.chat.id, f'y = {y} - {abs(int(sp_c[0]))}k')
    except:
        bot.send_message(message.chat.id, f'Ошибка!')


bot.polling()