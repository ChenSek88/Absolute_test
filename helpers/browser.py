from selenium import webdriver


def with_driver(f):
	def _f(*args):
		driver = webdriver.Chrome()
		driver.maximize_window()
		result = f(*args)(driver)
		driver.quit()
		return result
	return _f
