import datetime,shutil

zeitstempel = datetime.datetime.now().timestamp()
zieldat='/var/www/vhosts/rjs.de/rb.autoren-net.de/thumb/thumb/reichenbach' + str(zeitstempel) + '.jpg' 
try:
    shutil.copy2('/var/www/vhosts/rjs.de/rb.autoren-net.de/thumb/reichenbach.jpg', zieldat)
except:
    pass