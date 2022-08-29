import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()    #Firefox()......

url = 'https://google.com'
browser.get(url)

"""
Najlepšie je odkazovať sa na name attribute, lebo ten je naviazaný často na backend a 
nie je jednoduché ho zzmeniť

<input type='text' class = '' id = '' name = '??' />
<textarea name = '??' > <textarea>

Case Google:
<input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" 
type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" 
autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" 
title="Hľadať" value="" aria-label="Hľadať" data-ved="0ahUKEwjIvuSojND5AhUcXvEDHQijDM8Q39UDCAQ">

z uvedeného vyplýva, že všetko čo potrebujeme je nasledovné:
<input name="q" type="text">

"""

time.sleep(5)
name = 'q'
search_el = browser.find_element(By.CSS_SELECTOR, '[name="q"]')
print (search_el)

search_el.send_keys("Selenium python")


"""
<input type='submit' />
<button type='submit' />
<form></form>
Google case

<input class="gNO89b" value="Hľadať Googlom" aria-label="Hľadať Googlom" 
name="btnK" role="button" tabindex="0" type="submit" 
data-ved="0ahUKEwiug9SLkdD5AhU7g84BHbFpAyoQ4dUDCAs">

Pre naše účely je dôležité
<input type="submit" >

"""

submit_btn = browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
print ("Submit button coord.:  ---- ", submit_btn.get_attribute('name'))

time.sleep(2)
submit_btn.click()




