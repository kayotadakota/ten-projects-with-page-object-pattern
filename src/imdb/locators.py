from selenium.webdriver.common.by import By


class HomePageLocators(object):

    facebook = (By.CSS_SELECTOR, 'a[title="Facebook"]')
    instagram = (By.CSS_SELECTOR, 'a[title="Instagram"]')
    twitch = (By.CSS_SELECTOR, 'a[title="Twitch"]')
    twitter = (By.CSS_SELECTOR, 'a[title="Twitter"]')
    youtube = (By.CSS_SELECTOR, 'a[title="Youtube"]')
    
