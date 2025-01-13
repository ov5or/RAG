
from turtle import delay
from httpx import post, Client
from json import load
import os, sys
from httpx import Client, post
from urllib import request
from playwright.sync_api import sync_playwright
from httpx import Client
from secrets import token_hex
from random import randint,choice
import pystyle
from pystyle import Colors, Colorate
from time import sleep
from json import loads
from re import search
import time

# -- config zone --#
saverb=open("robloxgen.txt","a+",encoding="utf-8")
configrb=load(open("configroblox.json","r",encoding="utf8"))
userrb = configrb["names"]
passwordrb = configrb["password"]
webhookroblox = configrb["webhook"]
ranname = configrb["random-name"]

# -- color zone --#

def rb(text):
        return (Colorate.Horizontal(Colors.rainbow,text))

# -- cd zone --#
delayreg = "60"
def countdown(t):  
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Register In : {timer}", end="\r")
        time.sleep(1)
        t -= 1


# -- mian zone --#

sess = Client(headers={"user-agent": "Mozilla/5.0"},timeout=300)
def main():
    username = f"ov5orAltGen{randint(10000, 99999)}{''.join([choice('abcdefghijklmnopqrstuvwxyz') for _ in range(4)])}"
    password = f"{passwordrb}@_{token_hex(5)}"
    cookie_roblox=""
    with sync_playwright() as p:
        Browser=p.firefox.launch(headless=False)
        BContext=Browser.new_context(viewport={"height":700,"width":500})
        Page=BContext.new_page()
        Page.goto("https://www.roblox.com", timeout=60000,wait_until="networkidle")
        print(rb("Start Register"))
        Page.select_option('[id="MonthDropdown"]',label="April")
        print(rb("Select Month"))
        try:
            Page.select_option('[name="birthdayDay"]', label="25", timeout=5000, force=True)
            print(rb("Select Day"))
        except:pass
        Page.select_option('[id="YearDropdown"]',label=str(randint(1995,2003)))
        print(rb("Select Year"))
        Page.type('[id="signup-username"]',username)
        print(rb("Tpye Username"))
        Page.type('[id="signup-password"]',password)
        print(rb("Type Password"))
        Page.click('[id="MaleButton"]')
        print(rb("Select to Male"))
        sleep(1.5)
        Page.evaluate("""document.querySelector('[id="signup-button"]').click()""")
        print(rb("Click"))
        sleep(5)
        Page.wait_for_load_state("networkidle")
        try: 
            Page.wait_for_selector("iframe",timeout=5000) 
            input("got captcha, Please pick picture from captcha , and pess enter") # solve funcaptcha
        except:pass # pass
        try:
            for cookie_roblox in filter(lambda data: data["name"] == ".ROBLOSECURITY",BContext.cookies()):
                # print(cookie_roblox)
                saverb.write(f"GEN :  {username} |-| {password} |-| {cookie_roblox['value']}\n")
                print(rb("Success!"))
                post(webhookroblox,json={"content": "🚗","embeds": [{"title": f"ROBLOX GEN","description":f"> :white_check_mark:Status : success!\n> :speech_balloon:Name : {username}\n> :closed_lock_with_key:PassWord : ||{password}||\n> :cookie:Cookie : ||{cookie_roblox['value']}||","color": 2752256}]})
                print(rb("New Register in 60 Seconeds"))
                # post(webhookroblox,json={"content": None,"embeds": [{"title": f"ROBLOX GEN","description":f"> :white_check_mark:Status : waiting. . .\n> wait 60 secondes next register","color": 2752256}]})
                saverb.close()
        except:
            print("Error, Account don't have cookies!")
 
def loop():
    if __name__ == "__main__":
        main()
        countdown(int(delayreg)) 
loop()

if __name__ == "__main__":
    main()
    countdown(int(delayreg))
