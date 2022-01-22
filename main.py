# Token Checker by vivid

import requests, ctypes, colorama

colorama.init(convert=True)

def check_tokens():
 valid = 0
 invalid = 0
 ctypes.windll.kernel32.SetConsoleTitleW(f'911 Token Checker | {valid} Valid | {invalid} Invalid')

 with open('invalid.txt', 'r') as tokens:
   for line in tokens:
    token = line.rstrip('\n')
    r = requests.get('https://discord.com/api/v6/auth/login', headers={  'Authorization': token   })
    if r.status_code == 200:
     print(f"{colorama.Fore.GREEN}{token} is valid")
     valid += valid + 1
    else:
     print(f"{colorama.Fore.RED}{token} is invalid")
     invalid += invalid + 1



check_tokens()
