from . import main_rocx
import sys


def run_cli(args: list = None):
    if args is None:
        args = sys.argv[1:]
    return main_rocx(args)
