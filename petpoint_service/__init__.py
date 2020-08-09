from selenium import webdriver
import chromedriver_autoinstaller
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import os

ORG_ID = os.getenv('ORG', None)
NAME = os.getenv('NAME', None)
PW = os.getenv('PW', None)

if None in (ORG_ID, NAME, PW):
    raise Exception('Missing ENV!')

SELECTORS = {
    'Nav[Edit]': '#ctl00_MenuPP > ul > li:nth-child(3) > a',
    'Nav[Animal]': '#ctl00_MenuPP > ul > li:nth-child(3) > div > ul > li.rmItem.rmFirst > a',
    'search_input': '#cphSearchArea_ctrlAnimal_ctrlAnimalSearch_txtFirstCriteria',
    'find_button': '#cphSearchArea_ctrlAnimal_ctrlAnimalSearch_btnFind',
    'Animal[Name]': '#cphSearchArea_ctrlAnimal_ctrlAnimal_txtName',
    'Animal[Type]': '#cphSearchArea_ctrlAnimal_ctrlAnimal_ddlAnimalType',
    'Animal[Breed]:': '#ctl00_cphSearchArea_ctrlAnimal_ctrlAnimal_ddlPrimaryBreed',
    'Animal[Colour1]': '#cphSearchArea_ctrlAnimal_ctrlAnimal_ddlPrimaryColor',
    'Animal[Colour2]': '#cphSearchArea_ctrlAnimal_ctrlAnimal_ddlSecondaryColor',
    'Animal[Location]': '#cphSearchArea_ctrlAnimal_ctrlAnimal_ctrlStageLocation_ddlLocationID',
    'Animal[Img1]': '#cphSearchArea_ctrlAnimal_ctrlAnimal_imgAnimalPhoto1'
}


options = Options()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

def format_results(d: dict):
    formatted_results = {}

    for (key, value) in d.items():
        if key == 'colour1' or key == 'colour2':
            continue
        formatted_results[key] = value.replace('-- Select --', '< EMPTY >')

    color = ''
    if d['colour1'] != '-- Select --':
        color += d['colour1']

    if d['colour2'] != '-- Select --':
        if color != '':
            color += ' / '
        color += d['colour2']

    formatted_results['color'] = color

    return formatted_results

def get_animal_details(anumber):
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://sms.petpoint.com/sms3/forms/signinout.aspx')

    shelter_id_input = driver.find_element_by_id('cphSearchArea_txtShelterPetFinderId')
    user_name_input = driver.find_element_by_id('cphSearchArea_txtUserName')
    pw_input = driver.find_element_by_id('cphSearchArea_txtPassword')
    signin_button = driver.find_element_by_id('cphSearchArea_btn_SignIn')



    shelter_id_input.send_keys(ORG_ID)
    user_name_input.send_keys(NAME)
    pw_input.send_keys(PW)
    signin_button.click()


    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, SELECTORS['Nav[Edit]']))
    )

    edit_dropdown = driver.find_element_by_css_selector(SELECTORS['Nav[Edit]'])
    animal_search_bttn = driver.find_element_by_css_selector(SELECTORS['Nav[Animal]'])


    ActionChains(driver).move_to_element(edit_dropdown).click(animal_search_bttn).perform()

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, SELECTORS['search_input']))
    )

    anumber_input = driver.find_element_by_css_selector(SELECTORS['search_input'])
    find_button = driver.find_element_by_css_selector(SELECTORS['find_button'])


    anumber_input.send_keys(anumber)
    find_button.click()

    try:
        WebDriverWait(driver, 30).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        pass

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, SELECTORS['Animal[Name]']))
    )

    animal_name_input = driver.find_element_by_css_selector(SELECTORS['Animal[Name]'])
    animal_breed_input = driver.find_element_by_css_selector(SELECTORS['Animal[Breed]:'])
    animal_colour_1_input = driver.find_element_by_css_selector(SELECTORS['Animal[Colour1]'])
    animal_colour_2_input = driver.find_element_by_css_selector(SELECTORS['Animal[Colour2]'])
    animal_location_input = driver.find_element_by_css_selector(SELECTORS['Animal[Location]'])
    animal_type_input = driver.find_element_by_css_selector(SELECTORS['Animal[Type]'])
    animal_img1_input = driver.find_element_by_css_selector(SELECTORS['Animal[Img1]'])








    animal_name = animal_name_input.get_attribute('value')
    animal_breed = animal_breed_input.get_attribute('value')
    animal_colour_1 = Select(animal_colour_1_input).first_selected_option.text.strip()
    animal_colour_2 = Select(animal_colour_2_input).first_selected_option.text.strip()
    animal_location = Select(animal_location_input).first_selected_option.text.strip()
    animal_type = Select(animal_type_input).first_selected_option.text.strip()
    animal_img1 = animal_img1_input.get_attribute('src')

    driver.close()

    return format_results({
        'name': animal_name,
        'breed': animal_breed,
        'colour1': animal_colour_1,
        'colour2': animal_colour_2,
        'location': animal_location,
        'type': animal_type,
        'img': animal_img1
    })
