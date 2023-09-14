from . import runner
import time
import sys
import shutil
import json
import pip
import os

Runner = runner.Runner

# FILE INFORMATION
__version__ = '2.0.0'
__author__ = '\x53\x61\x6e\x61\x75\x72 \x41\x73\x69\x66'
__date__ = '18.01.2023'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2023 ROC-X'
__email__ = 'rootofcyber@gmail.com'
__status__ = 'Published'

# COLOR_VALUE
BLUE = '\33[94m'
LIGHT_BLUE = '\033[94m'
RED = '\033[91m'
WHITE = '\33[97m'
YELLOW = '\33[93m'
GREEN = "\033[0;92m"
CYAN = "\033[96m"
END = '\033[0m'
BLACK = "\033[0;30m"

service_json = json.loads(open(os.path.join(os.path.dirname(__file__), 'services.json')).read())


# MAIN
class Services:
    S_LIST = ['\n', '8', '8', '8', '8', '8', '8', '8', 'b', '.', ' ', ' ', ' ', '.', 'd', '8', '8', '8', '8', '8', 'b',
              '.', ' ', ' ', ' ', '.', 'd', '8', '8', '8', '8', 'b', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Y', '8',
              '8', 'b', ' ', ' ', ' ', 'd', '8', '8', 'P', '\n', '8', '8', '8', ' ', ' ', ' ', 'Y', '8', '8', 'b', ' ',
              'd', '8', '8', 'P', '"', ' ', '"', 'Y', '8', '8', 'b', ' ', 'd', '8', '8', 'P', ' ', ' ', 'Y', '8', '8',
              'b', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Y', '8', '8', 'b', ' ', 'd', '8', '8', 'P', '\n', '8', '8', '8',
              ' ', ' ', ' ', ' ', '8', '8', '8', ' ', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', '8',
              '8', '8', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Y', '8', '8', 'o',
              '8', '8', 'P', ' ', ' ', '\n', '8', '8', '8', ' ', ' ', ' ', 'd', '8', '8', 'P', ' ', '8', '8', '8', ' ',
              ' ', ' ', ' ', ' ', '8', '8', '8', ' ', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', '8',
              '8', '8', '8', '8', ' ', ' ', 'Y', '8', '8', '8', 'P', ' ', ' ', ' ', '\n', '8', '8', '8', '8', '8', '8',
              '8', 'P', '"', ' ', ' ', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', '8', '8', '8', ' ',
              ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', '8', '8', '8', '8', '8', ' ', ' ', 'd', '8', '8', '8', 'b', ' ',
              ' ', ' ', '\n', '8', '8', '8', ' ', 'T', '8', '8', 'b', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', ' ', ' ',
              ' ', '8', '8', '8', ' ', '8', '8', '8', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ',
              ' ', ' ', 'd', '8', '8', '8', '8', '8', 'b', ' ', ' ', '\n', '8', '8', '8', ' ', ' ', 'T', '8', '8', 'b',
              ' ', ' ', 'Y', '8', '8', 'b', '.', ' ', '.', 'd', '8', '8', 'P', ' ', 'Y', '8', '8', 'b', ' ', ' ', 'd',
              '8', '8', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', '8', '8', 'P', ' ', 'Y', '8', '8', 'b', ' ', '\n',
              '8', '8', '8', ' ', ' ', ' ', 'T', '8', '8', 'b', ' ', ' ', '"', 'Y', '8', '8', '8', '8', '8', 'P', '"',
              ' ', ' ', ' ', '"', 'Y', '8', '8', '8', '8', 'P', '"', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', '8', '8',
              'P', ' ', ' ', ' ', 'Y', '8', '8', 'b']

    LOGO = ''.join(S_LIST)
    LINES = LOGO.split('\n')

    @staticmethod
    def install_requirements(packages: list):
        """
        Install requirements.
        :param packages: A list of packages to install.
        :return: None.
        """
        for package in packages:
            print(GREEN + f'Installing {package}...' + END)
            try:
                print(GREEN)
                if hasattr(pip, 'main'):
                    pip.main(['install', package])
                else:
                    # noinspection PyProtectedMember
                    pip._internal.main(['install', package])
                __import__(package)
                print(f"\n{GREEN}[+] {YELLOW}{package}{GREEN} installed.")
            except ModuleNotFoundError:
                print(f"\n{RED}[-] {YELLOW}{package}{RED} not installed.")
            except Exception:
                print(f"\n{RED}[-] {YELLOW}{package}{RED} not installed.")

    @staticmethod
    def check_requirements(packages: list):
        """
        Check requirements.
        :param packages: A list of packages to check.
        :return: None if all requirements are met, otherwise packages list that are not met.
        """
        not_met = []
        for package in packages:
            if isinstance(package, list):
                try:
                    __import__(package[0])
                except ModuleNotFoundError:
                    not_met.append(package[1])
            else:
                try:
                    __import__(package)
                except ModuleNotFoundError:
                    not_met.append(package)

        if not_met:
            return not_met
        else:
            return None

    @staticmethod
    def slow_print(text: str, speed: int = 0.05, skip_space: bool = False):
        """
        Print text slowly.
        :param text: Text to print.
        :param speed: Speed of printing.
        :param skip_space: Skip space after printing.
        :return: None.
        """
        if skip_space:
            for char in text:
                if char != ' ':
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(speed)
                else:
                    print(char, end='')
        else:
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(speed)

    @staticmethod
    def get_terminal_size():
        """
        Get terminal size.
        :return: Terminal size.
        """
        return shutil.get_terminal_size()

    @staticmethod
    def clear():
        """
        Clear terminal.
        :return: None.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def header(self, clear: bool = True, notice: str = None, notice_color: str = CYAN):
        """
        Print header.
        :param clear: Clear terminal. Default is True.
        :param notice: Notice to print. Default is None.
        :param notice_color: Notice color. Default is CYAN. 
        :return: None.
        """
        if clear:
            self.clear()
        width = self.get_terminal_size().columns
        print(RED, end='')
        for line in self.LINES:
            print(line.center(width))
        print(CYAN)
        print(f"Developed By : {__author__}".center(width))
        print(GREEN)
        print(f"Version : {__version__}".center(width))
        print("\n" + YELLOW + "".center(width, "=") + notice_color)
        if notice:
            notice = " " + notice + " "
            print(notice.center(width, "="))
        print(YELLOW + "".center(width, "=") + "\n" + END)

    @staticmethod
    def menu():
        """
        Print menu.
        :return: None.
        """
        tools_ = service_json['tools']
        for num_, tool_ in enumerate(tools_):
            print(CYAN + f"\n [{num_ + 1}] {tool_['name']}", end='\n')
        return tools_

    def check_update(self):
        """
        Check for updates.
        :return: None.
        """
        try:
            import requests
        except:
            pass
        try:
            resp_ = requests.get('https://raw.githubusercontent.com/SanaurAsif/ROCX/pro/VERSION')
            if resp_.text != __version__:
                self.header(notice="Tools Updating", notice_color=YELLOW)
                os.system('pip install git+https://github.com/SanaurAsif/ROCX')
                sys.exit(f"{RED} [-] {YELLOW}Please run the tool again.{END}")
        except:
            self.header(notice="Something Went Wrong", notice_color=RED)
            sys.exit(f"{RED} [-] {YELLOW}Please run the tool again.{END}")

    def run(self, tool_: dict):
        """
        Run tool.
        :param tool_: Tool to run.
        :return: None.
        """
        packages = tool_['dependencies']
        to_install = self.check_requirements(packages)
        if to_install:
            self.install_requirements(to_install)
            self.header()
        not_met = self.check_requirements(packages)
        if not_met:
            self.header(notice="Please install the requirements manually", notice_color=RED)
            sys.exit(f"\n{RED} [-] {YELLOW}{not_met}{RED} are not installed.\n\n")

        runner_ = Runner(tool_['file'])
        result = runner_.run()
        if result:
            input(f"\n{CYAN} [+] {CYAN}Press Enter to continue...{END}")
            self.header()
        else:
            sys.exit(f"\n{RED} [-] This tool is not for you, Kid!{END}")
