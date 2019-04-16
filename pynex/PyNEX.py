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
import pocketmine\utils\MainLogger;
import pocketmine\utils\ServerKiller;
import pocketmine\utils\Terminal;
import pocketmine\utils\Timezone;
import pocketmine\utils\Utils;
import pocketmine\utils\VersionString;
import pocketmine\wizard\SetupWizard;


from pynex.core.server import Server

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
