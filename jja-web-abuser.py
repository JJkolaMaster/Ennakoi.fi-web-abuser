import selenium
import time
import random
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# JJa Web-Abuser 🄯
# Jotta ohjelma toimii asenna chrome driveri ja juuri sama driver versio, kuin omassa chromessa.

# Loopataan esim. 20 kertaa
for i in range(20):
    # Valitaan selain
    driver = webdriver.Chrome()
    
    # Osoite minne mennään /// *** Korvaa "erääseen-sivustoon" oikein, you know ;)
    driver.get("https://erääseen-sivustoon/create/assessment")
    print(driver.title)
    
    # Ilmoittajan nimi
    reporter = driver.find_element_by_name("name")
    reporter.send_keys("Oma nimi")
    
    # Ilmoittajan työnantaja
    employer = driver.find_element_by_name("company")
    employer.send_keys("Firman nimi")
    
    # Ilmoittajan sähköposti
    reporter_email = driver.find_element_by_name("email")
    reporter_email.send_keys("Oma sähköpostiosoite")
    
    # Esimiehen sähköposti
    boss_email = driver.find_element_by_name("emailBoss")
    boss_email.send_keys("Esimiehen sähköposti")
    
    # Lista sepityksiä /// ***Tee omat sepityksesi***
    bs_list = [
        "esimerkki 1",
        "esimerkki 2",
        "esimerkki 3"
        ]
    
    # Arvotaan selitys
    random.shuffle(bs_list)
    bs_story = bs_list[1]
    
    # Liitetään arvottu työ
    description = driver.find_element_by_id("inputdescription")
    description.send_keys(bs_story)
    
    # Rastitaan boxit "Kiire" ja "Ohjeet" /// *** Samalla tyylillä saadaan lisään laatikoita ruksittua tässä selaimen laajennus Selenium IDE auttaa *** 
    box1 = driver.find_element_by_css_selector(".span6:nth-child(1) > .checkbox:nth-child(64) > .checkbox")
    box1.send_keys(Keys.SPACE)
    box2 = driver.find_element_by_css_selector(".span6:nth-child(2) > .checkbox:nth-child(7) > .checkbox")
    box2.send_keys(Keys.SPACE)
    
    # Valitaan Firma --> Alue --> Osasto /// *** Muuta nämä jotta ohjelma toimisi ***
    own1 = driver.find_element_by_link_text("Valitse")
    own1.send_keys(Keys.ENTER)
    own2 = driver.find_element_by_link_text("Firma")
    own2.send_keys(Keys.ENTER)
    own3 = driver.find_element_by_link_text("Valitse")
    own3.send_keys(Keys.ENTER)
    own4 = driver.find_element_by_link_text("Alue")
    own4.send_keys(Keys.ENTER)
    own5 = driver.find_element_by_link_text("Valitse")
    own5.send_keys(Keys.ENTER)
    own6 = driver.find_element_by_link_text("Osasto")
    own6.send_keys(Keys.ENTER)
    
    # Lähetetään riskien arviointi
    print(bs_story)
    sendButton = driver.find_element_by_id("send")
    sendButton.send_keys(Keys.ENTER)
    
    # Lyödään Chrome kiinni
    driver.close()
    driver.quit()
