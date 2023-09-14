from . import main as rx
import sys


def main_rocx(args=None):
    # COLOR_VALUE

    RED = rx.RED
    YELLOW = rx.YELLOW

    # MAIN

    rocx = rx.Services()

    rocx.header()
    packages = ["requests"]
    to_install = rocx.check_requirements(packages)

    if to_install:
        rocx.install_requirements(to_install)
        rocx.header()

    not_met = rocx.check_requirements(packages)

    if not_met:
        rocx.header(notice="Please install the requirements manually", notice_color=RED)
        sys.exit(f"\n{RED}[-] {YELLOW}{not_met}{RED} are not installed.\n\n")

    rocx.header()
    rocx.check_update()

    while True:
        menu = rocx.menu()
        print(YELLOW)
        select = input(" >>> Select any tool : ")
        try:
            num = int(select)
            if len(menu) < num or 1 > num:
                rocx.header(notice="Wrong Option Selected", notice_color=RED)
            else:
                rocx.header()
                tool = menu[num - 1]
                rocx.run(tool)
        except ValueError:
            rocx.header(notice="Wrong Option Selected", notice_color=RED)
