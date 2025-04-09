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

def run_test():

    target_driver = webdriver.Chrome()


    target_driver.get("https://www.target.com/p/pokemon-scarlet-violet-s3-5-booster-bundle-box/-/A-88897904#lnk=sametab")

    # Loop to check if item is in stock
    while True:

        target_add_to_cart_button = target_driver.find_element(By.ID, "addToCartButtonOrTextIdFor88897904")
        
        if "disabled" in target_add_to_cart_button.get_attribute('class'):
            print("Item is currently out of stock")
            time.sleep(60)
        else:
            print("Item is in stock!")
            
            target_add_to_cart_button.click()
            
            view_and_checkout_target_button = target_driver.find_element(By.XPATH, '//a[@class="styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButtonSecondary__iSf2I"]')
            view_and_checkout_target_button.click()
        
            sign_in__checkout_target_button = target_driver.find_element(By.XPATH, '//button[@class="styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButton__XOOOH styles_md__Yc3tr styles_filleddefault__7QnWt"]')
            sign_in__checkout_target_button.click()
            
            target_username = target_driver.find_element(By.ID, "username")
            target_username.send_keys("Gach56@hotmail.com")
            
            target_username = target_driver.find_element(By.ID, "password")
            target_username.send_keys("Waterh56$")
            
            view_and_checkout_target_button = target_driver.find_element(By.XPATH, '//button[@class="styles_ndsBaseButton__W8Gl7 styles_lg___H2IL styles_lgGap__bPB7P styles_fullWidth__3XX6f styles_ndsButtonPrimary__tqtKH sc-609faf1c-4 gwYVYs"]')
            view_and_checkout_target_button.click()
            
            target_place_order_button = target_driver.find_element(By.XPATH, '//button[@class="styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButton__XOOOH styles_md__Yc3tr styles_filleddefault__7QnWt"]')
            target_place_order_button.click()
            
            target_username = target_driver.find_element(By.ID, "enter-cvv")
            target_username.send_keys("645")
            target_place_order_button = target_driver.find_element(By.XPATH, '//button[@class="styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButton__XOOOH styles_md__Yc3tr styles_filleddefault__7QnWt h-margin-t-default"]')
            target_place_order_button.click()
            break
            
        
    target_driver.quit()

if __name__ == "__main__":
    run_test()

