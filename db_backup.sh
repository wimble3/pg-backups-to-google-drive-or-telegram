#!/bin/bash
source /var/www/db_backups/venv/bin/activate
backup_dir=/var/www/db_backups/
backup_file="$backup_dir/backup_$(date +'%Y%m%d_%H%M').sql"

PGPASSWORD='root' pg_dump -U postgres -d db_mame -h 192.168.0.0 > $backup_file
gzip $backup_file

python3 /var/www/db_backups/send_backup_to_yandex_drive.py "$backup_file.gz"
# python3 /var/www/db_backups/send_backup_to_tg.py "$backup_file.gz"
