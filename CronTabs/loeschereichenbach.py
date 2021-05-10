import os, shutil

zieldir='/var/www/vhosts/rjs.de/rb.autoren-net.de/thumb/thumb/' 
try:
    shutil.rmtree(zieldir)
except:
    pass
try:
    os.mkdir(zieldir)
except:
    pass

