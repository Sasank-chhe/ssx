import os, platform
try:
   import requests
except:
   os.system('pip install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from sx import mengecek_
    mengecek_()
elif bit == '32bit':
    from sx import mengeck_
    mengeck_()
