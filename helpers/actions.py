from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def delay(timeout):
	def _wrap(f):
		def _f(*args):
			return series(wait(timeout), f(*args))
		return _f
	return _wrap


def wait(x):
	return lambda driver: sleep(x)


def go_to(host):
	return lambda driver: driver.get(host)


@delay(0.5)
def wait_and_click(locator):
	return lambda driver: WebDriverWait(driver, 30).until(EC.visibility_of_element_located(locator)).click()


@delay(0.5)
def wait_vis(locator):
	return lambda driver: WebDriverWait(driver, 30).until(EC.visibility_of_element_located(locator))


@delay(0.5)
def wait_invis(locator):
	return lambda driver: WebDriverWait(driver, 30).until(EC.invisibility_of_element_located(locator))


def assert_text(locator, text):
	return lambda driver: WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element(locator, text))


def get_text_from_element(locator):
	return lambda driver: WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator)).text


def series(*ser):
	def _x(driver):
		for s in ser:
			if callable(s):
				s(driver)
	return _x
