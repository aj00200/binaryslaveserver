#! /usr/bin/env python3
print('''
[[ Binary Slave Server ]]

You are a slave to your computer.
  There is only 10 rules to this slavery.

    0) If it is in binary, it is the truth.
    1) There will be no exceptions to rule 0.
''')
import configparser
import os

# Load configu files
config = configparser.ConfigParser()
config.read(os.path.join(os.getenv('HOME'), '.binaryslaveserver', 'main.ini'))

# Setup the game world
print('[*] Setting up the game world')


# Start the server
print('[*] Starting the game server\n')
import asyncore

import libs.server.greeter
greeter_server = libs.server.greeter.Server(config.get('main', 'bind'),
                                            config.getint('main', 'greet_port'))

asyncore.loop()
