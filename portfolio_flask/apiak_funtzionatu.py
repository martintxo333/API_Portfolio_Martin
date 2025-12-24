import requests
from colorama import Fore, init

init(autoreset=True)

url = "http://127.0.0.1:5000/api/profile"
response = requests.get(url)

data = response.json()

print(Fore.BLUE + str(data))
