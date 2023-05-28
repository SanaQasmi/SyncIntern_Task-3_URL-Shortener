import pyshorteners
import colorama
from colorama import Fore, Style

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

colorama.init()
long_url = input(Fore.RED + "Enter The URL To Shorten: " + Fore.RESET)
short_url = shorten_url(long_url)

print(Style.BRIGHT+Fore.BLUE +"The Shorten URL Are:-", short_url)
colorama.deinit()


#Python3 URL_Shortener_Sana_Qasmi