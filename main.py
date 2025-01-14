from httpx import post, Client
from json import load
from playwright.sync_api import sync_playwright
from secrets import token_hex
from random import randint, choice
from pystyle import Colors, Colorate
from time import sleep
import threading

# -- Config Zone --#
saverb = open("robloxgen.txt", "a+", encoding="utf-8")
configrb = load(open("configroblox.json", "r", encoding="utf8"))
userrb = configrb["names"]
passwordrb = configrb["password"]
webhookroblox = configrb["webhook"]

# -- Color Zone --#
def rb(text):
    return Colorate.Horizontal(Colors.rainbow, text)

# -- Main Function --#
def main(instance_id):
    username = f"ov5orAltGen{randint(10000, 99999)}{''.join([choice('abcdefghijklmnopqrstuvwxyz') for _ in range(4)])}"
    password = f"{passwordrb}@_{token_hex(5)}"

    with sync_playwright() as p:
        print(rb(f"Launching instance {instance_id}"))
        # Launch Google Chrome in normal mode
        browser = p.chromium.launch(channel="chrome", headless=False)  # Google Chrome
        context = browser.new_context()  # Normal browsing session
        page = context.new_page()
        page.goto("https://www.roblox.com", timeout=60000, wait_until="networkidle")
        print(rb(f"Instance {instance_id}: Start Register"))
        
        # Fill the form
        page.select_option('[id="MonthDropdown"]', label="April")
        print(rb(f"Instance {instance_id}: Select Month"))
        try:
            page.select_option('[name="birthdayDay"]', label="25", timeout=5000, force=True)
            print(rb(f"Instance {instance_id}: Select Day"))
        except:
            pass
        page.select_option('[id="YearDropdown"]', label=str(randint(1995, 2003)))
        print(rb(f"Instance {instance_id}: Select Year"))
        page.type('[id="signup-username"]', username)
        print(rb(f"Instance {instance_id}: Type Username"))
        page.type('[id="signup-password"]', password)
        print(rb(f"Instance {instance_id}: Type Password"))
        page.click('[id="MaleButton"]')
        print(rb(f"Instance {instance_id}: Select Male"))
        sleep(1.5)
        page.evaluate("""document.querySelector('[id="signup-button"]').click()""")
        print(rb(f"Instance {instance_id}: Click Signup"))
        
        # Wait for potential CAPTCHA
        try:
            page.wait_for_selector("iframe", timeout=5000)
            input(f"Instance {instance_id}: Solve CAPTCHA, then press Enter to continue.")
        except:
            pass
        
        # Save cookies
        try:
            for cookie_roblox in filter(lambda data: data["name"] == ".ROBLOSECURITY", context.cookies()):
                saverb.write(f"GEN :  {username} |-| {password} |-| {cookie_roblox['value']}\n")
                print(rb(f"Instance {instance_id}: Success!"))
                
                # Print the username and password for successful account creation
                print(f"Account Created Successfully!\nUsername: {username}\nPassword: {password}")
                
                post(webhookroblox, json={
                    "content": "🚗",
                    "embeds": [{
                        "title": f"ROBLOX GEN - Instance {instance_id}",
                        "description": f"> :white_check_mark:Status : success!\n> :speech_balloon:Name : {username}\n> :closed_lock_with_key:PassWord : ||{password}||\n> :cookie:Cookie : ||{cookie_roblox['value']}||",
                        "color": 2752256
                    }]
                })
                print(rb(f"Instance {instance_id}: Registered successfully"))
                saverb.close()
        except:
            print(f"Instance {instance_id}: Error, account doesn't have cookies!")
        
        # Keep the browser open after successful registration
        input(f"Instance {instance_id}: Registration complete. Press Enter to close browser.")
        browser.close()

# Launch 5 instances in parallel
def launch_multiple_instances():
    max_instances = 5
    threads = []
    for i in range(1, max_instances + 1):  # Launch up to 5 instances
        thread = threading.Thread(target=main, args=(i,))
        thread.start()
        threads.append(thread)
        sleep(1)  # Add slight delay to prevent launching all at once

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    launch_multiple_instances()
