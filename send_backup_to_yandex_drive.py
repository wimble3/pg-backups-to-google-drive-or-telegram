import os
import sys

import requests

from load_env_file import load_env_file


load_env_file("/var/www/db_backups/.env")

YANDEX_DISK_TOKEN = os.getenv("YANDEX_DISK_TOKEN")


def upload_file_to_yandex_disk(filepath: str) -> None:
    headers = {
        "Authorization": f"OAuth {YANDEX_DISK_TOKEN}",
    }

    upload_url = (
        f"https://cloud-api.yandex.net/v1/disk/resources"
        f"/upload?path={os.path.basename(filepath)}&overwrite=true"
    )
    response = requests.get(upload_url, headers=headers)

    if response.status_code == 200:
        upload_link = response.json().get('href')
        with open(filepath, "rb") as dump_file:
            upload_response = requests.put(upload_link, data=dump_file)
            if upload_response.status_code == 201:
                print(
                    f"File uploaded to Yandex Disk: {upload_response.url}")
            else:
                print(
                    f"Error during upload to Yandex Disk: "
                    f"{upload_response.text}"
                )
    else:
        print(f"Error getting upload URL: {response.text}")

    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Dump with filepath {filepath} has been removed from disk")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Failed to parse argv, exit. Example usage: send_backup_yandex.py"
            " /path/to/dump.sql"
        )
        sys.exit(1)

    filepath_arg = sys.argv[1]
    upload_file_to_yandex_disk(filepath_arg)
