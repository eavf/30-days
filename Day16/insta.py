
from urllib.parse  import urlparse
import time
import requests
import os
from _kluce import INSTA_USERNAME, INSTA_PASSWORD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# import getpass
# my_password = getpass.getpass("What is your password?\n")
# print (my_password)

c = Options()
#passing headless parameter
#c.add_argument('headless')
c.add_argument('--log-level=3')
prefs = {"profile.default_content_setting_values.media_stream_mic" : 1,
         "profile.default_content_setting_values.notifications": 2,
         "profile.default_content_setting_values.media_stream_camera": 1}
#c.add_experimental_option("prefs",prefs)
c.add_experimental_option("excludeSwitches", ["enable-automation"],)
c.add_argument("--user-data-dir=C:\\Users\\vovo\\AppData\\Local\\Google\\Chrome\\User Data\\Default")


browser = webdriver.Chrome(options=c)
url = "https://www.instagram.com"
browser.get(url)

time.sleep(5)
"""
<input aria-label="Telefónne číslo, používateľské meno alebo e-mailová adresa" 
aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75" 

name="username"

type="text" class="_2hvTZ pexuQ zyHYP" value="">
"""
username_el = browser.find_element(By.NAME, "username")
username_el.send_keys(INSTA_USERNAME)

"""
<input aria-label="Heslo" 
aria-required="true" autocapitalize="off" autocorrect="off" 

name="password" 

type="password" class="_2hvTZ pexuQ zyHYP" value="">
"""
password_el = browser.find_element(By.NAME, "password")
password_el.send_keys(INSTA_PASSWORD)

"""
<div class="             qF0y9          Igw0E     IwRSH      eGOV_       acqo5   _4EzTm    bkEs3                          CovQj                  jKUp7          DhRcB                                                    ">
    <button class="sqdOP  L3NKy   y3zKF     " disabled="" type="submit">
        <div class="             qF0y9          Igw0E     IwRSH      eGOV_       acqo5   _4EzTm                                                                                                              ">
            Prihlásiť sa
        </div>
    </button>
</div>

"""
submit_btn_el = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
time.sleep(2)
submit_btn_el.click()

#body_el = browser.find_element(By.CSS_SELECTOR, "body")
#html_text = body_el.get_attribute("innerHTML")
#print(html_text)

"""
<div class="_aacl _aaco _aacw _adda _aad6 _aade">S’abonner</div>

"""
# xpath
#my_button_xpath = "//button"
#browser.find_elements(By.XPATH, my_button_xpath)
def click_to_follow(browser):
    #my_follow_bttn_xpath = "//a[contains(text(), 'aboner')][not(contains(text(), 'aboné'))]"
    #my_follow_bttn_xpath = "//button[contains(text(), 'aboner')][not(contains(text(), 'aboné'))]"
    my_follow_bttn_xpath = "//*[contains(text(), 'Sledova')][not(contains(text(), 'Sledované'))]"
    follow_btn_elements = browser.find_elements(By.XPATH, my_follow_bttn_xpath)

    for btn in follow_btn_elements:
        time.sleep(2)
        try: 
            btn.click()
        except:
            pass


#new_user_url = "https://www.instagram.com/angelinajolie__queen/"
time.sleep(5)
print("natahujem the rock\n")
the_rock_url = "https://www.instagram.com/therock/"
browser.get (the_rock_url)

"""
<a class="qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv rse6dlih s5oniofx m8h3af8h l7ghb35v
kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq _a6hd" 
href="/p/ChSfjptpdjx/" 
role="link" tabindex="0"><div class="_aagu"><div class="_aagv"><img alt="Monday. 
"""

time.sleep(5)
post_url_pattern = "https://www.instagram.com/therock/p/<post-slug-id>"
post_xpath_string = "//a[contains(@href, '/p/')]"
post_links = browser.find_elements(By.XPATH, post_xpath_string)
print("Natiahol som všetky linky .....\n")
time.sleep(5)
post_link = None
if len(post_links)>0:
    post_link = post_links[1].get_attribute("href")
    print ("som v prvom if a tlasim yvbnranu linku : ", post_link)
    print ("som v prvom if a tlasim prvy element zoznamu : ", post_links[0].get_attribute("href"))
if post_link != None:
    print (post_link, "\n")
    browser.get(post_link)

print ("End......\n")

time.sleep(3)
video_els = browser.find_element(By.XPATH, ("//video"))
images_els = browser.find_elements(By.XPATH, ("//img"))

base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

def scrape_and_save(elements):
    for el in elements:
        #print (el.get_attribute('src'))
        url = el.get_attribute('src')
        base_url = urlparse(url).path
        filename = os.path.basename(base_url)
        file_path =os.path.join(data_dir, filename)
        if os.path.exists(file_path):
            continue
        with requests.get(url, stream=True) as r:
            try:
                r.raise_for_status()
            except:
                continue
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content():
                    if chunk:
                        f.write(chunk)
    
#scrape_and_save(images_els)

#Video nefunguje lebo to zmenili a je posklytované ako blob....
#scrape_and_save(videos_el)


"""
LONG TERM GOAL:
Use machine learniong to clasify the post's 
image or video 
and then comment in a relevant fasion
"""

"""
<textarea aria-label="Pridať komentár..." placeholder="Pridať komentár..." 
class="_ablz _aaoc" autocomplete="off" autocorrect="off"></textarea>
"""
def automate_comment(browser, content="That is cool!!!"):
    time.sleep(3)
    comment_xpath_string = "//textarea[contains(@placeholder, 'Pridať komentár...')]"
    comment_el = browser.find_element(By.XPATH, comment_xpath_string)
    print("Som v def automate : ", comment_el)
    time.sleep(3)
    comment_el.send_keys(content)

    # a teraz postnuť button

    """
    <button class="_acan _acao _acas" type="submit">
        <div class="_aacl _aaco _aacw _adda _aad0 _aad6 _aade">
            Uverejniť
        </div>
    </button>
    """
    time.sleep(5)
    submit_btns = "button[type='submit']"
    submit_btns = browser.find_elements(By.CSS_SELECTOR, submit_btns)

    for btn in submit_btns:
        try:
            btn.click()
        except:
            pass


automate_comment(browser, content = "I am going to buy this one!")