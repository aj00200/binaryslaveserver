#! /usr/bin/env python3
print('''
[[ Binary Slave Server ]]

You are a slave to your computer.
  There is only 10 rules to this slavery.

    0) If it is in binary, it is the truth.
    1) There will be no exceptions to rule 0.
''')

# Setup the game world
print('[*] Setting up the game world')


# Start the server
print('[*] Starting the game server')
import asyncore

import libs.server.greeter
greeter_server = libs.server.greeter.Server('localhost', 31337)

asyncore.loop()
