import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def wait(chat_id, question):
    delay_second = parse(question)
    wait_message = f"Осталось {delay_second} секунд \n"
    initial_message_id = bot.send_message(chat_id, wait_message)
    bot.create_countdown(delay_second, notify_progress, notify_id=chat_id, message_id=initial_message_id, total_time=delay_second)
    bot.create_timer(delay_second, choose, autor_id=chat_id)


def notify_progress(secs_left, notify_id, message_id, total_time):
    progress_bar = render_progressbar(total_time, total_time - secs_left)
    message = f"Осталось {secs_left} секунд \n {progress_bar}"
    bot.update_message(notify_id, message_id, message)


def choose(autor_id):
    message = 'Время вышло!'
    bot.send_message(autor_id, message)


def main():
    global bot
    load_dotenv()
    login = os.getenv('TG_TOKEN')
    bot = ptbot.Bot(login)

    bot.reply_on_message(wait)
    bot.run_bot()


if __name__ == '__main__':
    main()
