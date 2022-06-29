##
## PERSONAL PROJECT, 2022
## FUN
## File description:
## get_BTC
##

from colorama import Fore
import time
import secrets
from random import randint

continuing = True
btcval = 31643.79
wallet = 0.0
btc_total= 0.0

while True:
    if continuing == True:
        time.sleep(0.01)
        random_int = randint(0,2500)
        if random_int <= 1:
            random_btc = randint(1,100)/100
            print(Fore.WHITE + "> 0x" + secrets.token_hex(20) + Fore.GREEN + " > " + str(random_btc) + " BTC ($" + str("{:,}".format(round(btcval * random_btc, 2))) + ")")
            wallet += round(btcval * random_btc, 2)
            btc_total += random_btc
            answer = input("> Would you like to continue? (Y/N)")
            if answer.lower() == "y":
                continuing = True
            else:
                continuing = False
        else:
            print(Fore.WHITE + "> 0x" + secrets.token_hex(20) + Fore.RED + " > 0.00 BTC ($0.00)")
    else:
        print(Fore.WHITE + "> Thx for using me :)\n> You've collected " + Fore.GREEN + str(btc_total) + "BTC")
        print(Fore.WHITE + "> which mean " +  Fore.GREEN + str("{:,}".format(wallet)) + "$" + Fore.WHITE)
        break