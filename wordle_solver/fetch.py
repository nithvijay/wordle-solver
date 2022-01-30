import json

from selenium import webdriver

def get_solution():
    try:   
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')     
        driver = webdriver.Chrome(options=options)

        driver.get("https://www.powerlanguage.co.uk/wordle/")
        data = driver.execute_script("return window.localStorage.getItem(arguments[0]);", "gameState")
        return json.loads(data)["solution"]
    except Exception:
        return False
    finally:
        driver.quit()
