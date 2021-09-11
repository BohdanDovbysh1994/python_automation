from argparse import ArgumentParser

# example 1
from browsers.chrome import Chrome
from browsers.firefox import Firefox

parser = ArgumentParser()
parser.add_argument('--browser', help='name of browser', default="chrome")
args = parser.parse_args()

if args.browser == "chrome":
    browser = Chrome()
elif args.browser == "firefox":
    browser = Firefox()
else:
    raise Exception("Not supported browser")

print(browser)