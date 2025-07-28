import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait

from data import PHONE_NUMBER
from helpers import retrieve_phone_code


class UrbanRoutesPage:

    # Seção DE e PARA
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Selecionar tarifa e chamar taxi
    taxi_option_locator = (By.XPATH, "//button[text()='Chamar um táxi']")
    confort_icon_locator = (By.XPATH, "//img[contains(@src, 'kids')]")
    confort_active =(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')

    # Numero de telefone
    number_text_locator = (By.CSS_SELECTOR, '.np-button')
    number_enter = (By.ID, 'phone')
    number_confirm = (By.CSS_SELECTOR, '.button.full')
    number_code = (By.ID, 'code')
    code_confirm = (By.XPATH, '//button[contains(text(),"Confirmar")]')
    number_finish = (By.CSS_SELECTOR, '.np-text')

    #METODO DE PAGAMENTO
    add_metodo_pagamento = (By.CSS_SELECTOR, ".pp-button.filled")
    add_card = (By.CSS_SELECTOR, '.pp-plus')
    number_card = (By.ID, 'number')
    code_card = (By.CSS_SELECTOR, 'input.card-input#code')
    add_finish_card= (By.XPATH, '//button[contains(text(),"Adicionar")]')
    close_button_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    confrim_card = (By.CSS_SELECTOR, '.pp-value-text')

    # ADICIONAR COMENTARIO
    add_comment = (By.ID, 'comment')
    switch_blanket = (By.CSS_SELECTOR, "div.switch > span.slider.round")
    switch_blanket_active = (By.CSS_SELECTOR, "div.switch > input.switch-input")
    add_icecream = (By.CSS_SELECTOR, '.counter-plus')
    qnt_icecream = (By.CSS_SELECTOR, '.counter-value')
    call_taxi_button = (By.CSS_SELECTOR, '.smart-button')
    pop_up = (By.CSS_SELECTOR, '.order-header-tittle')


    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        WebDriverWait(self.driver, 3).until(
            Ec.visibility_of_element_located(self.from_field)
        )
        self.driver.find_element(*self.from_field).send_keys(from_text)

    def enter_to_location(self, to_text):
        WebDriverWait(self.driver, 3).until(
            Ec.visibility_of_element_located(self.to_field)
        )
        self.driver.find_element(*self.to_field).send_keys(to_text)

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_from_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            Ec.visibility_of_element_located(self.from_field)
        ).get_attribute('value')

    def get_to_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            Ec.visibility_of_element_located(self.to_field)
        ).get_attribute('value')

    def click_taxi_option(self):
        self.driver.find_element(*self.taxi_option_locator).click()

    def click_confort_icon(self):
        self.driver.find_element(*self.confort_icon_locator).click()

    def click_confort_active(self):
        try:
            active_button = WebDriverWait(self.driver, 10).until(
                Ec.visibility_of_element_located(self.confort_active))
            return "active" in active_button.get_attribute("class")
        except:
            return False

    def click_number_text(self, telefone):
        self.driver.find_element(*self.number_text_locator).click() #clica no numero

        self.driver.find_element(*self.number_enter).send_keys(telefone) #digita o numero

        self.driver.find_element(*self.number_confirm).click() #confirma o numero

        code = retrieve_phone_code(self.driver) #digita o codigo
        code_input = WebDriverWait(self.driver, 3).until(
            Ec.visibility_of_element_located(self.number_code)
        )
        code_input.clear()
        code_input.send_keys(code)

        self.driver.find_element(*self.code_confirm).click()  #Confirma

    def numero_confirmado(self):
        numero = WebDriverWait(self.driver, 10).until(
            Ec.visibility_of_element_located(self.number_finish))
        return numero.text

    def click_add_cartao(self,cartao,code):
        self.driver.find_element(*self.add_metodo_pagamento).click()
        self.driver.find_element(*self.add_card).click()
        time.sleep(1)
        self.driver.find_element(*self.number_card).send_keys(cartao)
        time.sleep(1)
        self.driver.find_element(*self.code_card).send_keys(code)
        time.sleep(1)
        self.driver.find_element(*self.add_finish_card).click()
        self.driver.find_element(*self.close_button_card).click()

    def confirm_cartao(self):
        return self.driver.find_element(*self.confrim_card).text


    def add_comentario(self, comentario):
        self.driver.find_element(*self.add_comment).send_keys(comentario)

    def comment_confirm(self):
        return self.driver.find_element(*self.add_comment).get_attribute('value')

    def switch_cobertor(self):
        self.driver.find_element(*self.switch_blanket).click()

    def switch_cobertor_active(self):
        # aguarda o checkbox real aparecer e verifica se está selecionado
        checkbox = WebDriverWait(self.driver, 10).until(
            Ec.presence_of_element_located(self.switch_blanket_active)
        )
        print("Cobertor está ativado?", checkbox.is_selected())  # Debug
        return checkbox.is_selected()