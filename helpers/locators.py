from selenium.webdriver.common.by import By


class CalcPageLocators(object):
	header = (By.CSS_SELECTOR, '.calc-col-content__h1')
	two_people = (By.CSS_SELECTOR, '.calc-col-content .step1 .form-radio-label[for="fr2"]')
	mite = (By.CSS_SELECTOR, '.antimite-type-controller[data-target="ak2"]')
	mite_is_active = (By.CSS_SELECTOR, '.antimite-type-controller.checked[data-target="ak2"]')
	region_list = (By.CSS_SELECTOR, '.calc-col-content #region-button')
	krasnodar = (By.CSS_SELECTOR, '#region-menu #ui-id-2')
	krasnodar_is_active = (By.CSS_SELECTOR, '.calc-col-content [aria-activedescendant="ui-id-2"]')
	promocod = (By.CSS_SELECTOR, '.calc-col-content [name="PROMOCODE"]')
	calc = (By.CSS_SELECTOR, '.calc-col-content button[name="calculate"]')
	price = (By.CSS_SELECTOR, '.calc-result #result-sum')
	number = (By.CSS_SELECTOR, '.calc-result #result-number')
