#####################################
#  _____       _   _ ________   __  #
# |  __ \     | \ | |  ___ \ \ / /  #
# | |__) |   _|  \| | |__   \ V /   #
# |  ___/ | | | . ` |  __|   > <    #
# | |   | |_| | |\  | |____ / . \   #
# |_|    \__, |_| \_|______/_/ \_\  #
#         __/ |MCBE Server Software #
#        |___/                      #
#####################################
import logging
import socket
import sys
import threading
import pynex\utils\MainLogger;
import pynex\utils\ServerKiller;
import pynex\utils\Terminal;
import pynex\utils\Timezone;
import pynex\utils\Utils;
import pynex\utils\VersionString;
import pynex\wizard\SetupWizard;


from pynex.server import Server

ascii_pynex = """

 _____       _   _ ________   __ 
|  __ \     | \ | |  ___ \ \ / / 
| |__) |   _|  \| | |__   \ V / 
|  ___/ | | | . ` |  __|   > <   
| |   | |_| | |\  | |____ / . \ 
|_|    \__, |_| \_|______/_/ \_\ 
        __/ |MCBE Server Software
       |___/
"""

GIT_INFO = None
VERSION = "0.1 indev"
API_VERSION = "1.0.0"
CODENAME = "PyNEX"
MINECRAFT_VERSION = None
MINECRAFT_VERSION_NETWORK = None
PATH = None
DATA_PATH = None
PLUGIN_PATH = None
START_TIME = None
ANSI = True
TITLE = False
short_title = False
DEBUG = 1

def critical_error(massage):
    print("[ERROR]", massage)
    pass

   massage = 
