import telebot

import os

import sys

from load_env_file import load_env_file


load_env_file("/var/www/db_backups/.env")


TOKEN = os.getenv("TG_BOT_API_KEY")
CHAT_ID = os.getenv("TG_BOT_BACKUPS_CHAT_ID")


def send_backup_to_telegram(filepath: str) -> None:
    bot = telebot.TeleBot(token=TOKEN)

    try:
        with open(filepath, "rb") as dump_file:
            bot.send_document(CHAT_ID, dump_file)
        print(
            f"Dump with filepath {filepath} has been sent to chat with "
            f"id {CHAT_ID}"
        )
    except Exception as e:  # noqa
        print(f"Error while dump sending: {e}")
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"Dump with filepath {filepath} has been removed from disk")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Failed to parse argv, exit. Example usage: send_backup_tg.py "
            "/path/to/dump.sql"
        )
        sys.exit(1)

    filepath_arg = sys.argv[1]
    send_backup_to_telegram(filepath_arg)

