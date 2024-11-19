# What is it?
#### This is a small program writing on python, which may running from sh script for making dumps for your postgres databases, sending this dumps to telegram chat, deleting this dumps from disk after sending or errror occured.

# Usage
#### 1. Create a .env file (as in the example with .env.example).
#### 2. Edit the paths in the sh and py files depending on the path in which you have located the directory. (Skip the point if the git clone was made in /var/www/db_backups).
#### 3. Add running command for sh file via cron or something else, for example crontab task with log file may be seems like that.
```crontab
0 3 * * * /var/www/db_backups/db_backup.sh >> /var/www/db_backups/logs.log 2>&1
```
