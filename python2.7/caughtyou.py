import os
import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop

"""
$ python2.7 caughtyou.py
```
[Here is a tutorial](http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/)
teaching you how to setup a bot on Raspberry Pi. This simple bot does nothing but accepts two commands:
- `/roll` - reply with a random integer between 1 and 6, like rolling a dice.
- `/time` - reply with the current time, like a clock.
- `/pic - sends picture
"""

#file_count = 0

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command
    #file_count_two = file_count
    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/pic':
        path, dirs, files = os.walk("/home/pi/Desktop/cookie/client/images").next()
        # Sends a message to the chat
        bot.sendPhoto(chat_id, photo=open('./capture.jpg', 'rb'))

bot = telepot.Bot('  ')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
