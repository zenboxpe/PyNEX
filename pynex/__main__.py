import argparse
import os
import sys

from logzero import logger

from pynex import __version__
from pynex.server import Server

PATH = os.getcwd() + "/"
DATA_PATH = os.getcwd() + "/"
PLUGIN_PATH = DATA_PATH + "plugins"

def test_command(args):
    print('test_command invoke')


def main():

    # parser = argparse.ArgumentParser(
    #     description="A Minecraft PE server software written in Python.",
    #     epilog="""example usage:
    #     Start server by doing: pyromine serve
    #     """,
    #     formatter_class=argparse.RawDescriptionHelpFormatter
    # )
    # parser.add_argument('--version', action='version', version='pyromine %s' % __version__)
    #
    # subparsers = parser.add_subparsers()
    # # create the parser for the "test" command
    # parser_rec = subparsers.add_parser('test', help='Test terminal session')
    # parser_rec.set_defaults(func=test_command)
    #
    # args = parser.parse_args()
    #
    # if hasattr(args, 'func'):
    #     command = args.func(args)
    # else:
    try:
        Server(DATA_PATH, PLUGIN_PATH)
    except Exception as e:
        logger.error(e)

    logger.info("Stopping other threads")




if __name__ == '__main__':
    main()
