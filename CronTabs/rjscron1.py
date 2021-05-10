from crontab import CronTab
cron = CronTab(user='root')
job = cron.new(command='python3 /var/www/vhosts/rjs.de/rb.autoren-net.de/thumb/copierereichenbach.py')
job.minute.every(2)
job.hour.during(8,19)
job = cron.new(command='python3 /var/www/vhosts/rjs.de/rb.autoren-net.de/thumb/loeschereichenbach.py')
job.day.on(4)
cron.write()