import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
# Avoiding detection
options.add_argument('--disable-blink-features=AutomationControlled')

target_driver = webdriver.Chrome()


target_driver.get("https://www.target.com/p/pokemon-scarlet-violet-s3-5-booster-bundle-box/-/A-88897904#lnk=sametab")


# Click the button using class name
try:
    
    target_add_to_cart_button = target_driver.find_element(By.ID, "addToCartButtonOrTextIdFor88897904")
    target_add_to_cart_button.click()
    
    view_and_checkout_target_button = target_driver.find_element(By.XPATH, '//a[@class="styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButtonSecondary__iSf2I"]')
    view_and_checkout_target_button.click()
   
    sign_in__checkout_target_button = target_driver.find_element(By.XPATH, '//button[@class="styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButton__XOOOH styles_md__Yc3tr styles_filleddefault__7QnWt"]')
    sign_in__checkout_target_button.click()
    
    target_username = target_driver.find_element(By.ID, "username")
    target_username.send_keys("Enter username")
    
    target_username = target_driver.find_element(By.ID, "password")
    target_username.send_keys("Enter password")
    
    view_and_checkout_target_button = target_driver.find_element(By.XPATH, '//button[@class="styles_ndsBaseButton__W8Gl7 styles_lg___H2IL styles_lgGap__bPB7P styles_fullWidth__3XX6f styles_ndsButtonPrimary__tqtKH sc-609faf1c-4 gwYVYs"]')
    view_and_checkout_target_button.click()
    
    target_place_order_button = target_driver.find_element(By.XPATH, '//button[@class="styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButton__XOOOH styles_md__Yc3tr styles_filleddefault__7QnWt"]')
    target_place_order_button.click()
    
    target_username = target_driver.find_element(By.ID, "enter-cvv")
    target_username.send_keys("CVV")
    target_place_order_button = target_driver.find_element(By.XPATH, '//button[@class="styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButton__XOOOH styles_md__Yc3tr styles_filleddefault__7QnWt h-margin-t-default"]')
    target_place_order_button.click()
    
except:
    target_button = target_driver.find_element(By.CLASS_NAME, ".styles_ndsBaseButton__W8Gl7 styles_sm__4HXZ8 styles_smGap__J2VD0 styles_ndsButtonPrimary__tqtKH.styles_ndsBaseButton__W8Gl7 styles_sm__4HXZ8 styles_smGap__J2VD0 styles_ndsButtonPrimary__tqtKH")
    target_button.click()
    #walmart_button = walmart_driver.find_element(By.CLASS_NAME, "w_hhLG w_8nsR w_jDfj pointer bn sans-serif b ph2 flex items-center justify-center w-auto shadow-1")
    #walmart_button.click()



